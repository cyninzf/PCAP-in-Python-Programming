# more example of break instruction

largest_number = -99999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to stop: "))
    if number == -1:
        break
    counter +=1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
