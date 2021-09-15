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


    #def __rmul__(self,other):
    #    return self * other
    
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

x = Complex(3, 6) 
y = 2 * x
print(x.__dict__)
'''if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(Complex, globals(), name='HW1',verbose=True)'''