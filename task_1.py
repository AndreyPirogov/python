import copy


def add_list(var_1, var_2):
    new_list = []
    if len(var_1) >= len(var_2):
        for el in range(len(var_1)):
            if el < len(var_2):
                new_list.append(var_1[el] + var_2[el])
            else:
                new_list.append(var_1[el])
    else:
        new_list = add_list(var_2, var_1)
    return new_list


class Matrix:

    def __init__(self, arg):
        self.matrix = []
        for el in arg:
            self.matrix.append(el)
        self.len = len(arg)

    def __str__(self):
        string = ""
        for el in self.matrix:
            for i in el:
                string += str(i) + " "
            string.rstrip()
            string = string + "\n"
        return string

    def __len__(self):
        return self.len

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix) >= len(other.matrix):
            for el in range(len(self.matrix)):
                if el < len(other.matrix):
                    new_matrix.append(add_list(self.matrix[el], other.matrix[el]))
                else:
                    new_matrix.append(self.matrix[el])
        else:
            for el in range(len(other.matrix)):
                if el < len(self.matrix):
                    new_matrix.append(add_list(self.matrix[el], other.matrix[el]))
                else:
                    new_matrix.append(other.matrix)
        return Matrix(new_matrix)


my_matrix = Matrix([[12, 13, 15], [5, 46, 7], [23, 21], [14]])
my_matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [5], [55, 5, 12]])
my_matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(my_matrix)
print(my_matrix_2)
print(my_matrix_3)
print(my_matrix + my_matrix_2 + my_matrix_3)

