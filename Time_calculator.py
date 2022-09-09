t=input("Inserisci un'orario di inizio formato 12H, le ore da aggiungere e facoltativamente un giorno della settimana:\n")

for index in enumerate(t):
    time=t.split(' ')

def add_time(time):
    #variabili e dict
    week={"Monday": 1 , "Tuesday": 2 , "Wednesday" : 3 , "Thursday" : 4 , "Friday" : 5 , "Saturday" : 6 , "Sunday" : 7}
    days=0
    eccesso=0

    #somma orario
    ore= int(time[1])+int(time[6])
    min= int(time[3])+int(time[8])

    while ore >= 24:                #ciclo ore 
        ore= int(ore)-24            
        days +=1
        if ore == 0:
            ore = "00"
            break
        if ore < 24 and ore != 0:
            break

    giorni= f"({days} days later)"

    while min >= 60:               #ciclo min 
        min = int(min)-60   
        eccesso +=1
        if min == 0:
            min = "00"
            break
        if min < 60 and min != 0:
            break

    Ore= int(ore)+int(eccesso)    
    if Ore > 12 :
        AM_or_PM= "PM"  
    if Ore <= 12:
        AM_or_PM= "AM"

    if time[10] in week and days >= 1:        #giorno settimana 
        giorno=week.get(f'{time[10]}')
        val= int(giorno)+int(days)

        for key , value in week.items():
            if val == value:
                giorno_week= key 

        ris= f"{Ore}{time[2]}{min} {AM_or_PM} {giorno_week} {giorni}"
    else:
        ris= f"{Ore}{time[2]}{min} {AM_or_PM} {giorni}"
     
    print(ris)

add_time(time)
