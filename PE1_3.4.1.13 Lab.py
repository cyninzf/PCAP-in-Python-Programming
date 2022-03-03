# 3.4.1.13 Lab: the basics of lists - the beatles

beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range (len(beatles)-2):
      beatles.append("Stu Sutcliffe")
      beatles.append("Pete Best") 
print("Step 3:", beatles)

del beatles[4]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

print("The Fab", len(beatles))

