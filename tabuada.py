num = int(input("informe seu numero "))
for i in range(1 + num):
    print(f'{i} X {num} = {i*num}')
if num <= 0:
    print("opçao invalida")
