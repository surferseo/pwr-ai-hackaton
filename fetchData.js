const { gql, storeJson, PLACES_QUERY, GRIDS_QUERY } = require("./api");

fetchPlaces()
  .then((places) => Promise.all(places.map(fetchPlaceGrids)))
  .then(() => process.exit(0));

function fetchPlaces() {
  return gql(PLACES_QUERY).then((data) =>
    storeJson("places.json", data).then(() => {
      console.log("fetched and saved places");

      return data.places;
    })
  );
}

function fetchPlaceGrids(place) {
  return gql(GRIDS_QUERY, { placeId: place.id })
    .then((data) =>
      storeJson(`grids ${place.id}.json`, data).then(() => place.id)
    )
    .then((placeId) => console.log(`fetched and saved place ${placeId}`));
}
