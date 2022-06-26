import inspect


def  whoami():
    return inspect.stack()[1][3]

def whosdaddy():
    return inspect.stack()[2][3]
def bar():
    print ("hello, i'm %s ,\n %s"%(whoami(),whosdaddy()))

def foo():
    print ("hello, i'm %s ,\n %s"%(whoami(),whosdaddy()))
    bar()
foo()
bar()

s=whoami()
print(s,type(s))
