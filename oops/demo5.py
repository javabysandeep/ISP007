class Test:
    x=10
    xxx=111
    def __init__(self):
        self.y=100 # instance variable got created

ref=Test()
print(ref.y) #instance variable

ref.x=100 # creating instance variable
print(ref.x) # printing instance variable
print(Test.x) # static variable
del Test.xxx
print(Test.xxx)
