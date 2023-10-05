#code to find the average for a set of numbers
my_list = list()
pro = print("input done when all the numbers have been inputed")
while True :
    inp = input("input number: ")
    if inp == "done" : break
    try:
        value = float(inp)
    except:
        print("not a number")
        quit()

        
    my_list.append(value)

    ave = sum(my_list) / len(my_list)
print("The mean =", ave)