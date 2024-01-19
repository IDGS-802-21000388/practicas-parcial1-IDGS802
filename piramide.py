class Piramide:
    totalValores = 0

    def __init__(self, totalValores) -> None:
        self.totalValores = totalValores

    def piramide(self):
        for n in range(1,self.totalValores+1):
            cadena = ''
            for tt in range(1,n+1):
                cadena+='*'
            print(cadena)

    
    def main():  
        totalValores = int(input("Dame el valor para hacer la piramide: "))
        obj = Piramide(totalValores)
        obj.piramide()

if __name__ == "__main__":
    Piramide.main()