#Inheritance
class A:
    def method1(self):
        print("Method 1")
    def method2(self):
        print("Method 2")                


class B(A):
    def method3(self):
        print("Method 3")
    def method4(self):
        print("Method 4")  

class C(A, B):
    def method5():
        print("Method 5")         

a = A()
b = B()
c = C()   

c.method1()
c.method2()