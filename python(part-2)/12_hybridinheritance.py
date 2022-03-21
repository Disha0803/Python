class a:
    def fun_a(self):
        print("a")
class b:
    def fun_b(self):
        print("b")
class c:
    def fun_c(self):
        print("c")
class d(a,b,c):
    def fun_d(self):
        print("d")
class e(d):
    pass
class f(d):
    def fun_f(self):
        print("f")
class g(f,e):
    def fun_g(self):
        print("g")
obj=g()
obj.fun_a()
obj.fun_c()

obj2=d()
obj2.fun_c