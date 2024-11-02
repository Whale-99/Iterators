# Пользовательское исключение StepValueError, унаследованное от ValueError
class StepValueError(ValueError):
    pass


# Класс Iterator
class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

        # Проверка на некорректный шаг
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        # Сброс указателя на начало
        self.pointer = self.start
        return self

    def __next__(self):
        # Проверка окончания итерации
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        # Сохранение текущего значения указателя перед увеличением
        current = self.pointer
        self.pointer += self.step  # Увеличение указателя на шаг
        return current


# Пример использования
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')  # Вывод ошибки шага

# Примеры создания итераторов с различными параметрами
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Итерация по созданным итераторам
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
