# 1.0 Basic
integers=[x for x in range(151)]
print (integers)

# 2.0 Multiples of 5
bounce=[x for x in range(0,1005,5)]
print (bounce)

# 3.0 Counting the Dojo Way
for x in range(0,101):
    if x % 5 != 0:
        print(x)
    elif x % 5 == 0 and x % 10 !=0:
        print('Coding')
    else:
        print('Coding Dojo')

# 4.0 Whoa
sum=0
for x in range(0,500000):
    if x % 2 != 0:
        sum=sum+x
print(sum)

# 5.0 Countdown by 4s

x = 2018
while x >= 0:
    if x % 4 == 0:
        print(x)
    x = x-1

#6.0 Flexible Counter
low_Num = 0
high_Num = 50
multi = 10
for x in range(low_Num,high_Num+1):
    if x % multi == 0 and x != 0:
        print (x)