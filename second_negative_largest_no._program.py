#Write a program to find the second-largest negative number in a list.\

def find_number(my_list) :
   
      print("second largest negative number is : ",my_list[r])
    


my_list = []
n = int(input("enter the no.of ekements in the list : "))
for i in range(n) :
    value = int(input("enter the value : "))
    my_list.append(value)

my_list.sort()
r = n-2

find_number(my_list)

# output :

#enter the no.of ekements in the list : 5
#enter the value : -1
#enter the value : -5
#enter the value : -2
#enter the value : -7
#enter the value : -3
#second largest negative number is :  -2



