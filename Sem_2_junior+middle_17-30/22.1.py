# 22.1. Найти расстояние между точками в пространстве 3D

def GetLenght3D (x1, y1, z1, x2, y2, z2):
    l = (((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))**0.5
    return l

print(GetLenght3D(1,1,1,-1,1,1))