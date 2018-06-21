var path = require("path");

module.exports = {
  context: __dirname,
  entry: "./javascripts/pokemon_lets_go.js",
  output: {
    path: path.resolve(__dirname, 'javascripts'),
    filename: "bundle.js"
  },
  devtool: 'source-map',
  resolve: {
    extensions: [".js", "*"]
  }
};