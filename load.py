import pandas as pd
import numpy as np
import json

dtypes = {"scrape_id": np.int32, "position": np.int8}
parse_dates = ["inserted_at"]
converters = {"brief_content_sections": json.loads}
df = pd.read_csv(
    "scrapes_clean.csv", dtype=dtypes, parse_dates=parse_dates, converters=converters
)
print(df)