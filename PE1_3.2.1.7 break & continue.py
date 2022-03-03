# break - example

print("The break instruction:")
for i in range (2, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example

print("\nThe continue instruction:")
for i in range(2, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

    
# 3.2.1.8 break & continue

print("\n")
largest_number = -999999
counter = 0 

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
       break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is: ", largest_number)
    print("The count is: ", counter)
else:
    print("You haven't entered any number.")


# 3.2.1.8 break 2

print("\n")
largest_number = -999999
counter = 0 
number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
       continue
    counter += 1
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is: ", largest_number)
else:
    print("You haven't entered any number.")


# 3.2.1.9: more example of break - stuck in a loop

print("\n")
while True:
    word = input("Enter a word: ")
    if word == "chupacabra":
        break
print("You've successfully letf the loop!")
