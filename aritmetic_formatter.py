
def Verifica():
    #input e variabili utili
    problemi=input("Inserisci qui i problemi da risolvere:\n")
    visualizer= input("Scrivi True per visualizzare la risposta altrimenti scrivi False per uscire:\n")
    x=1
    z=1
    ok="True"
    exit="False"

    #GESTIONE ERRORI
    num_pro= problemi.split(',')  
    if len(num_pro) > 4:                         #Erorr: Too many problems
        print("Erorr: Too many problems!")
        return

    for index in enumerate(problemi):
        operator= problemi.split(' ')

    if "*" in operator:                          #Error: Operator must be '+' or '-'!
        print("Error: Operator must be '+' or '-'!")
        return

    if "/" in operator:                          
        print("Error: Operator must be '+' or '-'!")
        return

    if ' ' not in problemi:                      #Error: You forgot to insert space!
        print("Error: You forgot to insert space!")
        return

    y=len(operator)-2
    try:                                         #Error: Numbers must only contain digits!
        while x<= y:
            verifica= int(operator[x])
            x +=2 
    except ValueError:
        print("Error: Numbers must only contain digits!")
        return

    Y2= len(operator)-2                          #Error: Numbers cannot be more than four digits! 
    while z <= Y2:
        verifica2= len(operator[z])
        z +=2 
        if verifica2 >4:
            print("Error: Numbers cannot be more than four digits!")
            return

    if visualizer == ok:
        aritmethic_formatter(num_pro,operator,)
    
    if visualizer == exit:
        return
              
#Funzione Principale 
def aritmethic_formatter(num_pro,operator,):

    def sol_a_un_probl():
        riga1=f"{oper1} "
        riga2=f"{o}{oper2}"
        riga_lin=f"{lin}"
        risultato=f"{r_1}"

        sol=f"{riga1}\n{riga2}\n{riga_lin}\n{risultato}"
        print(sol)
    
    def sol_a_due_prbl():
        riga1=f"{oper1}    {oper3}   "
        riga2=f"{o}{oper2}    {o1}{oper4}"
        riga_lin=f"{lin}    {lin}"
        risultato=f"{r_1}    {r_2}"

        sol=f"{riga1}\n{riga2}\n{riga_lin}\n{risultato}"
        print(sol)

    def sol_a_tre_prbl():
        riga1=f"{oper1}    {oper3}    {oper5}"
        riga2=f"{o}{oper2}    {o1}{oper4}    {o2}{oper6}"
        riga_lin=f"{lin}    {lin}    {lin}"
        risultato=f"{r_1}    {r_2}    {r_3}"

        sol=f"{riga1}\n{riga2}\n{riga_lin}\n{risultato}"
        print(sol)

    def sol_a_quattro_prbl():
        riga1=f"{oper1}    {oper3}    {oper5}    {oper7}   "
        riga2=f"{o}{oper2}    {o1}{oper4}    {o2}{oper6}    {o3}{oper8}"
        riga_lin=f"{lin}    {lin}    {lin}    {lin}"
        risultato=f"{r_1}    {r_2}    {r_3}    {r_4}"

        sol=f"{riga1}\n{riga2}\n{riga_lin}\n{risultato}"
        print(sol)

    #Soluzione a quattro problemi
    if len(num_pro) == 4:

    #PROBLEMA 1
        oper1= operator[1].rjust(6,' ')
        o= operator[2].ljust(2,' ')
        oper2= operator[3].rjust(4,' ')
        lin= "______"

        if "+" in o:
            ris= int(oper1) + int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')

        if "-" in o:
            ris= int(oper1) - int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')
    
    #PROBLEMA 2 
        oper3= operator[5].rjust(6,' ')
        o1= operator[6].ljust(2,' ')
        oper4= operator[7].rjust(4,' ')
   
        if "+" in o1:
            ris2= int(oper3) + int(oper4)
            r2 = str(ris2)
            r_2=r2.rjust(6,' ')

        if "-" in o1:
            ris2= int(oper3) - int(oper4)
            r2 = str(ris2)
            r_2=r2.rjust(6,' ')

    #PROBLEMA 3
        oper5= operator[9].rjust(6,' ')
        o2= operator[10].ljust(2,' ')
        oper6= operator[11].rjust(4,' ')

        if "+" in o2:
            ris3= int(oper5) + int(oper6)
            r3 = str(ris3)
            r_3=r3.rjust(6,' ')

        if "-" in o2:
            ris3= int(oper5) - int(oper6)
            r3 = str(ris3)
            r_3=r3.rjust(6,' ')

    #PROBLEMA 4
        oper7= operator[13].rjust(6,' ')
        o3= operator[14].ljust(2,' ')
        oper8= operator[15].rjust(4,' ')

        if "+" in o3:
            ris4= int(oper7) + int(oper8)
            r4 = str(ris4)
            r_4=r4.rjust(6,' ')

        if "-" in o3:
            ris4= int(oper7) - int(oper8)
            r4 = str(ris4)
            r_4=r4.rjust(6,' ')

        sol_a_quattro_prbl()

    #Soluzione a tre problemi
    if len(num_pro) == 3:
    
    #PROBLEMA 1
        oper1= operator[1].rjust(6,' ')
        o= operator[2].ljust(2,' ')
        oper2= operator[3].rjust(4,' ')
        lin= "______"

        if "+" in o:
            ris= int(oper1) + int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')

        if "-" in o:
            ris= int(oper1) - int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')
    
    #PROBLEMA 2 
        oper3= operator[5].rjust(6,' ')
        o1= operator[6].ljust(2,' ')
        oper4= operator[7].rjust(4,' ')
   
        if "+" in o1:
            ris2= int(oper3) + int(oper4)
            r2 = str(ris2)
            r_2=r2.rjust(6,' ')

        if "-" in o1:
            ris2= int(oper3) - int(oper4)
            r2 = str(ris2)
            r_2=r2.rjust(6,' ')

    #PROBLEMA 3
        oper5= operator[9].rjust(6,' ')
        o2= operator[10].ljust(2,' ')
        oper6= operator[11].rjust(4,' ')

        if "+" in o2:
            ris3= int(oper5) + int(oper6)
            r3 = str(ris3)
            r_3=r3.rjust(6,' ')

        if "-" in o2:
            ris3= int(oper5) - int(oper6)
            r3 = str(ris3)
            r_3=r3.rjust(6,' ')

        sol_a_tre_prbl()
 
    #Soluzione a due problemi
    if len(num_pro) == 2:
    #PROBLEMA 1
        oper1= operator[1].rjust(6,' ')
        o= operator[2].ljust(2,' ')
        oper2= operator[3].rjust(4,' ')
        lin= "______"

        if "+" in o:
            ris= int(oper1) + int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')

        if "-" in o:
            ris= int(oper1) - int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')
    
    #PROBLEMA 2 
        oper3= operator[5].rjust(6,' ')
        o1= operator[6].ljust(2,' ')
        oper4= operator[7].rjust(4,' ')
   
        if "+" in o1:
            ris2= int(oper3) + int(oper4)
            r2 = str(ris2)
            r_2=r2.rjust(6,' ')

        if "-" in o1:
            ris2= int(oper3) - int(oper4)
            r2 = str(ris2)
            r_2=r2.rjust(6,' ')

        sol_a_due_prbl()

    #Soluzione a un problema
    if len(num_pro) == 1:

        #PROBLEMA 1
        oper1= operator[1].rjust(6,' ')
        o= operator[2].ljust(2,' ')
        oper2= operator[3].rjust(4,' ')
        lin= "______"

        if "+" in o:
            ris= int(oper1) + int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')

        if "-" in o:
            ris= int(oper1) - int(oper2)
            r = str(ris)
            r_1=r.rjust(6,' ')
        
        sol_a_un_probl()

Verifica()


