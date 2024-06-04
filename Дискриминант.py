from math import sqrt

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3nd number: '))
def discriminant (a,b,c):
    """Функция для дискриминанта"""
    return b**2 - 4 * a * c
print (f'd={discriminant (a,b,c)}')

def solve (a,b,c):
    """Функция, которая вычисляет корни квадратное уравнения"""
d = discriminant(a,b,c) 
if d > 0:
    x1 = (-b - sqrt(d))/(2*a)
    x2 = (-b + sqrt(d))/(2*a)
    print (f'Два кореня, x1= {x1}, x2= {x2}')
elif d == 0:
    x = -b/(2*a)
    print (f'Один корень, x= {x}')
else:
    print ('Корней нет')