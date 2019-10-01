# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # print(key, hash(key))
        # print(key, hash(key))
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # print a warning
        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if self.capacity
        index = self._hash_mod(key)

        if self.storage[index] != None:
            currNode = self.storage[index]
            found = False
            while not found and currNode != None:
                if currNode.key == key:
                    currNode.value = value
                    found = True
                elif currNode.next == None:
                    currNode.next = LinkedPair(key, value)
                    found = True
                else:
                    currNode = currNode.next

        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        value = self.retrieve(key)
        index = self._hash_mod(key)
        if self.storage[index] == None:
            print("No value for that key!")
            return
        # self.storage[index] = None
        currNode = self.storage[index]
        prevNode = None
        while currNode != None:
            # print(currNode.key)
            if currNode.key == key:
                if prevNode:
                    prevNode.next = None
                else:
                    self.storage[index] = None
                currNode = None

            else:
                prevNode = currNode
                currNode = currNode.next
        return value

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        if pair:
            currNode = self.storage[index]
            while currNode != None:
                if currNode.key == key:
                    return currNode.value
                else:
                    currNode = currNode.next
            return None
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # count = self.capacity
        # self.capacity *= 2
        # new_storage = [None] * self.capacity
        # for i in range(count):
        #     new_storage[i] = self.storage[i]
        # self.storage = new_storage

        self.capacity *= 2
        new_storage = [None] * self.capacity
        firstStorage = self.storage
        self.storage = new_storage
        print(self.storage, firstStorage)

        for pair in firstStorage:
            if pair is not None:
                currNode = pair
                while currNode != None:
                    # new_index = self._hash_mod(currNode.key)
                    # new_storage[new_index] = LinkedPair(
                    #     currNode.key, currNode.value)
                    self.insert(currNode.key, currNode.value)
                    currNode = currNode.next

        print(self.storage)
        # self.storage = new_storage


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
# ht = HashTable(8)

# ht.insert("key-0", "val-0")
# ht.insert("key-1", "val-1")
# ht.insert("key-1", "val-12")
# ht.insert("key-2", "val-2")
# ht.insert("key-3", "val-3")
# ht.insert("key-4", "val-4")
# ht.insert("key-5", "val-5")
# ht.insert("key-6", "val-6")
# ht.insert("key-7", "val-7")
# ht.insert("key-8", "val-8")
# ht.insert("key-9", "val-9")
# for i in ht.storage:
#     if i:
#         curr = i
#         while curr != None:
#             print(curr.key, curr.value)
#             curr = curr.next
#         # print(i.key, i.value)
#     else:
#         print(None)
# # # ht.insert("key-1", "val-13")
# # # print(ht.storage)
# return_value = ht.retrieve("key-0")
# print(return_value == "val-0")
# return_value = ht.retrieve("key-1")
# print(return_value == "val-1")
# ht.remove("key-1")
# ht.remove("key-0")
# print(ht.retrieve("key-0"))

ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

ht.insert("key-0", "new-val-0")
ht.insert("key-1", "new-val-1")
ht.insert("key-2", "new-val-2")
ht.insert("key-3", "new-val-3")
ht.insert("key-4", "new-val-4")
ht.insert("key-5", "new-val-5")
ht.insert("key-6", "new-val-6")
ht.insert("key-7", "new-val-7")
ht.insert("key-8", "new-val-8")
ht.insert("key-9", "new-val-9")

return_value = ht.retrieve("key-0")
print(return_value == "new-val-0")
return_value = ht.retrieve("key-1")
print(return_value == "new-val-1")
return_value = ht.retrieve("key-2")
print(return_value == "new-val-2")
return_value = ht.retrieve("key-3")
print(return_value == "new-val-3")
return_value = ht.retrieve("key-4")
print(return_value == "new-val-4")
return_value = ht.retrieve("key-5")
print(return_value == "new-val-5")
return_value = ht.retrieve("key-6")
print(return_value == "new-val-6")
return_value = ht.retrieve("key-7")
print(return_value == "new-val-7")
return_value = ht.retrieve("key-8")
print(return_value == "new-val-8")
return_value = ht.retrieve("key-9")
print(return_value == "new-val-9")

ht.remove("key-1")
ht.remove("key-0")

return_value = ht.retrieve("key-0")
print(return_value)

ht.resize()
