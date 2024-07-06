def checknum():
    num = int(input("Enter you number less than 10:"))

    match num:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3 | 4:
            print("3 or 4")
        case num if num == 5:
            print("number is 5")
        case num if num > 5:
            print("Number is greater than 5")    
        case _:
            print("Number is grater than 10")


checknum()



