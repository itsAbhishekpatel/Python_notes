age = int(input("Enter your age:"))

# Here it the if else conditional statments 
if age > 18 or age == 18:
    print("You are adult",end=" ")

    if age > 50:
        print("and You are old to ;;)")

elif age < 18 and age > 0:
    print("you are minor")

else:
    print("Please enter your correct age.")



