A=float(input("donner la première valeur : "))
B=float(input("donner la deuxiee valeur : "))
C=float(input("donner la première valeur : "))


if A<B and A<C:
    print ("LA VALEUR MINIMALE EST :", A)

elif B<A and B<C:
    print ("LA VALEUR MINIMALE EST :", B)

else:
    print ("LA VALEUR MINIMALE EST :", C)