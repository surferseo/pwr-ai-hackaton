const fs = require("fs");
const path = require("path");

const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const DIR = "surferlocal-data";

module.exports = {
  gql(query, variables) {
    return fetch("https://app.surferlocal.com/api/gql", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query, variables }),
    })
      .then((resp) => resp.json())
      .then((resp) => {
        if (!resp.data) {
          throw resp;
        }

        return resp.data;
      });
  },

  storeJson(filename, data) {
    return new Promise((resolve) => {
      fs.mkdir(DIR, { recursive: true }, () => {
        fs.writeFile(path.join(DIR, filename), JSON.stringify(data), () => {
          resolve();
        });
      });
    });
  },

  PLACES_QUERY: `{
    places {
      __typename
      id
      touchedAt
      insertedAt
      
      latestPlaceSnapshot {
        __typename
        id
        title
        address
        snippet
        mainImage
        ogTitle
        ogImage
        ogDescription
        insertedAt
        googlePlaceId
        googleCid
      }
    }
  }`,

  GRIDS_QUERY: `
  query PlaceGrids($placeId: GUID!) {
    latestGrids(placeId: $placeId) {
      __typename
      id
      sharedPermalink
      query
      centerLatitude
      centerLongitude
      country
      language
      place {
        __typename
        id
      }
      competitors {
        __typename
        id
        averagePosition
        queryPlace {
          ...GridQueryPlace
        }
      }
      audits {
        __typename
        id
        latitude
        longitude
        isError
        isPinned
        insertedAt
        difficulty
        position
        hasGuidelines: hasDescriptions
        ogTitle
        metadataLatitude
        metadataLongitude
        queryOrigin {
          latitude
          longitude
        }
        queryPlaces {
          ...GridQueryPlace
          titleMetrics {
            ...StringMetrics
          }
          descriptionMetrics {
            ...StringMetrics
          }
          postsMetrics {
            ...StringMetrics
          }
          replyMetrics {
            ...StringMetrics
          }
          reviewsMetrics {
            ...StringMetrics
          }
          urlMetrics {
            ...StringMetrics
          }
        }
        titleProminentPhrases {
          ...ProminentPhrase
        }
        descriptionProminentPhrases {
          ...ProminentPhrase
        }
        reviewsProminentPhrases {
          ...ProminentPhrase
        }
        postsProminentPhrases {
          ...ProminentPhrase
        }
      }
    }
  }
  
  fragment GridQueryPlace on QueryPlace {
    __typename
    id
    position
    distance
    placeSnapshot {
      __typename
      id
      address
      title
      description
      phone
      rating
      reviewsCount
      imagesCount
      link
      category
      additionalCategories
      googlePlaceId
      googleCid
      latitude
      longitude
      unclaimed
      mainImage
      ogImage
      ogTitle
      ogDescription
      unclaimed
      link
      phone
      address
    }
  }
  
  fragment ProminentPhrase on ProminentPhrase {
    __typename
    id
    pages
    phrase
    occurrences
    position
    scoreSum
    scoreValue
    inTop5: inTopN(n: 5)
    origins {
      position
    }
  }
  
  
  fragment StringMetrics on StringMetrics {
    __typename
    id
    averageWordsCount
    exactKeywordDensity
    exactKeywordsCount
    graphemesCount
    partialKeywordDensity
    partialKeywordsCount
    wordsCount
  }
  `,
};
