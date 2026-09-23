class MyHashSet(object):

    def __init__(self, size = 1000):
        self.size = size
        self.buckets = [[] for b in range(size)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size 
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = key % self.size
        return key in self.buckets[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)