#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./star_wars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Failed to fetch movie:', err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch movie with ID ${movieId}`);
    return;
  }
  const characters = body.characters;
  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        console.error('Failed to fetch character:', err);
        return;
  }
      console.log(body.name);
    });
  });
});
