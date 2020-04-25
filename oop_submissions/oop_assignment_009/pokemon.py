class Pokemon:
    
    sound=""
    
    def __init__(self,name="",level=1):
        if len(name)==0:
            raise ValueError('name cannot be empty')
        self._name=name
        if level<=0:
            raise ValueError('level should be > 0')
        self._level=level
        
    def __str__(self):
        return f'{self._name} - Level {self._level}'
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
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
        

        