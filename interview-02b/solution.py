class Node:
    # O enunciado apresenta mas diz que não é para colocar uma classe Node. Contudo, o pytest rodando localmente não reconhece o Node se não for declarado. Portanto, coloco aqui exatamente como apresentado no enunciado para que o teste rode.

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def nth_to_last(head: Node, k: int) -> Node:
    #Etapa 1: iterar pela lista ligada inteira para descobrir seu tamanho.
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    #Agora sabemos o tamanho da lista.

    #Verificação de caso de contorno.
    if k > length:
        return None
    
    #Cálculo do índice do último elemento.
    index = length - k 

    #Agora rodamos a lista ligada novamente até chegar ao elemento desejado.
    current = head
    for i in range(index):
        current = current.next
    
    return current
    