#Создать базовый класс «список» на основе обычного массива с  функциями вставки и удаления элементов.
#Реализовать на базе списка производные классы стека и очереди. 
#Для каждого класса провести модульное тестирование основных методов класса.

class List:
    def __init__(self):
        self._array = []

    #Вставляет элемент в заданный индекс
    def insert(self, index, value):
        if index < 0 or index > len(self._array):
            print("Индекс вне диапазона")
        else:
        	self._array.insert(index, value)

    #Удаляет элемент по индексу
    def delete(self, index):
        if index < 0 or index >= len(self._array):
            print("Индекс вне диапазона")
        else:
        	return self._array.pop(index)

    def __repr__(self):
        return repr(self._array)

class Stack(List):
    #Добавление элемента в стек
    def insert_s(self, value):
        self.insert(len(self._array), value)

    #Удаление и возвращение элемента из стека
    def pop(self):
        if len(self._array) == 0:
            print("Стек пуст")
        else:
        	return self.delete(len(self._array) - 1)

    #Вывод последнего элемента стека без удаления
    def last(self):
        if len(self._array) == 0:
            print("Стек пуст")
        else:
        	return self._array[-1]

class Queue(List):
    #Добавление элемента в конце очереди
    def insert_q(self, value):
        self.insert(len(self._array), value)

    #Удаление и возвращение элемента из начала очереди
    def delete_q(self):
        if len(self._array) == 0:
            print("Очередь пуста")
        else:
        	return self.delete(0)

    #Вывод первого элемента очереди без удаления
    def first(self):
        if len(self._array) == 0:
            print("Очередь пуста")
        else:
        	return self._array[0]

stack = Stack()
print("Работа со стеком")
print("Введите желаемую длину стека")
for x in range(int(input())):
	print("Введите число:")
	stack.insert_s(input())
print("Стек после добавления:", stack)
print("Последний элемент стека:", stack.last())
print("Удаленный элемент из стека:", stack.pop())
print("Стек после удаления:", stack)

queue = Queue()
print("Работа с очередью")
print("Введите желаемую длину очереди")
for x in range(int(input())):
	print("Введите число:")
	queue.insert_q(input())
print("Очередь после добавления:", queue)
print("Удаленный элемент из очереди:", queue.delete_q())
print("Первый элемент очереди:", queue.first())
print("Очередь после удаления:", queue)
