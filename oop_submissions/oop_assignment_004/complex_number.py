from math import sqrt,pow
class ComplexNumber:
    def __init__(self,real=0,imag=0):
        if isinstance(real,str) and isinstance(imag,str):   # it is same as type(real)==str and type(imag)==str
            raise ValueError('Invalid value for real and imaginary part')
            
        if isinstance(real,str):
            raise ValueError('Invalid value for real part')
        self._real_part=real
        
        if isinstance(imag,str):
            raise ValueError('Invalid value for imaginary part')
        self._imaginary_part=imag
        
    @property
    def real_part(self):
        return self._real_part
    
    @property
    def imaginary_part(self):
        return self._imaginary_part
        
    def __str__(self):
        return '{}{:+}i'.format(self._real_part,self._imaginary_part)
            
    def conjugate(self):
        return __class__(self._real_part,-self._imaginary_part)
      
    def __sub__(self,other):
        real=self._real_part-other._real_part
        imag=self._imaginary_part-other._imaginary_part
        return __class__(real,imag)
            
    def __add__(self,other):
        real=self._real_part+other._real_part
        imag=self._imaginary_part+other._imaginary_part
        return __class__(real,imag)
    
    def __mul__(self,other):
        real=(self._real_part*other._real_part)-(self._imaginary_part*other._imaginary_part)
        imag=(self._real_part*other._imaginary_part)+(self._imaginary_part*other._real_part)
        return __class__(real,imag)
        
    def __truediv__(self,other):
        if (other._real_part==0) and (other._imaginary_part==0):
            raise ZeroDivisionError('division by zero')
        num=self.__mul__(other.conjugate())
        den=pow(other._real_part,2)+pow(other._imaginary_part,2)
        real=num._real_part/den
        imag=num._imaginary_part/den
        return __class__(real,imag)
        
    def __abs__(self):
        return round(sqrt(pow(self._real_part,2)+pow(self._imaginary_part,2)),3)
        
        
    def __eq__(self,other):
        return (self._real_part==other._real_part) and (self._imaginary_part==other._imaginary_part)
