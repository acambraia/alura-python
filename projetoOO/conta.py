class Conta:

    def __init__(self, numero, titular, saldo = 0, limite = 1000): #Criação do construtor
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def mostrarSaldo(self):
        print("Saldo {} do titular {}.".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor




