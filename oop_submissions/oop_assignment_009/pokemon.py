class Pokemon:
    
    sound=""
    
    def __init__(self,name="",level=1):
        if len(name)==0:
            raise ValueError('name cannot be empty')
        self._name=name
        if level<=0:
            raise ValueError('level should be > 0')
        self._level=level
        self._master=""
        
    def __str__(self):
        return f'{self._name} - Level {self._level}'
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
    
    @property
    def master(self):
        if self._master=="":
            print("No Master")
            return
        return self._master
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
            
class ElectricPokemon:
    
    def __init__(self):
        self._current_level=0
    
    def attack(self):
        print(f'Electric attack with {self._current_level*10} damage')
        
class WaterPokemon:
    
    _pokemon_name=""
    
    def __init__(self):
        self._current_level=0
    
    @classmethod
    def swim(cls):
        print(f'{cls._pokemon_name} swimming...')
    
    def attack(self):
        print(f'Water attack with {self._current_level*9} damage')
    

class FlyingPokemon:
    
    _pokemon_name=""
    
    def __init__(self):
        self._current_level=0
    
    @classmethod
    def fly(cls):
        print(f'{cls._pokemon_name} flying...')
    
    def attack(self):
        print(f'Air attack with {self._current_level*5} damage')
    
    
class Pikachu(Pokemon,ElectricPokemon):
    
    sound="Pika Pika"
    
    def __init__(self,name="",level=1):
        super().__init__(name=name,level=level)
        self._current_level=self._level
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def run(cls):
        print("Pikachu running...")
        
class Squirtle(Pokemon,WaterPokemon):
    
    sound="Squirtle...Squirtle"
    _pokemon_name="Squirtle"
    
    def __init__(self,name="",level=1):
        super().__init__(name=name,level=level)
        self._current_level=self._level
      
    @classmethod
    def run(cls):
        print("Squirtle running...")  
    
class Pidgey(Pokemon,FlyingPokemon):
    
    sound="Pidgey...Pidgey"
    _pokemon_name="Pidgey"
    
    def __init__(self,name="",level=1):
        super().__init__(name=name,level=level)
        self._current_level=self._level
        

class Swanna(Pokemon,WaterPokemon,FlyingPokemon):
    
    sound="Swanna...Swanna"
    _pokemon_name="Swanna"
    
    def __init__(self,name="",level=1):
        super().__init__(name=name,level=level)
        self._current_level=self._level
        
    def attack(self):
        print(f'Water attack with {self._current_level*9} damage')
        print(f'Air attack with {self._current_level*5} damage')
        
class Zapdos(Pokemon,ElectricPokemon,FlyingPokemon):
    
    sound="Zap...Zap"
    _pokemon_name="Zapdos"
    
    def __init__(self,name="",level=1):
        super().__init__(name=name,level=level)
        self._current_level=self._level
        
    def attack(self):
        print(f'Electric attack with {self._current_level*10} damage')
        print(f'Air attack with {self._current_level*5} damage')
        

class Island:
    
    all_islands_list=[]
    
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        Island.all_islands_list.append(self)
        
    @property
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    
    def __str__(self):
        return f'{self._name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
    
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch<self._max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
            return
        print("Island at its max pokemon capacity")
    
    @classmethod    
    def get_all_islands(cls):
        for island in cls.all_islands_list:
            print(str(island))

class Trainer:
    
    _pokemon_treasure=[]
    
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self._experience
        self._food_in_bag=0
        self._current_island=""
    
    @property
    def name(self):
        return self._name
     
    @property  
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    @property
    def current_island(self):
        if self._current_island=="":
            print("You are not on any island")
            return
        return self._current_island
        
    def move_to_island(self,island):
        self._current_island=island
        
    def collect_food(self):
        if self._current_island=="":
            print("Move to an island to collect food")
            return
        
        if self._food_in_bag==self._max_food_in_bag:
            return
        
        if self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
            self._food_in_bag=self._max_food_in_bag
            self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
            return
        self._food_in_bag=self._current_island._total_food_available_in_kgs
        self._current_island._total_food_available_in_kgs=0

    def catch(self,pokemon):
        if self._experience>=100*pokemon._level:
            print(f"You caught {pokemon._name}")
            self._experience+=(20*pokemon._level)
            self._pokemon_treasure.append(pokemon)
            pokemon._master=self
            return
        
        print("You need more experience to catch Pigetto")
        
    def get_my_pokemon(self):
        for pokemon in self._pokemon_treasure:
            print(pokemon)
        
        
