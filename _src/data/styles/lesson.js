const Cache = require('@11ty/eleventy-cache-assets')

module.exports = async function () {
  const url = 'https://d31uz8lwfmyn8g.cloudfront.net/Styles/lesson.css'
  const style = await Cache(url, {
    duration: '1d',
    type: 'txt',
    directory: '_cache'
  })
  return style
}
