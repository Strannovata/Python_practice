#29. Написать программу вычисления произведения чисел от 1 до N

def Factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
        i += 1
    return result

N = 15
print(Factorial(N))