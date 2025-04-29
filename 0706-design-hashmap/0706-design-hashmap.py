class Node:
    def __init__(self,key=0,value=0,next = None):
        self.key = key
        self.value =value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.dict = [Node(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.dict)
        cur = self.dict[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next   
        cur.next = Node(key,value,None)

    def get(self, key: int) -> int:
        index = key % len(self.dict)
        cur = self.dict[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.dict)
        cur = self.dict[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)