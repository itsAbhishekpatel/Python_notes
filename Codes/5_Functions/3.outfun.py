def is_leap(year):
  """leap year logic"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year")
        return True
      else:
        # print("Not leap year")
        return False
    else:
    #   print("Leap year")
        return True
  else:
    # print("Not leap year")
    return False
  
# TODO: Add more code here 👇
def days_in_month(whichyear,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month != 2:
    return month_days[month-1]
  else:
    if is_leap(whichyear):
      return 29
    else:
      return 28
    
  
#🚨 Do NOT change any of the code below 
year = int(input("year")) # Enter a year
month = int(input("month")) # Enter a month
days = days_in_month(year, month)
print(days)

