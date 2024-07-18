import pandas as pd

data = {
    "calarious":[420,500,300],
    "duration":[50,40,60]
}

# load data into data frame 
df = pd.DataFrame(data, index=["x","y","z"])

print(df)

print(df.loc["x"]) # you can locate the row's value 

print(df.loc[["x","y"]])

