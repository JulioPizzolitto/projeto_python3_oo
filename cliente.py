class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #definindo o getter
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    #definindo o setter
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
