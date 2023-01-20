class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print('your dog '+self.name+' is siting')
    def wang(self):
        message='wang,wang,wang'
        return message

my_dog=Dog('wilian',15)
my_dog.sit()


class happyDog(Dog):
    def __init__(self, name, age):
        super().__init__(name,age)
    def happy_sit(self):
        print('your dog sitting happily')
your_dog=happyDog('ylian',10)
your_dog.sit()
your_dog.happy_sit()

from 外置类 import Cat
your_cat=Cat('yello',3)
your_cat.sit()