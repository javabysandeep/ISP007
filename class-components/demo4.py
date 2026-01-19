class Test:
    x=20 # this is a static variable

    def __init__(self):
        #creating static variable inside the constructor using ClassName
        Test.static_variable1='this is static variable1'
        self.y=30
        z=40

    def instance_method(self):
        # creating static variable inside the instance method using ClassName
        Test.static_variable2 = 'this is static variable2'

    @staticmethod
    def static_method():
        # creating static variable inside the static method using ClassName
        Test.static_variable3 = 'this is static variable3'


ref=Test()
print(ref.x)
print(Test.x)
print(ref.y)
#print(ref.z)#Error : Z is local to constructor
ref.instance_method()
Test.static_method()

print("static variable 1=",Test.static_variable1)
print("static variable 2=",Test.static_variable2)
print("static variable 3=",Test.static_variable3)


