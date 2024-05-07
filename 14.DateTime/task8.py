def circuit_power (num1, num2):
    result=num1*num2
    return f'Cirkuit power ({num1},{num2}) ---> ({result})'

while True:
    a=int(input())
    b=int(input())
    print(circuit_power(a,b))