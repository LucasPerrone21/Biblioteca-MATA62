def funcao(x,y,z):
    print(type(x))
    print(type(y))
    print(type(z))



x = input("Digite 3 valores: ").split()

funcao(*x)

print(" ")

for i in range(len(x)):
    try:
        x[i] = int(x[i])
    except:
        pass

funcao(*x)

