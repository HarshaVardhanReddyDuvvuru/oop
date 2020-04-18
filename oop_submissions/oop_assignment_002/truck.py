from car import Car
        
class Truck(Car):
    
    sound="Honk Honk"
    
    def __init__(self,max_speed=0,acceleration=0,tyre_friction=0,color=None,max_cargo_weight=0):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._load=0
        if max_cargo_weight<0:
            raise ValueError('Invalid value for max_cargo_weight')
        self._max_cargo_weight=max_cargo_weight
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
           
    def load(self,load):
        if load<0:
            raise ValueError('Invalid value for cargo_weight')
            
        if self._current_speed==0:
            if self._load+load>self._max_cargo_weight:
                    print('Cannot load cargo more than max limit: {}'.format(int(self._max_cargo_weight)))                    
            else:
                self._load+=load
                
        else:
            print('Cannot load cargo during motion')
    
    def unload(self,load):
        if load<0:
            raise ValueError('Invalid value for cargo_weight')

        if self._current_speed==0:
            if self._load>=load:
                self._load-=load
                    
        else:
            print('Cannot unload cargo during motion')
    
        

                
    