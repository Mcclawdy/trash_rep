import math

class OperandTypeError(TypeError):
    pass
class MoneyArithmeticError(ArithmeticError):
    pass

class Money(object):
    def __init__(self, whole, fraction = 0):
        self.whole = whole
        self.fraction = fraction
        

    def float_converter(self):
        if self.fraction >= 10:
            fraction = float(f'0.{self.fraction}')
        else:
            fraction = float(f'0.0{self.fraction}') 
        return self.whole + fraction


    def money_converter(self, math_expression):
        """конвертируем полученное значение из операторов в тип money"""
        result = math.modf(math_expression)
        return Money(int(result[1]), round(result[0] * 100))
        

    def __add__(self, other):
        """+"""
        if not isinstance(other, Money):
            raise OperandTypeError(f"unsupported operand type(s) for +: 'Money' and '{other.__class__.__name__}'")
        return self.money_converter(self.float_converter() + other.float_converter())


    def __sub__(self, other):
        """-"""
        if not isinstance(other, Money) :
            raise OperandTypeError(f"unsupported operand type(s) for -: 'Money' and '{other.__class__.__name__}'")
        return self.money_converter(self.float_converter() - other.float_converter())


    def __mul__(self, other):
        """*"""
        if not isinstance(other, (int,float)):
            raise OperandTypeError(f"unsupported operand type(s) for *: 'Money' and '{other.__class__.__name__}'")
        return self.money_converter(self.float_converter() * other) 


    def __truediv__(self, other):
        """/"""
        if not isinstance(other, (Money, int)) :
            raise OperandTypeError(f"unsupported operand type(s) for /: 'Money' and '{other.__class__.__name__}'")

        if isinstance(other, int) and other == 0:
            raise MoneyArithmeticError ('The coefficient should be positive')
      
        return self.money_converter(self.float_converter() / other) if isinstance(other, int) else self.float_converter() /  other.float_converter()
        # тута поправить
        # return round(self.float_converter() / other, 2) if isinstance(other, int) else self.money_converter(self.float_converter() / other.float_converter())

    def __eq__(self, other):
        """=="""
        if not isinstance(other, (Money,)):
            raise OperandTypeError(f"comparison not supported between instances of 'Money' and '{other.__class__.__name__}'")
        else:
           return self.whole == other.whole and self.fraction == other.fraction


    def __gt__(self, other):
        """>"""
        if not isinstance(other, Money):
            return super().__gt__(self.whole)
        return self.float_converter() > other.float_converter()
       


    def __ge__(self, other):
        """>="""
        if not isinstance(other, Money):
            return super().__ge__(self.whole)
        return self.float_converter() >= other.float_converter()


    def __repr__(self):
        return f'{self.__class__.__name__}({self.get_whole()}, {self.get_fraction()})'


    def get_whole(self):
        return self.whole


    def get_fraction(self):
        return self.fraction

# a = Money(379, 99)
# b = Money(203, 70)
# c = 15.01
# d = 15
# print(a / b)
# print(type(a / b))