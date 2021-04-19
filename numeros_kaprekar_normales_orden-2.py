import math

def divisores(n):
    resultado = []	
    for i in range(1, int(math.sqrt(n) + 1)):		
        if (n % i == 0):			
            if (n / i == i):
                resultado.append(i)
            else:
                resultado.append(i)
                resultado.append(int(n / i))
    return resultado;
		
def mcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def divisoresUnitarios(n, divisores):
    resultado = []
    for divisor in divisores:
        if mcd(n//divisor, divisor) == 1:
            resultado.append(divisor)
    return resultado

def inv(a, b, respuesta_minima):
    minimo = respuesta_minima // a
    resultado = 1
    for i in range(minimo, b + 1):
        am = a * i
        if (am - 1) % b == 0:
            resultado = am
            break
    return resultado

def numerosKaprekar(minimo_kapre, longitud):
    n = (10**longitud) - 1
    divs = divisores(n)
    divs_unitarios = divisoresUnitarios(n, divs)
    divs_unitarios.sort()
    kaprekars =  []
    cant_div_uns = len(divs_unitarios)
    for i in range(cant_div_uns // 2):
        n_kapre = inv(divs_unitarios[i], divs_unitarios[cant_div_uns - i - 1], minimo_kapre)
        kaprekars.append(n_kapre)
        #kaprekars.append(inv(divs_unitarios[cant_div_uns - i - 1], divs_unitarios[i], minimo_kapre))
        kaprekars.append(n + 1 - n_kapre)
    return kaprekars

def kaprekarsCuadradoEnRango(minimo, maximo):
    resultado = []
    minimo_kapre = math.ceil(math.sqrt(minimo))
    maximo_kapre = math.floor(math.sqrt(maximo))
    lista_kaprekar = numerosKaprekar(minimo_kapre, len(str(minimo))//2)
    for kaprekar in lista_kaprekar:
        if kaprekar >= minimo_kapre and kaprekar <= maximo_kapre:
            resultado.append(kaprekar)
    return resultado

#print(inv(11, 9, 36))
#print(numerosKaprekar(316227767, 9))
print(kaprekarsCuadradoEnRango(1000, 9999))

##%time numerosKaprekar(316227767, 9)
##Wall time: 1min 40s
# [1,
#  999999999,
#  567567568,
#  432432432,
#  765432099,
#  234567901,
#  332999667,
#  667000333]
