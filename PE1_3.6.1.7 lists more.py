# 3.6.1.7 Lists - more details 

my_list = [17,3,11,5,1,9,15,13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

# alternative
print("\n")
my_list = [17,3,11,5,1,9,15,13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list [i] > largest:
        largest = my_list[i]      
print(largest)


# 3.6.1.8 Lists - more details
print("\n")

my_list = [1,2,3,4,5,6,7,8,9,10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index: ", i)
else:
    print("Absent")

# 3.6.1.8 Lists - more details - lottery
print("\n")
drawn = [5,11,9,42,3,49]
bets = [3,7,11,42,34,49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1
        
print(hits)
