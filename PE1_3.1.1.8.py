# PE1
# 3.1.1.8 

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# largest_number = number1

# if number2 > largest_number:
#     largest_number = number2  
# if number3 > largest_number:
#     largest_number = number3 
# print("The largest number is: ", largest_number)


# 3.1.1.10

#var = input("Enther the name: ")
#if var == "Spathiphyllum":
#   print("Yes - Spathiphyllum is the best plant ever!")
#   if var == "spathiphyllum":
#       print("No, I want a big Spathiphyllum!")
#else:
#   print("Spathiphyllum! Not", var,"!")


# 3.1.1.12 if-elif-else
year = int(input("Enter a year: "))

if year >= 1582:
   if year % 4 != 0:
       print("It is a common year")
   elif year % 100 != 0:
       print("It is a leap year")
   elif year % 400 != 0:
       print("It is a common year")
   else:
       print("It is a leap year")
else:
     print ("Not within the Gregorian calendar period")


