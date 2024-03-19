#Your task is to write a program which removes all the number repetitions from the list. 
#The goal is to have a list in which all the numbers appear not more than once.

#Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out
#a conversation with the user and obtain all the data from her/him.

#Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

#answer :

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_numbers =[]

for my_list in my_list :
     if my_list not in unique_numbers :
         unique_numbers.append(my_list)# Write your code here.

print("The list with unique elements only:")
print(my_list)
