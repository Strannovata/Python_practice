# 41. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

lst = ['a18', '7ud', '567', '8hf', '865', 'u8h']
num = '8h'

def foundNumPosition(list, found):
    
    temp = 0
    for i in range(0, len(list)):
        str = list[i]
        count = 0
        for j in str:
            for k in found:
                if k == j:
                    count += 1
                    if count == len(found):
                        temp +=1
                        if temp == 2:
                            return i
       

pos = foundNumPosition(lst, num)

if pos == None:
    print(f'Второго вхождения нет')
else:
    print(f'Второе вхождение строки {num} на {pos} позиции ')
    