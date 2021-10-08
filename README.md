# AI Hackaton Data

## Description
In general, provided data contains scraped web pages from Google search results. The structure of data is enforced by Surfer's application flow. 

Each search result has fields `id`, `keyword`, `search_date`, `language_code` and 20 first webpages ordered by field `position`. Each webpage consists of `content_sections` extracted from its HTML. A single section consists of `heading`, `heading_level` and `content`. For the curious: `content` are simply merged \<p> paragraphs under given heading.

Collected data is multilingual, but 70% of searches are in English. You can go multilingual or limit scope to `en` only, we are totally ok with it.

There are about 23,000 search results, each containing 20 webpages. That gives 460,000 scraped webpages and millions of sections.

## Tasks
We propose several tasks that can be accomplished using given data but teams are **very welcome to propose own ideas** how to leverage Surfer's data.
Our tasks:
* Keyword extraction
* Topic modelling
* Revealing most important words/phrases/topics
* Paraphrasing
* Text completion
* Whole article generation (list of unique headings and contents based on scraped websites)
* yours
  
## Download
Download data from [here](https://console.cloud.google.com/storage/browser/pwr_hackaton?project=dogebot-1198). Select `data_clean.csv` .
## Loading
``` Python
import pandas as pd
import numpy as np
import json

dtypes = {"search_result_id": np.int32, "position": np.int8}
parse_dates = ["search_date"]
converters = {"content_sections": json.loads}
df = pd.read_csv(
    "data_clean.csv", dtype=dtypes, parse_dates=parse_dates, converters=converters
)
```