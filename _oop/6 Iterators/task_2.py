# Завдання 2
# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи очищення списку,
# додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.

class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    #  Метод поиска значения по индексу
    def _get(self, ind):
        index = self._head
        index_counter = 0
        try:
            while index_counter <= ind:
                if index_counter == ind:
                    return index.value
                index_counter += 1
                index = index.next
        except:
            print("Такого индекса нет в списке")

    #  Метод очистки списка
    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0

    #  Метод вставки значения по индексу
    def insert_index(self, ind, data):
        if self._head is None:
            print("Список пуст")
            return
        else:
            index = self._head
            index_counter = 0
            try:
                while index_counter <= ind:
                    if index_counter == ind:
                            index.value = data
                    index_counter += 1
                    index = index.next
            except:
                print("Такого индекса нет в списке")

    #  Метод вставки значения после определенного значения
    def in_after_item(self, x, data):
        if self._head is None:
            print("Список пуст")
            return
        else:
            n = self._head
            while n is not None:
                if n.value == x:
                    break
                n = n.next
            if n is None:
                print("Значения нет в списке")
            else:
                new_node = MyList._ListNode(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    #  Метод удаления значения с конца
    def dell_end(self):
        if self._head is None:
            print("Список пуст")
            return
        if self._head.next is None:
            self._head = None
            return
        n = self._head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    #  Метод удаления значения по индексу
    def dell_index(self, ind):
        index = self._head
        index_counter = 0
        while index_counter <= ind:
            if index_counter == ind:
                if ind == 0:
                    self._head = index.next
                else:
                    index.prev.next = index.next
            index_counter += 1
            index = index.next

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    # Повторный обход списка
    for element in my_list:
        print(element)

    print('\nДЗ! <<<<<<<<<<\n')
    my_list.insert_index(2, 6)  # Метод вставки значения по индексу
    my_list.insert_index(3, 9)
    print(my_list)

    print(my_list._get(1))  # Метод поиска значения по индексу
    print(my_list._get(3))

    my_list.dell_index(1)  # Метод удаления значения по индексу
    print(my_list)

    my_list.in_after_item(1, 4)  # Метод вставки значения после определенного значения
    print(my_list)

    my_list.dell_end()  # Метод удаления значения с конца
    print(my_list)

    my_list.clear()  # Метод очистки списка
    print(my_list)
    print('\n>>>>>>> КОНЕЦ ДЗ!')


if __name__ == '__main__':
    main()
