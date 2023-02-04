import random
import math
import time

#Variables

#leapYear = False
#year = 2000
#month = 1
#date = 1

streak = 0
    
#Date Generation
def genNewDate(difficulty):
    maxDay = 31
    if(difficulty == 1):
        year = 2022
    elif(difficulty == 2):
        year = random.randint(2000,2099)
    else:
        print("DIFFICULTY SET TO:: "+str(difficulty))
    month = random.randint(1,12)
    
    if(month == 2):
        if(year%4==0):
            maxDay = 29
        else:
            maxDay = 28
    elif(month <= 7):
        if(month%2==0):
            maxDay = 30
    elif(month%2==1):
        maxDay = 30
    
    date = random.randint(1,maxDay)
   
    return month, date, year


#Creating week date dictionary

def anchorDay(year):
    c = math.floor(year/100)
    centuryAnchor = ((5*(c%4)+2)%7)
    yearOfCentury = year%100
    return (yearOfCentury+math.floor(yearOfCentury/4)+centuryAnchor)%7
    
def findDayOfTheWeek(param):
    #Declaring doomsdates
    doomsdates={3:0,4:4,5:9,6:6,7:11,8:8,9:5,10:10,11:7,12:12}
    if(param['year']%4==0):
        leapYear = True
    else:
        leapYear = False
    if(leapYear):
        doomsdates[1] = 4
        doomsdates[2] = 1
    else:
        doomsdates[1] = 3
        doomsdates[2] = 0

    anchorDate = anchorDay(param['year'])
    return (param['day']-doomsdates[param['month']]+anchorDate)%7
    
#while(True):
#    month, date, year, leapYear = genNewDate()
#    print("Current score: "+str(score)+"     Streak: "+str(streak))
#    print(scoreLine)
#    print("")
#    print(" "+str(month)+" / "+str(date)+" / "+str(year))
#    time.sleep(5)
#    print("\n"*30)
#    guessedDate = input("Day of the week: ")
#    correctDate = findDayOfTheWeek();
    
#    if(guessedDate.lower() == weekdays[correctDate]):
#        print("Correct")
#        scoreLine+="0"
#        score+= 10 + streak
#        streak +=1
#    else:
#        print("Incorrect")
#        print("Answer was "+weekdays[correctDate]);
#        scoreLine+="~"
#        streak = 0
#        score -= 3
#    print("\n\n==================================================")
#    time.sleep(3)