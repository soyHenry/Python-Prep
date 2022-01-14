const Cache = require('@11ty/eleventy-cache-assets')

module.exports = async function () {
  const url = 'https://henry-11ty-resources.s3.sa-east-1.amazonaws.com/Styles/header.css'
  const style = await Cache(url, {
    duration: '1d',
    type: 'txt',
    directory: '_cache'
  })
  return style
}
