# Write your code below this line 👇
# check number is prime or not 
def prime_checker(number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
         
        
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Enter:")) # Check this number
prime_checker(number=n)
