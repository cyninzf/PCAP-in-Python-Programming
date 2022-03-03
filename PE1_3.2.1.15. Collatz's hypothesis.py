# 3.2.1.15 LAB: Collatz's hypothesis15

c0 = int(input("Please enter a number: ")) 
steps = 0

while c0:
    if c0 <= 0:
        break
    elif c0 == 1:
        break
    elif c0 % 2 == 0:
        c0 = c0 / 2
        print (int(c0))
    else:
        c0 = 3 * c0 + 1
        print (int(c0))
    steps += 1

print("steps: ", steps)
