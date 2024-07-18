import pandas
# make alis for it pandas
import pandas as pd

mydataset = {
    'cars':["volov","honda","mustang"],
    'passing':[1,2,0]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

price = [10,20,30]

new_p = pd.Series(price, index=["x","y","z"])  #return a column, also can use index to chnage the dfault index value
print(new_p)

mydic = {
    "name":"abhishek",
    "age":34 
}

keys = pd.Series(mydic)

print(keys)

