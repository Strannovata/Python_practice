#22.Найти расстояние между точками в пространстве 2D

def GetLenght2D (x1, y1, x2, y2):
    l = (((x1-x2)**2)+((y1-y2)**2))**0.5
    return l

print(GetLenght2D(1,1,-1,1))

