class Pilha:

    def __init__(self, limite_pilha):
        self.__pilha = []
        self.__limite_pilha = limite_pilha

    def push(self, valor):
        if self.pilhaCheia():
            raise Exception

        self.__pilha.append(valor)

    def pop(self):
        if self.pilhaVazia():
            raise Exception

        self.__pilha.pop()

    def mostrar(self):
        print(self.__pilha)

    def top(self):
        position = len(self.__pilha - 1)
        return self.__pilha[position]

    def pilhaCheia(self):
        if len(self.__pilha) >= self.__limite_pilha:
            return True
        return False

    def pilhaVazia(self):
        if len(self.__pilha) == 0:
            return True
        return False

    def numElemts(self):
        return len(self.__pilha)


pilha = Pilha(4)
# pilha.push("a")
# pilha.push("b")
# pilha.push("c")
# pilha.push("oi")
# pilha.push("o")
pilha.pop()
pilha.mostrar()