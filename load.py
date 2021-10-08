import pandas as pd
import numpy as np
import json

dtypes = {"search_result_id": np.int32, "position": np.int8}
parse_dates = ["search_date"]
converters = {"content_sections": json.loads}
df = pd.read_csv(
    "data_clean.csv", dtype=dtypes, parse_dates=parse_dates, converters=converters
)
print(df)
