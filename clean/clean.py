import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
df.drop(index=df[df["search_result_id"] == "search_result_id"].index, inplace=True)
df = df.astype(
    {"search_result_id": np.int32, "search_date": np.datetime64, "position": np.int8}
)
df.sort_values(
    by=["language_code", "search_date", "search_result_id", "position"], inplace=True
)
df.reset_index(inplace=True, drop=True)
df.to_csv("data_clean.csv", index=False)
