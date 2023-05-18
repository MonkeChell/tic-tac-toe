

a = 3
mas = ['-'] * a
for i in range(a):
    mas[i] = ['-'] * a

def lol_l(mas):
    for i in range(a):
        for j in range(a):
            print(mas[i][j], end="")
        print()

lol_l(mas)
lol_l(mas)
def move(mas,c):
    z, x = input().split()
    z = int(z)
    x = int(x)
    mas[z][x] = c
    lol_l(mas)

move(mas,"0")
move(mas,"x")
move(mas,"0")
move(mas,"x")
move(mas,"0")
move(mas,"x")
