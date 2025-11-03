userReply = input(" Do you need to ship a package? ) (Enter yes or no) ")

if userReply == "yes":
    print( " We can help you ship that package!")
    
else:
    print("Please come back when you need to ship a package. Thank you!")
    
userReply = input(" Would you like to buy stamps, buy a an enevelope, or make a copy? (Enter stamps, enevelope, or copy) ")
if userReply == "stamps":
    print("we have many stamp design t choose from.")
elif userReply == "enevelope":
    print(" We have many enevelope sizes to choose from.")
elif userReply == "copy":
    copies = input(" How many copies would you like? (Eneter a number)")
    print(" Here are {} copies".format(copies))
else:
    print("thank you! Please come again.")