class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % len(self.data_map)
