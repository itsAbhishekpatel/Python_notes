import pandas as pd

dict1 = {
    "name":["abhi","nik"],
    "age":[19,20],
    "city":["hui","lop"]
}

df = pd.DataFrame(dict1,index=["1","2"])

print(df)