# 53. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

def PolinominalInDegree (k):
    listarg = []
    listpol = []
    for i in range(0, k+1):
        i = randint(0, 101)
        listarg.append(i)
    print(listarg)
    for i in listarg:
        if i != 0:
            if k > 1:
                polinom = f'{i}x**{k}'
            elif k > 0:
                polinom = f'{i}x'
            else:
                polinom = f'{i}'
            listpol.append(polinom)
            strresult = " + ".join(listpol)
        k-=1
    data = open('PoliminalInDegree2.txt', 'w')
    data.write(f'{strresult} = 0\n')
    data.close()

PolinominalInDegree(2)

