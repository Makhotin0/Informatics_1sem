class Heap:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.left = left
            self.right = right
            self.value = value

        def __repr__(self):
            value_list = self.listing()
            depth = 0
            counter = 0
            floor = []
            print(value_list)
            for i in range(len(value_list)):
                counter += 1
                if value_list[i]:
                    floor.append(value_list[i])
                else:
                    floor.append(None)
                if 2 ** depth == counter:
                    counter %= (2 ** depth)
                    depth += 1
                    print(*floor)
                    floor = []
                    continue

            return ''

        def listing(self) -> list:
            nodes_list = []

            if self.left:
                nodes_list.append(self.left)
            if self.right:
                nodes_list.append(self.right)
            for node in nodes_list:
                if not node:
                    continue
                if node.left:
                    nodes_list.append(node.left)
                else:
                    nodes_list.append(None)
                if node.right:
                    nodes_list.append(node.right)
                else:
                    nodes_list.append(None)
            value_list = [self.value]
            for node in nodes_list:
                if node:
                    value_list.append(node.value)
                else:
                    value_list.append(None)

            return value_list

        def get_value(self):
            return self.value

        def get_child(self, side='left'):
            if side == 'left':
                return self.left
            elif side == 'right':
                return self.right
            else:
                return ValueError

        def set_child(self, node, side='left'):
            if side == 'left':
                self.left = node
                return
            elif side == 'right':
                self.right = node
                return
            else:
                return ValueError

    def __init__(self):
        self.root = None
    def get_root(self):
        return self.root
    def add(self, num):
        assert isinstance(num, int)
        node = self.Node(num)
        if not self.root:
            self.root = node
            return
        current_node = self.root
        up_node = None
        while node.value > current_node.value:
            if not current_node.left:
                if current_node.left == None:
                    current_node.left = node
                else:
                    current_node = current_node.left
                    current_node.left = node
                return
            elif not current_node.right:
                if current_node.right == None:
                    current_node.right = node
                else:
                    current_node = current_node.right
                    current_node.right = node
                return
            up_node = current_node
            current_node = current_node.left
        if up_node != None:
            up_node.left = node
        node.left = current_node
        current_node.left = None
        node.right = current_node.right
        return

    #Я вроде бы исправил добавление. Теперь оно добавляет элемент вместо того, чтобы просто его заменять.
    #Но всё равно имеются проблемы с отображением пирамиды и тем, что у None могут быть потомки. :/
    #I can't fix that
    #В принципе удаление вроде бы работает коректно, но я не смог протестировать его на всех вариантах распложения элементов в куче.

    def pop(self) -> int: # НАПИСАТЬ УДАЛЕНИЕ КОРНЯ (done)
        del_current_node = self.root
        if del_current_node.value == None:
            print("Нечего удалять")
            return
        while del_current_node.left and del_current_node.right:
            if del_current_node.right.value == None or del_current_node.left.value == None:
                if del_current_node.right.value == None:
                    del_current_node.value = del_current_node.left.value
                    del_current_node = del_current_node.left
                else:
                    del_current_node.value = del_current_node.right.value
                    del_current_node = del_current_node.right
            else:
                if del_current_node.left.value <= del_current_node.right.value:
                    del_current_node.value = del_current_node.left.value
                    del_current_node = del_current_node.left
                else:
                    del_current_node.value = del_current_node.right.value
                    del_current_node = del_current_node.right
        del_current_node.value = None
        return

    def heapsort(self, N) -> list: # НАПИСАТЬ УДАЛЕНИЕ КОРНЯ N раз (done)
        current_node = self.root
        number_list = current_node.listing()
        numbers = 0
        for i in range(len(number_list)):
            if number_list[i] != None:
                numbers += 1
        if numbers <= N:
            for i in range(numbers):
                self.pop()
        else:
            for i in range(N):
                self.pop()
        return

heap = Heap()

'''first_node = heap.Node(1)
second_node = heap.Node(4)
third_node = heap.Node(3)
quatro_node = heap.Node(1)
cinco_node = heap.Node(2)
seis_node = heap.Node(10)
siete_node = heap.Node(6)
ocho_node = heap.Node(0)

heap.add(first_node)
heap.add(second_node)
heap.add(third_node)
heap.add(quatro_node)
heap.add(cinco_node)
heap.add(seis_node)
heap.add(siete_node)
heap.add(ocho_node)
print(quatro_node.listing())
print(third_node.listing())
print(heap.get_root())'''

heap.add(1)
heap.add(3)
heap.add(15)
heap.add(2)
heap.add(8)
heap.add(10)
heap.add(17)
print(heap.get_root())
heap.heapsort(4)
print(heap.get_root())
heap.pop()
print(heap.get_root())
