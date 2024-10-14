import random
class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.list.append(val)
            self.hash[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        else:
            index = self.hash[val]  
            last_element = self.list[-1] 

            self.list[index] = last_element
            self.hash[last_element] = index  
            
            self.list.pop()  
            del self.hash[val]  
            return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()