# 1.0

def counter(start_num):
    list = []
    for x in range(start_num,0,-1):
        list.append (x)
    return list
print(counter(100))

#2.0

def outputmix(list):
    print(list[0])
    return(list[1])
print(outputmix([10,50]))

# 3.0

def fubar(list):
    return list[0] + len(list)
print(fubar([27,5,21,29,45,2,97]))

# 4.0

def issues(list):
    if len(list) < 2:
        return False
    newlist = []
    for x in list:
        if x > list[1]:
            newlist.append(x)
    print(len(newlist))
    return newlist

print(issues([41,5,13,5,34]))
print(issues([7]))

# 5.0

def crazy(length,value):
    list = []
    for x in range (0,length,1):
        list.append (value)
    return list
print(crazy(5,10))