class Node:
    """Класс для узла односвязного списка"""
    __slots__ = ('data', 'next_node')
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if not self.head:
            self.head = Node(data, None)
        else:
            tmp_pointer = self.head
            while tmp_pointer.next_node:
                tmp_pointer = tmp_pointer.next_node
            tmp_pointer.next_node = Node(data, None)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        data_list = []
        if self.head is None:
            return []
        tmp_pointer = self.head
        while tmp_pointer.next_node:
            data_list.append(tmp_pointer.data)
            tmp_pointer = tmp_pointer.next_node
        data_list.append(tmp_pointer.data)
        return data_list

    def get_data_by_id(self, key_id):
        """ Возвращает первый найденный в LinkedList словарь с ключом 'id',
                значение которого равно переданному в метод значению"""
        for node in self.to_list():
            try:
                if node['id'] == key_id:
                    return node
            except:
                print('Данные не являются словарем или в словаре нет id.')
