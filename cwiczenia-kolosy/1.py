import random
import statistics

class klasa:
    def __init__(self):
        lista = []
        for i in range(500):
            lista.append(random.randint(0, 100))
        self.lista = lista
    def printLista(self):
        print(self.lista)
    def minimalny(self):
        sortedList = sorted(self.lista)
        return sortedList[0]
    def maksymalny(self):
        sortedList = sorted(self.lista)
        return sortedList[-1]
    def sumuje(self):
        sum = 0
        for item in self.lista:
            sum += item
        return sum
    def odchyl(self):
        return statistics.stdev(self.lista)
    def msu(self):
        return statistics.mode(self.lista)
    def mdu(self):
        return statistics.median(self.lista)
    def zapisuje(self):
        file = open(f'{self.lista[0]}', 'w')
        file.write(str(self.lista)+'\n')
        file.write(str(self.minimalny())+'\n')
        file.write(str(self.maksymalny())+'\n')
        file.write(str(self.sumuje())+'\n')
        file.write(str(self.odchyl())+'\n')
        file.write(str(self.msu())+'\n')
        file.write(str(self.mdu())+'\n')
        file.close()

myClass = klasa()
print(myClass.minimalny())
print(myClass.maksymalny())
print(myClass.sumuje())
print(myClass.odchyl())
print(myClass.msu())
print(myClass.mdu())
myClass.zapisuje()