import pandas as pd

results = pd.read_csv("data/results.csv")
drivers = pd.read_csv("data/drivers.csv")
races = pd.read_csv("data/races.csv")
constructors = pd.read_csv("data/constructors.csv")

df = results.merge(drivers, on="driverId", how="left")
df = df.merge(races[["raceId", "year", "name", "date"]], on="raceId", how="left")
df = df.merge(constructors, on="constructorId", how="left")

df["driver_name"] = df["forename"] + " " + df["surname"]
df["constructor_name"] = df["name_y"]

driver_yearly = (
    df.groupby(["year", "driver_name"])["points"]
    .sum()
    .reset_index()
)

total_driver_points = (
    driver_yearly.groupby("driver_name")["points"]
    .sum()
    .reset_index()
    .sort_values(by="points", ascending=False)
)

constructor_yearly = (
    df.groupby(["year", "constructor_name"])["points"]
    .sum()
    .reset_index()
)

total_constructor_points = (
    constructor_yearly.groupby("constructor_name")["points"]
    .sum()
    .reset_index()
    .sort_values(by="points", ascending=False)
)

df["position"] = pd.to_numeric(df["position"], errors="coerce")
df["grid"] = pd.to_numeric(df["grid"], errors="coerce")
grid_data = df.dropna(subset=["position", "grid"]).copy()
all_driver_names = df["driver_name"].dropna().unique()

circuits_df = pd.read_csv("data/circuits.csv")
