#Sammulugeja
goal = 10000
steps = int(input("Mitu sammu oled juba läbinud?: "))
precent = (steps/goal) * 100
if precent < 50: 
    print("Alles poolel teel, liigu edasi!")
elif precent < 75:
    print("Oled peaaegu kohal!")
elif precent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")