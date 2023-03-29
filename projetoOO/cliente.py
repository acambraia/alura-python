class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property          #define o metodo como propriedade
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter       #define o metodo como setter para receber valores como um atributo
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome