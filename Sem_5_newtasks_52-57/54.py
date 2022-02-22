# 54. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

path = 'PoliminalInDegree.txt'
data = open(path, 'r')
for line in data:
    string1 = line
data.close()

path = 'PoliminalInDegree2.txt'
data = open(path, 'r')
for line in data:
    string2 = line
data.close()

print(string1)
print(string2)

list1 = string1.split()
list2 = string2.split()

args1 = []
for i in list1:
    num1 = str(i).split('*')
    args1.append(num1[0])

args2 = []
for i in list2:
    num2 = str(i).split('*')
    args2.append(num2[0])

listargs1 = []
for i in range(0, len(args1), 2):
    arg1 = int(args1[i])
    listargs1.append(arg1)

    
listargs2 = []
for i in range(0, len(args2), 2):
    arg2 = int(args2[i])
    listargs2.append(arg2)


listres = []
for i in range(0, len(listargs1)):
    sum = listargs1[i] + listargs2[i]
    listres.append(sum)


data = open('PoliminalInDegreesum.txt', 'w')
data.write(f'{listres[0]}x**2 + {listres[1]}x + {listres[2]} = {listres[3]}\n')
data.close()

