inp = input("What's the name of the file? - ")
try:
    fhand= open(inp)

except:
    print(inp, "does not exist")
    quit()

count = 0
for line in fhand:
    count = count + 1
print("There are " , count , "lines in " , inp )
