'''

 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def area_triangulo(Poligono):
    lado, base = Poligono
    altura= (lado**2) + ((base/2)**2)
    altura= altura**0.5
    return round((base*altura)/2,5)


def area_rectangulo(Poligono):
    r1, r2 = Poligono
    return r1*r2

def area_cuadrado(Poligono):
    return Poligono*Poligono


triangulo=(5,6)
rectangulo=(5,6)
cuadrado = 4

print(area_triangulo(triangulo))
print(area_rectangulo(rectangulo))
print(area_cuadrado(cuadrado))