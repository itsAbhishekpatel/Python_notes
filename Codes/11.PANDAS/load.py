import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r"C:\Users\Abhishek.Patel\OneDrive - 365shl\Desktop\Git\Python\Codes\11.PANDAS\data.csv")

# use r or \\ 
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
print(df)

# Tip: use to_string() to print the entire DataFrame.

# print(df.to_string())

print(df.tail()) #deafult 5 values return

df.plot() # plot the data 

plt.show() # use pyplot in matplot lib to show data use plt funtion 






