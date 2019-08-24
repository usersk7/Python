class myclass:
    prof ="student"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def address(self,add):
        return add

obj1 = myclass("Shubham",22)


print("my name is {} from {} and age is {} i am {}".format( obj1.name,obj1.address("pune"), obj1.age, obj1.__class__.prof))
