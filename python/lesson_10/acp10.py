class maths:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def solve(self,sign):
        if(sign=='+'):
            print(self.num1+ self.num2)
        elif(sign=='-'):
            print(self.num1 - self.num2)
        elif(sign=='/'):
            print(self.num1 / self.num2)
        elif(sign=='*'):
            print(self.num1 *self.num2)

a = maths(5,5)
a.solve('*')