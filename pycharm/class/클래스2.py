
# 클래스 정의 : X
class MyClass:
    name = '희영'
    age  = 1000000000

    def sayHello(self): #self
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello

    def addAge(self):
        return self.age+1

myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()
obj_age = myClass.addAge()

print('Object name   :', obj_name)
print('Object method :', obj_method)
print('Object age :', obj_age)
print('Object age {:,}'.format(obj_age))
print('Object age {:0,.1f}' .format(obj_age))
print('Object age {:0,.2f}' .format(obj_age))

# 클래스 정의 : X
class MyClass:
    name = str()
    # age  = 1000000000

    def sayHello(self): #self
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello

    def addAge(self):
        return self.age+1

myClass = MyClass()
myClass.name='영목'
obj_name = myClass.name
# obj_method = myClass.sayHello()
# obj_age = myClass.addAge()

print('Object name   :', obj_name)
print('Object method :', obj_method)
print('Object age :', obj_age)
print('Object age {:,}'.format(obj_age))
print('Object age {:0,.1f}' .format(obj_age))
print('Object age {:0,.2f}' .format(obj_age))
