#Design a function that should check the sides entered are valid or not.? If the sides of a triangle are valid, 
#then It should print the message to enter the angles. (Since the Sum of Angles in a triangle should be 180 Degrees).
#If the angles are also valid, Print a message that it is a valid triangle. 

def triangle_testing(x,y,z) :
  if x + y >= z and y + z >= x and z + x >= y :
     print("the sides are valid")
     angle_1 = int(input("enter the angle 1 :"))
     angle_2 = int(input("enter the angle 2 : "))
     angle_3 = int(input("enter the angle 3 : "))
     angle_sum = angle_1 + angle_2 + angle_3
     if angle_sum == 180 :
        print("valid triangle")
     else :
         print("the angles are not valid")
         
  else :
       print("sides are not valid")
    
a = int(input("enter the first side :"))
b = int(input("enter the second side : "))
c = int(input("enter the third side : "))
triangle_testing(a,b,c)
                  
