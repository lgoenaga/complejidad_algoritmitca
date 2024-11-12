def morral(tamano_morral, pesos, valores, indice):
    if indice == 0 or tamano_morral == 0:
        return 0

    if pesos[indice - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, indice - 1)
   
    return  max(
        valores[indice - 1]
        + morral(tamano_morral - pesos[indice - 1], pesos, valores, indice - 1),
        morral(tamano_morral, pesos, valores, indice - 1),
    )


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)
    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
