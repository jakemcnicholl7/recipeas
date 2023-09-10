class Chef:
    def __init__(self, sous_chef):
        self.sous_chef = sous_chef
    
    def make_random_meal(self):
        return self.sous_chef.get_random_meal()
