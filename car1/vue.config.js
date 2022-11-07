/*
 * @Author: 邹洋
 * @Date: 2022-04-06 16:42:25
 * @Email: 2810201146@qq.com
 * @LastEditors:  
 * @LastEditTime: 2022-04-06 17:59:27
 * @Description: 
 */
module.exports = {
    // 基本路径
    baseUrl: './',
    // 输出文件目录
    outputDir: 'dist',
    // webpack-dev-server 相关配置
    devServer: {
      // 跨域
      proxy: {
      // 只要axios请求中带有/api的url,就会触发代理机制
      '/api': {
         // 目标路径：target(我们要代理请求的地址)
         target: 'http://localhost:5590/',
         // 允许跨域
         changOrigin: true,
         // 重写路径 api代替了目标路径
         pathRewrite: {
           '^/api': ''
         }
        }
      },
    },
  }