import random
import time

ask = input("Entrez différents caractères à tester : \n")
Liste = []
List = list(ask) #["1","2","3","4","5","6","7"]
Nbr = 0
Multi = 1

for i in range(len(List)):
    Nbr += 1
    Multi = Nbr * Multi
print(f"Pour {Nbr} caractères uniques, on a {Multi} possibilités.")

while len(Liste) != Multi :
    List = list(ask)
    random.shuffle(List)
    if List not in Liste :
        print(List)
        Liste.append(List)
    else :
        continue
print(f"La liste mesure donc {len(Liste)} avec {Liste}")


