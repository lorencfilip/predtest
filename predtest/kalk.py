funkce1 = True
while funkce1 == True:
    print("Vítej v kalkulačce")
    print("Zvol co chceš počítat: 1 pro rychlost, 2 pro čas, 3 pro dráhu, 4 pro konec:")

    výběr = int(input("váš výběr:"))

    if výběr == 1 :

        print("Vybral jsi si výpočet rychlosti(počítej tak aby výsledek byl v kilometrech za hodinu)")

        s = int(input("zadej proměnou s: "))
        t = int(input("zadej proměnou t: "))

        if s>0 and t>0:
            v = s/t
            a = print("rychlost je: ", v)
        else:
            print("zkus to znovu")

    elif výběr == 2 :

        print("Vybral jsi si výpočet času")
         
        v = int(input("zadej promněnou v: "))
        s = int(input("zadej promněnou s: "))

        if s>0 and v>0:
            t = s/v
            a = print("čas je: ", t)
        else:
            print("zkus to znovu")

    elif výběr == 3 :

        print("Vybral jsi si výpočet dráhy")
         
        v = int(input("zadej promněnou v: "))
        t = int(input("zadej promněnou t: "))

        if t>0 and v>0:
            s = v*t
            a = print("dráha je: ", s)
        else:
            print("zkus to znovu")
    elif výběr == 4 :
        
        print("Rozhodl jsi se skončit.")
        break
