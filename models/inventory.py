from models.item import Item

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Inventory:
    def __init__(self, capacity=10):
        self.top = None
        self.size = 0
        self.capacity = capacity

    def is_full(self):
        return self.size >= self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.is_full():
            print("Çanta dolu! Önce bir eşya çıkar.")
            return False
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True

    def pop(self):
        if self.is_empty():
            print("Çanta boş!")
            return None
        removed = self.top
        self.top = self.top.next
        self.size -= 1
        return removed.item

    def use_item(self, item_name):
        temp_stack = []
        found = False
        while not self.is_empty():
            item = self.pop()
            if item.name == item_name:
                found = True
                print(f"{item_name} kullanıldı!")
                break
            temp_stack.append(item)
        while temp_stack:
            self.push(temp_stack.pop())
        if not found:
            print(f"{item_name} çantada yok.")

    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        prev = None
        current = self.top
        for _ in range(self.size - index - 1):
            prev = current
            current = current.next
        if prev is None:
            self.top = current.next
        else:
            prev.next = current.next
        self.size -= 1
        return current.item

    def list_items(self):
        items = []
        current = self.top
        while current:
            items.append(current.item)
            current = current.next
        return items[::-1]