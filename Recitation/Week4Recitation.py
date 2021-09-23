class Complex:    
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
    
    def __str__(self):
        """Display complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"


    def __rmul__(self,other):
        return self * other
    
    def __mul__(self, other):
        if isinstance(other, Complex):
            realComponent = self._real * other._real - self._imag * other._imag
            imagComponent = self._real * other._imag + self._imag * other._real
            ans = Complex(realComponent, imagComponent)
        else:
            ans = Complex(self._real * other, self._imag * other)
        return ans
        
    def conjugate(self):
        return Complex(self._real, self._imag * -1)

class Real(Complex):
    '''
           >>> x = Real(3) 
>>> int(x) * [1,2,3] 
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> y = int(x) 
>>> y
3
>>> isinstance(y, int) 
True
>>> isinstance(y, Real) 
False
>>> z = float(x)        
>>> z                   
3.0
>>> isinstance(z, float) 
True
>>> isinstance(z, Real)  
False
    '''

    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self, other):
        if isinstance(other, Real):
            return Real(self._real * other._real)
        if isinstance(other, Complex):
            return super().__mul__(other)
        return Real(self._real * other)
    
    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):

        ''' Returns True if other is a Real object that has the same value or if other is
            a Complex object with _imag=0 and same value for _real, False otherwise

            >>> Real(4) == Real(4)
            True
            >>> Real(4) == Real(4.0)
            True
            >>> Real(5) == Complex(5, 0)
            True
            >>> Real(5) == Complex(5, 12)
            False
            >>> Real(5) == 5.5
            False
        '''
        if isinstance(other, Real) or isinstance(other, Complex):
            return self._real == other._real and other._imag == 0
        return self._real == other
        
    def __int__(self):
        return int(self._real)
    def __float__(self):
        return float(self._real)

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(Real, globals(), name='HW1',verbose=True)