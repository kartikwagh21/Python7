x = 5 #global
def func():
    x = 10 #local
    print("Inside:",x)
func()
print("Outside:",x)