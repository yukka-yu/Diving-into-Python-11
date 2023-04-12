class Matrix:
    """Класс матрицы."""

    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        return '\n'.join('  '.join(map(str, row)) for row in self.m_list)

    def __add__(self, other):
        self.height = len(self.m_list)
        self.width = len(self.m_list[0])
        other.height = len(other.m_list)
        other.width = len(other.m_list[0])
        if self.width == other.width and self.height == other.height:
            return Matrix([[self.m_list[i][j] + other.m_list[i][j] for i in range(self.width)]
                           for j in range(self.height)])
        else:
            return None

    def summa(self):
        """Суммирует все элементы матрицы."""
        return sum([self.m_list[i][j] for i in range(self.width) for j in range(self.height)])

    def __eq__(self, other):
        """Сравнивает размеры матрицы и их поэлементное равенство."""
        
        if self.width == other.width and self.height == other.height:
            for i in range(self.width):
                for j in range(self.height):
                    if self.m_list[i][j] != other.m_list[i][j]:
                        return False
        return True

    def __gt__(self, other):
        """Больше ли сумма всех элементов или меньше."""
        return self.summa() > other.summa()

    def __ge__(self, other):
        """Не больше, меньше или равны ли суммы элементов."""
        return self.summa() <= other.summa()

    def __le__(self, other):
        """Не меньше, больше или равны ли суммы элементов."""
        return self.summa() >= other.summa()
    
    def __mul__(self, other):
        if self.width == other.height:
            mul_list = [[0] * self.height for i in range(other.width)]
            for i in range(self.height):
                for j in range(other.width):
                    mul_list[i][j] = sum([self.m_list[i][k] * other.m_list[k][j] for k in range(self.width)])
            return Matrix(mul_list)
        else:
            return None
            


if __name__ == '__main__':
    li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = Matrix(li)
    n = Matrix(li2)
    print(m)
    print()
    print(n)
    print()
    print(m + n)

    print(m == n)
    print(m != n)
    print(m > n)
    print(m < n)
    print(m >= n)
    print(m <= n)
    print(m * n)