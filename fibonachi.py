__author__ = 'z'

# first 50
x=0
y=1
sum = x+y
print("number 1 is: ", 0)
print("number 2 is: ", 1)

for i in range(3,51):
    x = y
    y = sum
    sum = x + y
    print("number " + str(i) + " is: "+str(sum))


#  smaller then 10000
print ("\n\nsmaller then 10000")
x=0
y=1
sum = x+y
while sum <10000:
    print (sum)
    x=y
    y=sum
    sum=x+y



