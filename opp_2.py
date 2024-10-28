#Создать базовый класс с функцией – сумма прогрессии. Создать производные классы:
#арифметическая прогрессия и геометрическая прогрессия. Каждый класс имеет два поля типа double.
#Первое – первый член прогрессии, второе – постоянная разность (для арифметической)
#и постоянное отношение (для геометрической). Определить функцию вычисления суммы,
#где параметром является количество элементов прогрессии. 

class Progression:
    def __init__(self, first_el, constant):
        self.first_el = first_el
        self.constant_something = constant_something

    def sum(self, n):
        raise NotImplementedError("Метод sum() должен быть переопределен в производных классах.")


class Arithmetic(Progression):
    def sum(self, n):
        return n / 2 * (2 * self.first_el + (n - 1) * self.constant)


class Geometric(Progression):
    def sum(self, n):
        if self.constant == 1:
            return n * self.first_el  # Если отношение равно 1
        return self.first_el * (1 - self.constant ** n) / (1 - self.constant)

a_progression = ArithmeticProgression(1, 2)
print("Сумма первых 5 членов арифметической прогрессии:", a_progression.sum(5))

g_progression = GeometricProgression(1, 3)
print("Сумма первых 5 членов геометрической прогрессии:", g_progression.sum(5))
