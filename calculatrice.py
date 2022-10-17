A=float(input("donner la première valeur : "))
op=input("donner l'operateur ; ")
B=float(input("donner la deuxiee valeur : "))

if op=="*":
    print(A*B)
elif op=="+":
    print(A+B)
elif op == "-":
    print(A - B)
elif op == "/":
    if B!=0:
        print(A / B)
    else:
        print ("erreur")
else:
    print("donner l'operateur adequat")