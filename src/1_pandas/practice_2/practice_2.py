"""
Task: Given a people.csv and has_car.csv, do the following manipulation

1. Deduplicate
2. Create an sqlalchemy engine to upload these results into a PG DB.
3. Group by jobs and rank from highest income to lowest
4. Join to see how many people below the income of 100000 has car
"""

import pandas as pd
from sqlalchemy import create_engine, Engine

df_people: pd.DataFrame = pd.read_csv("src/1_pandas/practice_2/people.csv")
df_has_car: pd.DataFrame = pd.read_csv("src/1_pandas/practice_2/has_car.csv")

# 1. Deduplicate both of them
# Setting ignore index renumbers the auto-indexing, if not the removed index is skipped ie 5 -> 7, 6 is removed
df_people = df_people.drop_duplicates(keep="first", ignore_index=True)
print(df_people)

# 2. Upload to Postgres
engine: Engine = create_engine(
    "postgresql+psycopg2://postgres@localhost:5432/data_structures_practice"
)

# Note this way of writing to DB is not the most ideal, your table do not have Pkey or Fkey contraints.
# To have Pkey or Fkey constraint, use SQLAlchemy Tables to create the table first, then write using to_sql
df_people.to_sql(name="people", con=engine, if_exists="replace", index=False)

# 3. group by jobs, orderby income desc
# Analogous to orderby descending / ascending
df_people = df_people.sort_values(by=["job", "income"], ascending=[True, False])
print(df_people)

# 4. Join to see how many people above the income of 100000 have cars
df_merge: pd.DataFrame = df_people.merge(df_has_car, how="left", on="id")

# Returns id, name, income, has_car with those income < 100000.00 and has car
mask = (df_merge["has_car"]) & (df_merge["income_y"] < 100000.00)
filtered_df_merge: pd.DataFrame = df_merge.loc[
    mask, ["id", "name_x", "income_x", "has_car"]
]

print(filtered_df_merge)
