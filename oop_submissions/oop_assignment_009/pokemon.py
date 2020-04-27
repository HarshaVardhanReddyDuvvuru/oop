class Pokemon:
    
    _sound=""
    
    def __init__(self,name="",level=1):
        if len(name)==0:
            raise ValueError('name cannot be empty')
        self._name=name
        if level<=0:
            raise ValueError('level should be > 0')
        self._level=level
        self._master=None
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
    
    @property
    def master(self):
        if self._master==None:
            print("No Master")
            return
        return self._master
        
    def __str__(self):
        return f'{self._name} - Level {self._level}'
        
    @classmethod
    def make_sound(cls):
        print(cls._sound)
        
    def new_master(self,master):
        self._master=master
    
            
class ElectricPokemon(Pokemon):
    def attack(self):
        print(f'Electric attack with {self._level*10} damage')
   
        
class WaterPokemon(Pokemon):
    
    _pokemon_name=""
    def attack(self):
        print(f'Water attack with {self._level*9} damage')
    
    @classmethod
    def swim(cls):
        print(f'{cls._pokemon_name} swimming...')

    
class FlyingPokemon(Pokemon):
    
    _pokemon_name=""

    def attack(self):
        print(f'Air attack with {self._level*5} damage')
    
    @classmethod
    def fly(cls):
        print(f'{cls._pokemon_name} flying...')


class RunningPokemon:
    
    _pokemon_name=""
    
    @classmethod
    def run(cls):
        print(f"{cls._pokemon_name} running...")  
    
    
class Pikachu(ElectricPokemon,RunningPokemon):
    
    _sound="Pika Pika"
    _pokemon_name="Pikachu"
    
        
class Squirtle(WaterPokemon,RunningPokemon):
    
    _sound="Squirtle...Squirtle"
    _pokemon_name="Squirtle"
    
    
class Pidgey(FlyingPokemon):
    
    _sound="Pidgey...Pidgey"
    _pokemon_name="Pidgey"
    

class Swanna(WaterPokemon,FlyingPokemon):
    
    _sound="Swanna...Swanna"
    _pokemon_name="Swanna"
    
    def attack(self):
        WaterPokemon.attack(self)
        FlyingPokemon.attack(self)
    
        
class Zapdos(FlyingPokemon,ElectricPokemon):
    
    _sound="Zap...Zap"
    _pokemon_name="Zapdos"
    def attack(self):
        ElectricPokemon.attack(self)
        FlyingPokemon.attack(self)
    
    
class Island:
    
    _islands_list=[]
    
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        Island._islands_list.append(self)
        
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
        return cls._islands_list


class Trainer:
    
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self._experience
        self._food_in_bag=0
        self._current_island=""
        self._pokemon_treasure=[]
    
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
            pokemon.new_master(self)
            return
        
        print(f"You need more experience to catch {pokemon.name}")
      
    def get_my_pokemon(self):
        return self._pokemon_treasure
        
