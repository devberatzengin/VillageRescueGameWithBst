class QueueNode:
    def __init__(self, village):
        self.village = village
        self.next = None

class VillageQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, village):
        new_node = QueueNode(village)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed.village

    def peek(self):
        return self.front.village if self.front else None

    def list_villages(self):
        result = []
        current = self.front
        while current:
            result.append(current.village)
            current = current.next
        return result