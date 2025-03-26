while True:
    print("zadejte 2 čísla")
    a = int(input("Číslo 1"))
    b = int(input("Číslo 2"))
    operace = input("Chcete sčítání, odčítání, násobení nebo dělení")
    if operace == "sčítání":
        print("Výsledek je:")
        print(a+b)
    elif operace == "odćítání":
        print("Výsledek je:")
        print(a-b)
    elif operace == "násobení":
        print("Výsledek je:")
        print(a*b)
    elif operace == "dělení":
        print("Výsledek je:")
        print(a/b)
    opak = input("Chcete počítat znova? ano/ne")
    if opak== "ne":
        break
    

