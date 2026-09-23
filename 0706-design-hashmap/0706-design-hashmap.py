class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for b in range(self.size)]

    # inserts a (key, value) pair into the HashMap. If the key already exists
    # in the map, update the corresponding value.
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = key, value
                return
        
        bucket.append((key, value))

# returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.size
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key: 
                key, value = bucket[i] 
                return value
        return -1
    
# removes the key and its corresponding value if the map contains the mapping for the key.
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        value = MyHashMap.get(self, key)
        bucket = self.buckets[key % self.size]
        if value != -1:
            bucket.remove((key, value))

                
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)