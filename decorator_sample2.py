def double_result(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        result*=2
        return result
    return wrapper

@double_result
def add(a,b):
    return a+b

print(add(5,6))            



    
