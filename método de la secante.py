def func(x:int):
    return x**3 - x -2

def calcular_iteracion(x0,x1):
    return x1 - func(x1)*(x1 - x0)/(func(x1) - func(x0))

def metodo_secante(x0, x1):
    MAX_ITER = 100
    TOL = 1e-10

    i = 0