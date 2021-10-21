# AI Hackaton Data

## Description
In general, provided data contains scraped web pages from Google search results.

Each search result has fields: `search_result_id`, `keyword`, `search_date`, `country_language_code`, `country_name`, `city_name`, `latitude`, `longitude`, `device`(mobile or desktop), and 20 first webpages ordered by field `position`. Each webpage has `url`, `content_score`(calculated with Surfer's rules), `title`(from HTML head) and two content columns: `content_sections` and `content_unstructured` extracted from its HTML. `content_unstructured` is whole page content concatenated into one great string. `content_sections` is structured and much cleaner representation. A single section consists of `heading`, `heading_level` and `content`. For the curious: `content` are simply merged \<p> paragraphs under given heading.

Collected data is multilingual, but 70% of searches are in English. You can go multilingual or limit scope to `en` only, we are totally ok with it.

There are about 21,000 search results, each containing 20 webpages. That gives 420,000 scraped webpages and millions of sections.

## Tasks
We propose several tasks that can be accomplished using given data but teams are **very welcome to propose own ideas** how to leverage Surfer's data.
Our tasks:
* Keyword extraction
* Revealing most important words/phrases/topics
  * unsupervised way, e.g. finding most frequent words but excluding stopwords
  * supervised way, with use of page position, kind of Google reverse engineering
* Paraphrasing
* Text completion
* Whole article generation (list of unique headings with contents based on scraped websites)
* Check if `seo score`, calculated with Surfer rules, correlates with page positions in search result
* Find interesting dependencies in data
* Visualise data in a nontrivial way
* ... your tasks, just have fun!
  
## Download
Download data from here:

- [data_clean.csv](https://storage.cloud.google.com/pwr_hackaton/data_clean.csv)

ask for pendrive or...

...let's connect P2P via [sharedrop](https://www.sharedrop.io/).
## Loading
``` Python
import pandas as pd
import numpy as np
import json

dtypes = {
    "search_result_id": np.int32,
    "position": np.int8,
    "content_score": pd.Int8Dtype(),
    "latitude": np.float32,
    "longitude": np.float32,
}
parse_dates = ["search_date"]
converters = {"content_sections": json.loads}
names = [
    "search_result_id",
    "keyword",
    "search_date",
    "position",
    "city_name",
    "country_name",
    "country_language_code",
    "latitude",
    "longitude",
    "url",
    "content_score",
    "device",
    "title",
    "content_sections",
    "content_unstructured",
]
df = pd.read_csv(
    "data.csv.gz",
    dtype=dtypes,
    parse_dates=parse_dates,
    converters=converters,
    names=names,
)
df.sort_values(
    by=[
        "country_language_code",
        "search_date",
        "country_name",
        "city_name",
        "search_result_id",
        "position",
    ],
    inplace=True,
)
```
## Sampling
Collected data comes from last 4 months. To sample it, simply cut scope to fewer months, e.g last 2 months. Alternatively you can take alternate days.

## Presentations
We'd like you to present project results on 5-10 minutes presentation. Presetation may be a story that answers below questions:
- what kind of data you used?
- what task you solved?
- what you discovered?
- how accurate is proposed solution?
- what you learned?
- what can be done in the future?
  
Send presentation link to maciejgruszczynski@surferseo.com, please.

Cheers !