#Your task is very simple here: write a program that uses a for loop to "count mississippily" to five.
#Having counted to five, the program should 
#print to the screen the final message "Ready or not, here I come!"


#answer:

import time

for i in range(1,6):# Write a for loop that counts to five.
       print(i,"mississippi") # Body of the loop - print the loop iteration number and the word "Mississippi".
       time.sleep(1)# Body of the loop - use: time.sleep(1)

print("Ready or not, here I come!")# Write a print function with the final message.


