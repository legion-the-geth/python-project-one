class User:
    
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        # self.sayHi()
    
    def sayHi(self):
        print('Hello world, My name is ' + self.prenom + ' ' + self.nom + ' and I am ' + str(self.age) + ' years old.')
    