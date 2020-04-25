class Animal:
    
    _increase_age_in_months=1  
    _increase_required_food_in_kgs=2  
    _animal_sound="Buck Buck"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months!=1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        self._age_in_months=age_in_months
        
        if not isinstance(breed,str):
            raise ValueError('Invalid value for  breed')
        self._breed=breed
        
        if required_food_in_kgs<=0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        self._required_food_in_kgs=required_food_in_kgs
        
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @property
    def breed(self):
        return self._breed
    
    def grow(self):
        self._age_in_months+=self._increase_age_in_months
        self._required_food_in_kgs+=self._increase_required_food_in_kgs
    
    @classmethod    
    def make_sound(cls):
        print(cls._animal_sound)
        
class LandAnimals:
    
    @classmethod
    def breathe(cls):
        print("Breathe in air")

class WaterAnimals:
    
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
        
class HuntingAnimals:
    
    _prey_type=None
    _prey_value="deers"
    
    @classmethod
    def hunt(cls,zoo):
        for animal in zoo._animal_list:
            if isinstance(animal,cls._prey_type):
                zoo._animal_list.remove(animal)
                zoo._total_animals_in_all_zoos.remove(animal)
                return
            
        print(f'No {cls._prey_value} to hunt')
            
class Deer(Animal,LandAnimals):
    _increase_required_food_in_kgs=2

class Lion(Animal,LandAnimals,HuntingAnimals):
    _increase_required_food_in_kgs=4
    _animal_sound="Roar Roar"
    _prey_type=Deer

class GoldFish(Animal,WaterAnimals):
    _increase_required_food_in_kgs=0.2
    _animal_sound="Hum Hum"
    
class Shark(Animal,WaterAnimals,HuntingAnimals):
    _increase_required_food_in_kgs=8
    _animal_sound="Shark Sound"
    _prey_type=GoldFish
    _prey_value="GoldFish"

class Snake(Animal,LandAnimals,HuntingAnimals):
    _increase_required_food_in_kgs=0.5
    _animal_sound="Hiss Hiss"
    _prey_type=Deer
    
class Zoo:
    
    _total_animals_in_all_zoos=[]
    
    def __init__(self):
        self._reserved_food_in_kgs=0
        self._animal_list=[]
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food_quantity):
        self._reserved_food_in_kgs+=food_quantity
        
    def add_animal(self,animal):
        self._animal_list.append(animal)
        self._total_animals_in_all_zoos.append(animal)
        
    def count_animals(self):
        return len(self._animal_list)
        
    def feed(self,animal):
        if self._reserved_food_in_kgs>=animal.required_food_in_kgs:
            self._reserved_food_in_kgs-= animal.required_food_in_kgs
            animal.grow()
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls._total_animals_in_all_zoos)
    
    @staticmethod
    def count_animals_in_given_zoos(zoos):
        count=0
        for zoo in zoos:
            count+=zoo.count_animals()
            
        return count
