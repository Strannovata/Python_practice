#18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def CheckFunc(x, y):
    return (not(x or y)) == ((not x) and (not y))

print(CheckFunc(True, True))
print(CheckFunc(True, False))
print(CheckFunc(False, True))
print(CheckFunc(False, False))