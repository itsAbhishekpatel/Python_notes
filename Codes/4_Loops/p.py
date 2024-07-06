# Write your code below this line 👇
def prime_checker(num):
  if num == 0 or num == 1:
    print("It's not a prime number.")
  elif num >2:
    if num % num-1 == 0:
      print("It's not a prime number.")
    else:
      num -= 1
      prime_checker(num)
  else:
    print("It's a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(n)