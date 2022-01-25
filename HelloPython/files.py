# Файлы.
# a - открыть файл для дозаписи
# w - перезапись
# r - чтение

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# #data.writelines(colors) 
# data.write('LINE1211\n') 
# data.write('LINE2222\n') 
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()