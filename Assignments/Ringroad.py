print("Welcome to Ringroad travels\nWe provide you the best comfort and fast travel in the best price\n"
      "We have stop every 5Km apart and our rate is also very affordable standing at Rs.15 per 5km"
      "We have 6 stops across Ring Road:\n"
      " 1)Baneshwor \n 2)Gwarko \n 3)Ekantakuna \n 4)Kalanki \n 5)Balaju \n 6)Samakhusi")
you=0
go=0
dif=0
tot=0
stu=0
old=0
dis=0
gt=0


you=int(input("Where do  you want to start your ride press according to numbers above:"))
go=int(input("Where do you want to end your ride press according to numbers above:"))
dif=you-go
if dif==0:
      print("Total distance you have to travel is 30 km\n So you have to pay Rs.90\n")
      tot=90
elif dif== -5 or  dif==1:
      print("Total distance you have to travel is 25 km\n So you have to pay Rs.75\n")
      tot=75
elif dif==-4  or dif==2:
      print("Total distance you have to travel is 20 km\n So you have to pay Rs.60\n")
      tot=60
elif dif==-3  or dif==3:
      print("Total distance you have to travel is 15 km\n So you have to pay Rs.45\n")
      tot=45
elif dif==-2  or dif==4:
      print("Total distance you have to travel is 10 km\n So you have to pay Rs.30\n")
      tot=30
elif dif==-1 or dif==5:
      print("Total distance you have to travel is 5 km\n So you have to pay Rs.15\n")
      tot=15
else:
      print("Invalid")


stu=int(input("Are you a student?\n press 1 for yes and 2 for no:"))
old=int(input("\nIs your age more than 60?\n press 1 for yes and 2 for no:"))
if stu==1 or old==1:
      dis=0.10*tot
      print("\nYou have got discount of",dis)
else:
      print("\nSorry you are not valid for discount")

gt=tot-dis

print("\nYour grand total is",gt)



