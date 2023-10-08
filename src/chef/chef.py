class Chef:
    def __init__(self, sous_chef):
        self.sous_chef = sous_chef
    
    def make_random_meals(self, number=1):
        return self.sous_chef.get_random_meals(number)
