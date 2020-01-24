from LinkedLists.SortedLinkedList import SortedLinkedList


class HashTable:
    def  __init__(self, tableSize):
        self.m = tableSize
        self.array = [SortedLinkedList()] * self.m
        self.n = 0

    def hash(self, key):
        return key % self.m

    def display_table(self):
        for i in range(self.m):
            print("[",i, "] --> ",end='')
            if self.array[i] is not None:
                self.array[i].display_list()
            else:
                print("___")

    def search(self,key):
        h = self.hash(key)
        if self.array[h] is not None:
            return self.array[h].search(key)
        return None

    def insert(self, newRecord):
        h = self.hash(newRecord)
        if self.array[h] is None:
            self.array[h] = SortedLinkedList()
            self.array[h].insert(newRecord)
        self.n += 1

    def delete(self, key):
        h = self.hash(key)
        if self.array[h] is not None:
            self.array[h].delete_node(key)
            self.n += 1
        else:
            return False
