class Herramientas:
    def __init__(self, lista_numeros):
        if type(lista_numeros) != list:
            self.lista = []
            raise ValueError("Se ha creado una lista vacía. Se esperaba una lista con numeros enteros")
        else:    
            self.lista = lista_numeros
    def es_numero_primo(self):
        for i in self.lista:
            if (self.__es_numero_primo(i)):
                print(f"el elemento {i} SI es número primo")
            else:
                print(f"el elemento {i} NO es número primo")

    def conversion_grados(self, origen, destino):
        parametros_esperados = ["celsius", "farenheit", "kelvin"]
        lista_conversion =[]
        if str(origen) not in parametros_esperados:
            print(f"los parametros esperados de origen son {parametros_esperados}")
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print(f"los parametros esperados de destino son {parametros_esperados}")
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversion_grados(i, origen, destino))
        return lista_conversion
    
    def factorial(self):
        for i in self.lista:
            print("el factorial de ", i, "es " , self.__factorial(i))
        

    def __es_numero_primo(self, num):
        primo = True
        for i in range(2, num):
            if (num % i == 0):
                primo = False
                break
        return primo

    def valor_modal(self, lista, modo = "menor"):
        contador = {}
        for num in self.lista:
            if num in contador.keys():
                contador[num] += 1
            else:
                contador[num] = 1
        maximo_repeticion = 0
        mas_repetido = []

        for numero, repeticion in contador.items():
            if repeticion > maximo_repeticion:
                maximo_repeticion = repeticion
                mas_repetido = [numero]
            elif repeticion == maximo_repeticion:
                mas_repetido.append(numero)
        if modo == "menor":
            mas_repetido_num = min(mas_repetido)
        elif modo == "mayor":
            mas_repetido_num = max(mas_repetido)
        return mas_repetido_num, maximo_repeticion
                                
    def __conversion_grados(self, valor, origen, destino):
        if origen == "celsius":
            if destino == "celsius":
                valor_destino = valor
            elif destino == "farenheit":
                valor_destino = (valor * 9 /5) + 32
            elif destino == "kelvin":
                valor_destino = valor * 273.15
            else:
                print("Parámetro de destino incorrecto")
        elif origen == "farenheit":
            if destino == "celsius":
                valor_destino = (valor - 32) * 5 / 9
            elif destino == "farenheit":
                valor_destino = valor
            elif destino == "kelvin":
                valor_destino = ((valor - 32) * 5 / 9) +273.15
            else:
                print("Parámetro de destino incorrecto")
        elif origen == "kelvin":
            if destino == "celsius":
                valor_destino = valor - 273.15
            elif destino == "farenheit":
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif destino == "kelvin":
                valor_destino = valor
            else:
                print("Parámetro de Destino incorrecto")
        else:
            print("Parámetro de Origen incorrecto")  
                
        return valor_destino

    def __factorial(self, num):
        if type(num) != int or num < 0:
            return None
        if num <= 1:
            return 1
        num = num * self.__factorial(num -1)
        return num
