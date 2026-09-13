
# Criando classe carro.
class Carro:
    def __init__(self):
        self.__nome = None
        self._motor = None
        self._fabricante = None
    
    # Coletando atributos.
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def inserir_detalhes(self, motor, fabricante):
        self._motor = motor
        self._fabricante = fabricante
    
    # Mostrar informações sobre o carro.
    def mostrar(self):
        print(f"Nome: {self.__nome} | Motor: {self._motor.nome} | Fabricante:" +
               f" {self._fabricante.nome}.")

# Criando classe motor.
class Motor:
    def __init__(self):
        self.__nome = None
    
    # Coletando atributos.
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

# Criando classe fabricante.
class Fabricante:
    def __init__(self):
        self.__nome = None
    
    # Coletando atributos.
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

# Criando carros.
motor1 = Motor()
motor1.nome = "b.17"
motor2 = Motor()
motor2.nome = "a.78.3"

fabricante1 = Fabricante()
fabricante1.nome = "Celta"
fabricante2 = Fabricante()
fabricante2.nome = "Uno"

carro1 = Carro()
carro1.nome = "Doguinho"
carro1.inserir_detalhes(motor1, fabricante1)
carro2 = Carro()
carro2.nome = "Amarelado"
carro2.inserir_detalhes(motor2, fabricante2)

# Mostrando carros
print()
carro1.mostrar()
print()
carro2.mostrar()
print()