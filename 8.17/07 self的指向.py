class A:
    def f0(self):
        print('A.f0')
    def f1(self):
        print('A.f1')
        self.f0()
class B:
    def f1(self):
        print('B.f1')
        self.f0()
    def f4(self):
        print('B.f4')
class C(A,B):
    def f0(self):
        print('C.f0')
    def f3(self):
        print('C.f3')
        self.f1()
    def f4(self):
        print('C.f4')
c = C()
c.f3()
# b = B()
# b.f0()
# b.f1()