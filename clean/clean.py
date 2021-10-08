import pandas as pd
import numpy as np

df = pd.read_csv("scrapes.csv")
df.drop(index=df[df["scrape_id"] == "scrape_id"].index, inplace=True)
df = df.astype(
    {
        "scrape_id": np.int32,
        "language_code": str,
        "inserted_at": np.datetime64,
        "position": np.int8,
        "brief_content_sections": str,
    }
)
df.sort_values(
    by=["language_code", "inserted_at", "scrape_id", "position"], inplace=True
)
df.reset_index(inplace=True, drop=True)
df[df.language_code == "en"]

df.to_csv("scrapes.csv", index=False)
