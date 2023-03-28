class Conta:

    def __init__(self, numero, titular, saldo = 0, limite = 1000): #Criação do construtor
        print("Construindo objeto... {}".format(self))
        self.__numero = numero    #dois underline (__) antes do nome do atributo define como 'private'
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigoBanco = "001"

    def mostrarSaldo(self):
        print("Saldo {} do titular {}.".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def valorDisponivel(self):
        return self.__limite+self.__saldo
    def __podeSacar(self, valorSaque):     # O metodo também pode ser privado, utilizando '__'
        return (valorSaque <= self.valorDisponivel())


    def sacar(self, valor):
        if(self.__podeSacar()):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo


    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod           #propriedade de metodo estatico
    def codigoBanco():      #Metodo estático.
        return "001"

    @staticmethod  # propriedade de metodo estatico
    def codigosBancos():  # Metodo estático.
        return {'BB': '001', 'CEF': '104', 'Bradesco': '237'}










