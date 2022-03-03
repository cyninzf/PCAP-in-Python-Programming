# 3.4.1.9 Lists - collections of data | list methods

my_list = []

for i in range(5):
      my_list.insert(0, i+1)
print(my_list)


#3.4.1.10 Lists - collections of data | lists and loops
print("\n")

my_list = [10,1,8,3,5]
total = 0

for i in range (len(my_list)):
      total += my_list[i]

print(total)

#3.4.1.12 Lists - collections of data | lists and loops
print("\n")

my_list = [10,1,8,3,5]
length = len(my_list)

for i in range (length //2):
      my_list[i], my_list[length - i -1] =  my_list[length - i -1],my_list[i]

print(my_list)
