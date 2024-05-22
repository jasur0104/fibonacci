from  typing import Optional
class Fibonacci:
    def __init__(self,son):
        self.son=son
    def __iter__(self):
        return self
    def __next__(self):
        i=0
        a=0
        b=1
        sonlar=[]
        while i<self.son:
            son=a+b
            sonlar.append(son)
            a=b
            b=son
            i+=1
        return sonlar
son1=int(input("nechta fibonacci soninin chiqarsin:"))
print(next(object))
#bu bizga nechta fibonacci sonini chiqarsin desak chiqarib beradi






