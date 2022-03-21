class op:
    def a(self):
        print('apple')
    def b(self):
        print('bat')
    def c(self):
        print('cat')
    def d(self):
        print('dog')

x=op()
for i in range(6):
    x.a()
    x.b()
    x.c()
    x.d()