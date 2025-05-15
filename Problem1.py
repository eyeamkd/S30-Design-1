""" 
Time Complexity: 
firstHashFunction - O(1)
secondHashFuntion - O(1)

add - O(1)
remove - O(1)
contains - O(1)

Space Complexity: 
firstHashFunction - O(1)
secondHashFuntion - O(1)

add - O(n)
remove - O(1)
contains - O(1)

Approach:
- Use a hash matrix to store the keys
- Use two hash functions to map the key to an index in the hash matrix
- If the key already exists, update the value
- If the key does not exist, add the key-value pair to the hash matrix

"""

class MyHashSet:
    
    def firstHashFunction(self, item):
        return item%1000
    
    def secondHashFunction(self, item):
        return item//1000

    def __init__(self):
        self.hashMatrix = [ None for x in range(1000)]

    def add(self, key: int) -> None:
        idx1 = self.firstHashFunction(key)
        if not self.hashMatrix[idx1]:
            self.hashMatrix[idx1] = [False for i in range(1001)]
        idx2 = self.secondHashFunction(key)
        self.hashMatrix[idx1][idx2] = True

            

    def remove(self, key: int) -> None:
        idx1 = self.firstHashFunction(key)
        if self.hashMatrix[idx1]:
            idx2 = self.secondHashFunction(key)
            if self.hashMatrix[idx1][idx2]:
                self.hashMatrix[idx1][idx2]=False
        return 
        
            
    def contains(self, key: int) -> bool:
        idx1 = self.firstHashFunction(key)
        if self.hashMatrix[idx1]:
            idx2 = self.secondHashFunction(key)
            if self.hashMatrix[idx1][idx2]:
                return self.hashMatrix[idx1][idx2]

        return False


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)