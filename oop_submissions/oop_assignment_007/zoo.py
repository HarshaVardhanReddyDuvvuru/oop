class Deer:
    breathe_type="Breathe in air"
    sound="Buck Buck"
    
    def __init__(self,breed,required_food_in_kgs,age_in_months=1):
        
        if required_food_in_kgs<=0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        self._required_food_in_kgs=required_food_in_kgs
            
        if age_in_months>1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        self._age_in_months=age_in_months
        
        self._breed=breed
    
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=2
    
    @classmethod    
    def make_sound(self):
        print(self.sound)
        
    @classmethod
    def breathe(self):
        print(self.breathe_type)
        
        
class Lion(Deer):
    
    hunt_type="Buck Buck"
    hunt_value="No deers to hunt"
    sound="Roar Roar"
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=4
        
    def hunt(self,zoo):
        count=0
        for animal in zoo._animals:
            if animal.sound==self.hunt_type:
                zoo._animals.remove(animal)
                count+=1
            
        if count==0:
            print(self.hunt_value)
        
        
class Shark(Lion):
    
    hunt_type="Hum Hum"
    hunt_value="No GoldFish to hunt"
    sound="Shark Sound"
    breathe_type="Breathe oxygen from water"
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=8
        
class GoldFish(Shark):
    
    sound="Hum Hum"
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.2
        

class Snake(Lion):
    
    sound="Hiss Hiss"
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.5
        
        
class Zoo:
    
    total_animals=[]
    animo=[]
    
    def __init__(self):
        self._reserved_food_in_kgs=0
        self._animals=[]
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    
    def add_food_to_reserve(self,value):
        self._reserved_food_in_kgs+=value
        
        
    def count_animals(self):
        return len(self._animals)
        
        
    def add_animal(self,animal):
        self._animals.append(animal)
        self.animo.append(animal)
        self.total_animals.append(animal)
        
    def feed(self,animal):
        if self._reserved_food_in_kgs>=animal.required_food_in_kgs:
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
            animal.grow()
        
        else:
            self._reserved_food_in_kgs=0

    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(Zoo.total_animals)
        
    @staticmethod
    def count_animals_in_given_zoos(zoos):
        count=0
        for zoo in zoos:
            count+=zoo.count_animals()
        
        return count
        

