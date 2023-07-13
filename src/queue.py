class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """Конструктор класса Node"""
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Метод для добавления элемента в очередь"""
        if not self.head and not self.tail:    #if queue is empty
            self.head = self.tail = Node(data,None)
            return None

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def dequeue(self):
        """Метод для удаления элемента из очереди. Возвращает данные удаленного элемента"""
        if not self.head:    #if queue is empty
            return None
        if self.head is self.tail:    #if only one item is in the queue
            tmp_point = self.head
            self.head = self.tail = None
            return tmp_point.data

        tmp_point = self.head
        self.head = self.head.next_node
        return tmp_point.data


    def __str__(self):
        """Магический метод для строкового представления объекта"""
        tmp_pointer = self.head
        data_list = []
        while tmp_pointer:
            data_list.append(tmp_pointer.data)
            tmp_pointer = tmp_pointer.next_node
        return '\n'.join(data_list)
