class person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def myfunc(self):
        print("hello,"+self.name)

p1=person("John",36)
p1.myfunc()
