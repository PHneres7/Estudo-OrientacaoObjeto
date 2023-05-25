fatura=[]
class Fatura():
    def __init__(self, num, nome, quant=0, valor=0):
        self.__numero=num
        self.__nome=nome
        self.__quantidade=quant
        self.__valor=valor
        fatura.append(list((self.__numero, self.__nome, self.__quantidade, self.__valor)))
        
    def get_numero(self):
        return self.__numero
    
    def get_nome(self):
        return self.__nome

    def get_quantidade(self):
        return self.__quantidade
    
    def get_valor(self):
        return self.__valor
    
    def get_Total(self):
        return self.__quantidade*self.__valor
    
    def get_FaturaTotal(self):
        cont=0
        for i in fatura:
            s=i[-1]*i[2]
            cont+=s
        return cont  
    
    def set_numero(self, num):
        self.__numero=num
    
    def set_nome(self, nome):
        self.__nome=nome
    
    def set_quantidade(self, quant):
        if quant<0:
            quant=0
        self.__quantidade=quant
    
    def set_valor(self, valor):
        if valor<0:
            valor=0
        self.__valor=valor
    
def mostrarSet(fat):
    print('============MUDANDO=================')
    opc=int(input("Numero do Produto a ser mudado: "))
    for i in fatura:
        if opc==i[0]:
            fatura.remove(i[:])
            fat.set_numero(int(input("numero novo: ")))
            fat.set_nome(input("Nome novo: "))
            fat.set_quantidade(int(input("Quantidade nova: ")))
            fat.set_valor(float(input("Valor novo: ")))
            fatura.append(list((fat.get_numero(), fat.get_nome(),fat.get_quantidade(),fat.get_valor())))

    mostrar(fat)


def mostrar(fat):
    print("===============================")
    print(f'numero.....: {fat.get_numero()}')    
    print(f'nome.......: {fat.get_nome()}')
    print(f'quantidade.: {fat.get_quantidade()}')
    print(f'valor......: {fat.get_valor()}')
    print("==========Fatura Item===========")
    print(f"Valor......: {fat.get_Total()}")
    print("==========Fatura Total==========")
    print(f'Valor......: {fat.get_FaturaTotal()}')
    print(fatura)

while True:
    try:
        num=int(input("numero: "))
        nome=str(input("Nome do Produto: "))
        quant=int(input("Quantidade:"))
        if quant<0:
            quant=0
        valor=float(input("Valor unitário: "))
        if valor <0:
            valor=0
        fat=Fatura(num, nome, quant, valor)
        mostrar(fat)

        op=(input("Digite '#' para mudar Dados: "))
        if op == '#':
            mostrarSet(fat)
        else: 
            continue
    except:
        print("Ocorreu um erro")
    