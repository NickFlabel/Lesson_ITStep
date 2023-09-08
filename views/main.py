class A:

    def operation(self):
        print('A')


class B(A):

    def operation(self):
        print('B')


class C(A):

    def operation(self):
        print('C')

class E:

    def operation(self):
        print('E')


class D(B, C, E):

    def alt_operation(self):
        self.operation()
        super(A, self).operation()


d = D()
d.alt_operation()
print(D.__mro__)