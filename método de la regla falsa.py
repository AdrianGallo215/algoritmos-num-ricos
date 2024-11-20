import numpy

def func(x:int):
    return x*x*x - x - 2

def calcular_c(a,b):
    return a - func(a)*((b-a)/(func(b)-func(a)))

def regla_falsa(a,b):
    MAX_ITER = 100
    TOL = 1e-5
    i = 0
    while(i<MAX_ITER and abs(b-a) >=TOL ):
        c = calcular_c(a,b)
        i+=1
        if func(c) == 0:
            a = b = c
        elif func(a)*func(c) < 0:
            b = c
        else:
            a = c

        print(f'[a, b] = [{a:5.2f}, {b:5.2f}]')
    if abs(b-a)>= TOL:
        print('Método no converge')
    else:
        print(f'Solución c={c}')
        print(f'Número de iteraciones={i}')

regla_falsa(1,2)
