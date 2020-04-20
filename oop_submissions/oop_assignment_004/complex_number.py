class ComplexNumber:
    def __init__(self,real=0,imag=0):
        if isinstance(real,str) and isinstance(imag,str):
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
        
    # Formula for complex number division is ((a/k)+(b/k)i)*((x/k)+(y/k)i), where k is absolute value
    
    def __truediv__(self,other):
        if other._real_part==0 and other._imaginary_part==0:
            raise ZeroDivisionError('division by zero')
        r1=self._real_part/abs(other)           # a/k
        r2=self._imaginary_part/abs(other)      # b/k
        i1=other._real_part/abs(other)          # c/k
        i2=other._imaginary_part/abs(other)     # y/k
        real=r1*i1+r2*i2
        imag=r1*-i2+r2*i1
        return __class__(round(real,2),round(imag,2))
        
    def __abs__(self):
        return round((self._real_part**2+self._imaginary_part**2)**0.5,3)
        
        
    def __eq__(self,other):
        if self._real_part==other._real_part and self._imaginary_part==other._imaginary_part:
            return True
        return False

        