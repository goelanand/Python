def hello(a=1,b=2,c=3):
    def newf(x,y):
        return a+b+c*x*y
    return newf
newf=hello(a=100,b=200)
f=newf(4,5)
print(f.newf())
        
