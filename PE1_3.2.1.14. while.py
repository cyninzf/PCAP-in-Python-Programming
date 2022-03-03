# 3.2.1.14 LAB: Essentials of the while loops

blocks = int(input("Enter the number of blocks: "))
height = 0

while blocks:
    blocks = blocks - height
    if blocks == 0:
        break
    elif blocks <= height:
        break
    else:
        height += 1

print("The height of the pyramid:", height)
