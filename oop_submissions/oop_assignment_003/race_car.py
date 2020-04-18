from car import Car
class RaceCar(Car):
    sound="Peep Peep\nBeep Beep"
    def __init__(self,max_speed=0,acceleration=0,tyre_friction=0,color=None):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._nitro=0
        
    def accelerate(self):
        from math import ceil
        nitro_boost=0
        if self._is_engine_started and self._nitro>0:
            self._nitro-=10
            nitro_boost=ceil(self._acceleration*0.3)
        self._current_speed+=nitro_boost
        super().accelerate()
            
    def apply_brakes(self):
        if self._current_speed>(self._max_speed//2):
            self._nitro+=10
        super().apply_brakes()
            
    @property       
    def nitro(self):
        return self._nitro
            
        