#Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid 
#that can be built using these blocks.

#Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks 
#and cannot complete the next layer, they finish their work immediately.

#answer:

blocks = int(input("Enter the number of blocks: "))
height = 0
total_blocks = 0
    
while total_blocks <= blocks :
        height += 1
        total_blocks += height
        
        
if total_blocks > blocks :
        height -= 1
print("the height of the pyramid that can built is:",height)
        