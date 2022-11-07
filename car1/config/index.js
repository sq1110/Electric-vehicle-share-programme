/*
 * @Author: 邹洋
 * @Date: 2022-04-06 17:53:44
 * @Email: 2810201146@qq.com
 * @LastEditors:  
 * @LastEditTime: 2022-04-06 17:55:51
 * @Description: 
 */
var path = require('path')
module.exports = {
  build: {
    index: path.resolve(__dirname, '../dist1/index.html'), // 编译输入的 index.html 文件
    assetsRoot: path.resolve(__dirname, '../dist1'), // 编译输出的静态资源路径
    assetsSubDirectory: 'static', // 编译输出的二级目录
    assetsPublicPath: '/', // 编译发布的根目录，可配置为资源服务器域名或 CDN 域名
    productionSourceMap: true, // 是否开启 cssSourceMap
    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false, // 是否开启 gzip
    productionGzipExtensions: ['js', 'css'] // 需要使用 gzip 压缩的文件扩展名
  }
}
