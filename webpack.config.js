const path = require("path");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const PROD = process.env.NODE_ENV == 'production';
const BUILD_PATH = "./marble/static/build/";
const STATIC_PATH = "https://" + process.env.AWS_S3_CUSTOM_DOMAIN + BUILD_PATH;

module.exports = {
  plugins: [
    new MiniCssExtractPlugin(
      {filename: '[name].css', chunkFilename: '[id].css'}
    )
  ],
  entry: {
    index: ['./marble/src/marble.scss'],
  },
  output: {
    path: path.resolve(__dirname, BUILD_PATH)
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
            loader: MiniCssExtractPlugin.loader
          }, {
            loader: 'file-loader',
            options: {
              name: "[name].css",
              publicPath: PROD ? STATIC_PATH : BUILD_PATH
            }
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
