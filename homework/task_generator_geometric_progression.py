def geometric_progression_generator(q, b):
    if b == 0:
        raise ArithmeticError("The denominator is zero")
    if q == 0:
         raise ArithmeticError("The first term is zero")
    
    while 1:
        yield  q
        q *= b 