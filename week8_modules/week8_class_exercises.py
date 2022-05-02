

class Babies():

    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age

    def baby_gen(self, amount):
        my_set = {()}
        for x in range(amount):
            my_set.add(self.height,self.weight,self.age)
        print(my_set)


    baby_gen(6)