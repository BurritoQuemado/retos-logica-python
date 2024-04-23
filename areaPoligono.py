def calcularArea(**params):
    if len(params) == 3 and params["triangle"] is not None:
        return (params["base"] * params["height"]) / 2
    elif len(params) == 2:
        return params["base"] * params["height"]
    else:
        return params["base"]**2
    

print("Area de un Triangulo " + str(calcularArea(triangle=True,base=3,height=4)))
print("Area de un Rectangulo " + str(calcularArea(base=12,height=10)))
print("Area de un Cuadrado " + str(calcularArea(base=4)))
    
