class MatrixSizeError(ArithmeticError):
    pass

class OperandTypeError(TypeError):
    pass

class Matrix(object):
    def __init__(self, value):
        self.value = [i for i in value]
        self.result = []

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise OperandTypeError(f"unsupported operand type(s) for +: 'Matrix' and '{type(other)}'")
        self.result = []
        for i, j in zip(self.value, other.value):
            self.result.append([x + y for x, y in zip(i, j)])
        return self.result
    

    def __sub__(self, other):
        self.result = []


    def __mul__(self, other):
        self.result = []


    def get_transpose_matrix(self):
        transpose = [[] for i in range(0,len(self.value[0]))]
        
        for i in self.value:
            for j, _ in enumerate(transpose):
                transpose[j].append(i.pop(0)) 
        print(transpose)
    def tolist(self):
        pass


a = Matrix([[23, 80, 91, 13, 58], [59, 87, 16, 12, 15], [66, 25, 31, 94, 75], [88, 33, 6, 7, 92]])
b = Matrix([[8, 75, 54, 90, 96], [55, 40, 85, 99, 2], [71, 97, 85, 54, 67], [22, 69, 73, 50, 71]])
print(a.get_transpose_matrix())