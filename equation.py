# We search :
# 3*x + 5*y = 31
# 7*x + 9*y = 59

def calcul(nbr1, nbr2, nbr3):
  for i in range(0,10) :
    for j in range(0,10) :
      result = (nbr1*i + nbr2*j)
      if result == nbr3 :
        return result, i, j

result = calcul(7, 9, 59) 
print("For the first equation ""7*x + 9*y = 59"" answer is : " + str(result[0]) + " with x == " + str(result[1]) + " and y == " + str(result[2]))
result2 = calcul(3, 5, 31)
print("For the second equation ""3*x + 5*y = 31"" answer is : " + str(result2[0]) + " with x == " + str(result2[1]) + " and y == " + str(result2[2]))

