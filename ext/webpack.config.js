const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: {
        content: path.resolve(__dirname, './src/content.js'),
        background: path.resolve(__dirname, './src/background.js'),
    },
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: '[name].js',
    },
    mode: 'development',
    plugins: [
        new CopyWebpackPlugin({
            patterns: [
                { from: path.resolve(__dirname, './src/static'), to: path.resolve(__dirname, './dist') },
                { from: path.resolve(__dirname, './manifest.json'), to: path.resolve(__dirname, './dist/manifest.json')}
            ]
        }),
    ]
};