const syntaxHighlight = require('@11ty/eleventy-plugin-syntaxhighlight')
const eleventyNavigationPlugin = require('@11ty/eleventy-navigation')
const toBootstrapNav = require('eleventy-navigation-bootstrap')
const pluginTOC = require('eleventy-plugin-toc')
const markdownIt = require('markdown-it')
const markdownItAnchor = require('markdown-it-anchor')
const markdownItHighlightJS = require('markdown-it-highlightjs')
const readerBar = require('henry-reader-bar')
const readingTime = require('henry-reading-time')

const mdOptions = {
  html: true,
  breaks: true,
  linkify: true,
  typographer: true,
}

const mdAnchorOpts = {
  permalink: true,
  permalinkClass: 'anchor-link',
  permalinkSymbol: '',
  level: [1, 2, 3, 4],
}

module.exports = function (eleventyConfig) {
  eleventyConfig.setLibrary(
    'md',
    markdownIt(mdOptions)
      .use(markdownItAnchor, mdAnchorOpts)
      .use(markdownItHighlightJS)
  )

  eleventyConfig.addPlugin(eleventyNavigationPlugin)
  eleventyConfig.addPlugin(readingTime)
  eleventyConfig.addPlugin(readerBar)
  eleventyConfig.addPlugin(syntaxHighlight)

  eleventyConfig.addPlugin(pluginTOC, {
    tags: ['h2', 'h3'],
    ul: true,
  })

  eleventyConfig.addPassthroughCopy('_src/assets')
  eleventyConfig.addPassthroughCopy('_src/localStyles')

  eleventyConfig.addNunjucksFilter('bootstrapNav', toBootstrapNav)

  eleventyConfig.addLinter(
    'Spelling check',
    function (content, inputPath, outputPath) {
      let words = 'lenght, .lenght, .rigth'.split(',')

      // Eleventy 1.0+: use this.inputPath and this.outputPath instead
      if (inputPath.endsWith('.md')) {
        for (let word of words) {
          let regexp = new RegExp('\\b(' + word + ')\\b', 'gi')
          if (content.match(regexp)) {
            console.warn(`Spelling check (${inputPath}) Found: ${word}`)
          }
        }
      }
    }
  )

  return {
    dir: {
      layouts: '/_src/layouts',
      data: '/_src/data',
      output: '_dist',
    },
  }
}
