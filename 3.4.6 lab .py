#Your task is to:

#write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
#write a line of code that removes the last element from the list (Step 2)
#write a line of code that prints the length of the existing list (Step 3)

#answer :

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

number = int(input("enter the number : "))# Step 1: write a line of code that prompts the user
middle_index = len(hat_list)//2# to replace the middle number with an integer number entered by the user.

hat_list[middle_index] = number# Step 2: write a line of code that removes the last element from the list.

print(len(hat_list))# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)

