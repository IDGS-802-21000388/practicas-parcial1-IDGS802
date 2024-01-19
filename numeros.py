class Numeros:
    totalValores = 0
    lst = []

    def __init__(self, lst) -> None:
        self.lst = lst

    def ordenar(self):
        self.lst.sort()
        print("La lista de los valores ordenados son: ", self.lst)

    def duplicados(self):
        self.lst.sort()
        unicos = []
        duplicados = []

        for n in self.lst:
            if n in unicos and n not in duplicados:
                duplicados.append(n)
            else:
                unicos.append(n)
        print("La lista de los valores duplicados son: ", duplicados)

    def pares(self):
        self.lst.sort()

        lstPares = []
        for i in range(len(self.lst)):
            if self.lst[i] % 2 == 0 and self.lst[i] not in lstPares:
                lstPares.append(self.lst[i])
        print("La lista de los valores pares son: ",lstPares)
    
    def impares(self):
        self.lst.sort()

        lstImpares = []
        for i in range(len(self.lst)):
            if self.lst[i] % 2 != 0 and self.lst[i] not in lstImpares:
                lstImpares.append(self.lst[i])
        print("La lista de los valores impares son: ",lstImpares)
        
    
    def main():  
        totalValores = int(input("Dame cuantos valores vas a ingresar: "))
        lstValores = []
        for i in range(totalValores):
            num = int(input("Dame un número: "))
            lstValores.append(num)

        obj = Numeros(lstValores)
        #obj.ordenar()
        #obj.pares()
        #obj.impares()
        obj.duplicados()

if __name__ == "__main__":
    Numeros.main()
    