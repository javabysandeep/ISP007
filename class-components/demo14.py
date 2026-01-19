class Test:
    x = 10

    def __init__(self):
        print('Test::constructor')

    def __del__(self):
        print('Test:: destructor')

    def instance_method(self):
        print('Test::instance_method')

    @staticmethod
    def static_method():
        print('Test::static_method')
        print(Test.x)

    @classmethod
    def class_method(cls):
        print('Test::class_method')
        # cls.instance_method()
        # cls.static_method()
        print(cls.x)


t1 = Test()
t1.instance_method()
Test.static_method()
Test.class_method()
