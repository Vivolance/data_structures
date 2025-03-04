import pandas as pd
from pandas.core.groupby import DataFrameGroupBy

# Reading csv files
df: pd.DataFrame = pd.read_csv("src/1_pandas/sample.csv")
print(df)

# Count all rows in each column that are not null
print(df.count())

# Filter for 1st and 2nd row, 1st and 2nd columns
# iloc takes in [range_of_row_index, range_of_col_index]
filtered_df: pd.DataFrame = df.iloc[0:2, 0:2]
print(filtered_df)

# Returns a serires of bools that shows whether each row contains jaosn or not
contains_jason: pd.Series = df["name"].str.contains("jason")
print(contains_jason)

# Group by
filtered_df_2: pd.DataFrame = df.iloc[:, 0:2]
name_groupby: DataFrameGroupBy = filtered_df_2.groupby("name")
value_count_df: pd.Series = name_groupby.value_counts(["age"])
print(value_count_df)

# taking mean of the entire df, ensure that the columns other than the groupby can be averaged
mean_age: pd.Series = name_groupby.mean()
print(mean_age)

# Sum of ages
sum_age: pd.Series = name_groupby.sum()
print(sum_age)

# Creating indexes, so that searching using loc is O(1)
df: pd.DataFrame = pd.read_csv("src/1_pandas/sample.csv")
copy_df: pd.DataFrame = df.set_index(["town"])
print(copy_df)

# Searching by index, returning everything of that index
only_amk: pd.DataFrame = copy_df.loc["punggol"]
print(only_amk)

# slicing the df, from bishan to punggol, return the name only
only_amk: pd.DataFrame = copy_df.loc["bishan":"punggol", "name"]
print(only_amk)

# Resetting the index, slower search since index is dropped
df_reset: pd.DataFrame = copy_df.reset_index()

# Creating a data structure and writing it into a csv
my_list: list[dict[str, int]] = [
    {
        "car": 10, "price": 12000
    },
    {
        "car": "nissan", "price": 10000
    },
    {
        "car": "kia", "price": 15000
    }
]

df: pd.DataFrame = pd.DataFrame(my_list)
print(df)
df.to_csv("src/1_pandas/car_list.csv", index=False)
