const knexLib = require("knex");
const knexConfig = require("./knexfile.js");

const knex = knexLib(knexConfig);

module.exports = knex;
