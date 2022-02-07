# 58. Напишите программу, удаляющую из текста все слова содержащие "абв".



from gettext import find


def deleteWords(text, found):
    list = text.split(' ')
    result = []
    for i in range(0, len(list)):
        if not found in list[i]:
            result.append(list[i])
    restext = ' '.join(result)
    return restext

                    

txt = 'Ах абвтельный в России абвера'
ftext = 'абв'
newtxt = deleteWords(txt, ftext)
print(newtxt)
