# more example of continue instruction

largest_number = -99999
counter = 0

number = int(input("Enter a number or type -1 to stop: "))

while number != -1:
    if number == -1:
        continue
    counter +=1
    
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to stop: "))
    
if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
