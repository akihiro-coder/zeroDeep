class Man:
    def __init__(self, name):
        self.name = name
        print('Initialize!')

    def hello(self):
        print("hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye "+ self.name + "!")


m = Man("Akihiro")
m.hello()
m.goodbye()








