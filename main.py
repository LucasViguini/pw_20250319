from produto import Produto

#Tratamento de erro
try:
    p1 = Produto(1, "Cadeira", 100.0, 5)
    p2 = Produto(2, "Mesa", 200.0, 10)
    p3 = Produto(3, "Armário", 300.0, 15)
    p4 = Produto(4, "Cama", 400.0, 20)
    p5 = Produto(5, "Sofá", 500.0, 25)
    p6 = Produto(6, "Guarda-roupa", 600.0, 30)
    p7 = Produto(7, "Estante", 700.0, 35)
    p8 = Produto(8, "Rack", 800.0, 40)
    p9 = Produto(9, "Poltrona", 900.0, 45)
    p10 = Produto(10, "Mesa de centro", 1000.0, 50)


    # print(f'Produto criado com sucesso: {p1.get_nome()}')
    # p1.set_nome("Camiseta regata")
    # print(p1.get_nome())

except ValueError as e:
    print(e)
except Exception as e:
    print('Erro desconhecido')

produtos = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
Produto.mostrar_titulos()
for produto in produtos:
    produto.mostrar_dados()