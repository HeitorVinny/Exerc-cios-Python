
cont = 1

while cont <= 4:
    codigoPedido = int(input("Digite o código do pedido: "))
    qtdPedido = int(input("Quantidade: "))
    if codigoPedido == 100:
        valorPedido = qtdPedido * 5.20
        print("Pedido: Cachorro quente")
        print("Quantidade: {}".format(qtdPedido))
        print("Preço: {:.2f}".format(valorPedido)) 
    elif codigoPedido == 101:
        valorPedido = qtdPedido * 5.20
        print("Pedido: Hambúrger")
        print("Quantidade: {}".format(qtdPedido))
        print("Preço: {:.2f}".format(valorPedido))
    elif codigoPedido == 102:
        valorPedido = qtdPedido * 7.30
        print("Pedido: Cheeseburguer")
        print("Quantidade: {}".format(qtdPedido))
        print("Preço: {:.2f}".format(valorPedido))
    elif codigoPedido == 103:
        valorPedido = qtdPedido * 5.00
        print("Pedido: Refrigerante")
        print("Quantidade: {}".format(qtdPedido))
        print("Preço: {:.2f}".format(valorPedido))
    else:
        print("Código não existente")