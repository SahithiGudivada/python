#step 1: create an empty list named beatles;
#step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
#step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
#step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
#step 5: use the insert() method to add Ringo Starr to the beginning of the list


#answer:

beatles =[]# step 1
print("Step 1:", beatles)

beatles.append( "John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")  # step 2

for i in range (2) :# step 3
  member = input("enter the members of the band list :")
  beatles.append(member)
print("Step 3:", beatles)

del beatles[3:]# step 4
print("Step 4:", beatles)

beatles.insert(0,"ringo star")# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

