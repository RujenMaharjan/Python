print("Welcome To Carrier Bonus Services"
      "\nWe provide you bonus on calling"
      "\nFor every 10 minutes you talk you get bonus according to sim carrier you use")
you =0
the =0
min =0
tot =0
you=int(input("Press accordingly\n"
              "1)NTC\n"
              "2)Ncell\n"
              "Which carrier do you use:"))
the=int(input("\nIn which carrier do you want to call:"))
min=int(input("How many minutes would you like to talk:"))
if you==1 and the==1:
    if min > 0 and min <= 10:
        tot=0.5
    elif min>10 and min<=20:
        tot=2*0.5
    elif min>20 and min<=30:
        tot=3*0.5
    elif min>30 and min<=40:
        tot=4*0.5
    elif min>40 and min<=50:
        tot=5*0.5
    elif min>50 and min<=60:
        tot=6*0.5
    elif min>60 and min<=70:
        tot=7*0.5
    elif min>70 and min<=80:
        tot=8*0.5
    elif min>80 and min<=90:
        tot=9*0.5
    elif min>80 and min<=100:
        tot=10*0.5
    else:
        print("Out of reach")
        exit()
if you==1 and the==2:
    if min>0 and min<=10:
        tot=2
    elif min>10 and min<=20:
        tot=2*2
    elif min>20 and min<=30:
        tot=3*2
    elif min>30 and min<=40:
        tot=4*2
    elif min>40 and min<=50:
        tot=5*2
    elif min>50 and min<=60:
        tot=6*2
    elif min>60 and min<=70:
        tot=7*2
    elif min>70 and min<=80:
        tot=8*2
    elif min>80 and min<=90:
        tot=9*2
    elif min>80 and min<=100:
        tot=10*2
    else:
        print("Out of reach")
        exit()
if you == 2 and the == 2:
    if min > 0 and min <= 10:
        tot = 5
    elif min > 10 and min <= 20:
        tot = 2 * 5
    elif min > 20 and min <= 30:
        tot = 3 * 5
    elif min > 30 and min <= 40:
        tot = 4 * 5
    elif min > 40 and min <= 50:
        tot = 5 * 5
    elif min > 50 and min <= 60:
        tot = 6 * 5
    elif min > 60 and min <= 70:
        tot = 7 * 5
    elif min > 70 and min <= 80:
        tot = 8 * 5
    elif min > 80 and min <= 90:
        tot = 9 * 5
    elif min > 80 and min <= 100:
        tot = 10 * 5
    else:
        print("Out of reach")
        exit()
if you==2 and the==1:
    if min>0 and min<=10:
        tot=3
    elif min>10 and min<=20:
        tot=2*3
    elif min>20 and min<=30:
        tot=3*3
    elif min>30 and min<=40:
        tot=4*3
    elif min>40 and min<=50:
        tot=5*3
    elif min>50 and min<=60:
        tot=6*3
    elif min>60 and min<=70:
        tot=7*3
    elif min>70 and min<=80:
        tot=8*3
    elif min>80 and min<=90:
        tot=9*3
    elif min>80 and min<=100:
        tot=10*3
    else:
        print("Out of reach")
        exit()
print("You have decided to talk for",str(min) +" minutes")
print("So your bonus amount is Rs",tot)
