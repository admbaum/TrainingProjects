class Complex:
    'this class simulates complex numbers'
    def __init__(self, real, imag): # constructor, creates instances

        self.real = real  # instance variable
        self.imag = imag  # instance variable

        # self.real is the instance variable and the part after the = is the constructor argument

c = Complex(1, 1)
'''created an instance of Complex and assigned it to the variable c, while passing the integer 1 as
   an argument for real and 1 as an arguement for imag'''

print(c.real, c.imag)
#  Just prints to the console.



