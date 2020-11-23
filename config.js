const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  performance: {
    maxEntrypointSize: 512000,
    maxAssetSize: 512000
  },
  entry: './hydros/assets/js/main.js',
  output: {
    filename: 'main.js',
    path: path.join(__dirname, 'hydros/static/webpack'),
  },
  module: {
    rules: [
      {
        test: /\.(sass)$/,
        use: [ MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: './main.css'
    })
  ]
}
