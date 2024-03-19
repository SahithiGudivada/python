#Write a function that should return the Hypotenuse of the Triangle.

#answer


def calculate_hypotenuse(x,y) :
  hypotenuse = int(((side1**2 + side2**2))**0.5)
  return hypotenuse
    
side1 = int(input("enter the side1 : "))
side2 = int(input("enter the side2 : "))

print(calculate_hypotenuse(side1,side2))