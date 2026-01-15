# variable scope= where a variable is visible annd accessible
# scoperesolution  = (LEGB)   local -> enclosed -> global -> built-in


def func1():
    x = 10  # local variable
    print(x)
def func2():
    print(x)
    
x = 12

func1()
func2()