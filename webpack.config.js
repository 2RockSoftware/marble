const path = require("path");

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const KssWebpackPlugin = require('kss-webpack-plugin');

module.exports = {
  plugins: [
    new MiniCssExtractPlugin(
      {filename: '[name].css', chunkFilename: '[id].css'}
    ),
    new KssWebpackPlugin({
      source: './marble/static/scss',
      destination: './marble/templates/styleguide/build',
      title: 'Two Rock Software Style Guide',
      builder: './src/theme',
      homepage: './src/styleguide.md'
    })
  ],
  entry: {
    index: './src/index.js',
    home: ['./src/home.js', './static/scss/home.scss'],
    style: './marble/static/scss/cms.scss',
    kss: './marble/static/scss/kss.scss'
  },
  output: {
    path: path.resolve(__dirname, "marble/static/build")
  },
  module: {
    rules: [
      {
        test: /\.(woff|woff2|eot|svg)$/,
        use: {
          loader: 'url-loader'
        }
      }, {
        test: /\.(sa|sc|c)ss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              publicPath: '/static'
            }
          }, {
            loader: 'css-loader'
          }, {
            loader: 'sass-loader'
          }
        ]
      }
    ]
  },
  watchOptions: {
    ignored: 'node_modules/**'
  }
};
