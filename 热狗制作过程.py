class hot_dog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = '生的'
        self.condiments = []
    def __str__(self):
        mag = '热狗'
        if len(self.condiments) > 0:
            mag = mag + '和'
        for i in self.condiments:
            mag = mag + str(i) + ', '
        mag = mag.strip(', ')
        mag = self.cooked_string +  mag + '。'
        return mag
    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = '过熟的'
        elif self.cooked_level > 5:
            self.cooked_string = '刚刚好的'
        elif self.cooked_level > 3:
            self.cooked_string = '较生的'
        else:
            self.cooked_string = '生的'
    def add_condiment(self, condiments):
        self.condiments.append(condiments)


my_dog = hot_dog()
print(my_dog)
print('烤上热狗4分钟……')
my_dog.cook(4)
print(my_dog)
print('再烤上热狗3分钟……')
my_dog.cook(3)
print(my_dog)
print('如果我再烤上10分钟会怎么样？')
my_dog.cook(10)
print(my_dog)
print("现在我要去往热狗里加配料了。")
my_dog.add_condiment('番茄酱')
my_dog.add_condiment('芥末酱')
print(my_dog)