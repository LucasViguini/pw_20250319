from util import string_contem_somente_numeros


class Produto:
    def __init__(self, id, nome, preco, quantidade):
        #Verifica se os parâmetros são válidos
        # if not isinstance(id, int) or id <= 0:
        #     raise ValueError('ID deve ser um inteiro positivo')
        # if not isinstance(nome, str) or len(nome) < 2 or string_contem_somente_numeros(nome):
        #     raise ValueError('Nome deve ser uma string com 2 ou mais caracteres e não pode conter somente números')
        # if not isinstance(preco, (int, float)) or preco <= 0:
        #     raise ValueError('Preço deve ser um número positivo')
        # if not isinstance(quantidade, int) or quantidade <= 0:
        #     raise ValueError('Quantidade deve ser um inteiro positivo')
        
        #Atributos encapsulados
        #Chamando a propria função set, para evitar a redundância acima
        self.set_id(id)
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_quantidade(quantidade)

    #Método de leitura
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade
    
    #Método de escrita
    def set_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError('ID deve ser um inteiro positivo')
        self.__id = id

    def set_nome(self, nome):     
        if not isinstance(nome, str) or len(nome) < 2 or string_contem_somente_numeros(nome):
            raise ValueError('Nome deve ser uma string com 2 ou mais caracteres e não pode conter somente números')
        self.__nome = nome

    def set_preco(self, preco):
        if not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError('Preço deve ser um número positivo')
        self.__preco = preco

    def set_quantidade(self, quantidade):
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError('Quantidade deve ser um inteiro positivo')
        self.__quantidade = quantidade

    #Método de exibição
    def mostrar_dados(self):
        print(f'{self.__id:06d} {self.__nome:15} {self.__preco:>10.2f} {self.__quantidade:>10d}')

    #Método de classe
    @classmethod
    def mostrar_titulos(cls):
        print(f'Código {"Produto":15} {"Preço":>10} {"Estoque":>10}')
    


    
