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
print(df)
