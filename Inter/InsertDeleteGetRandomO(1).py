class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val] # get val index in list
            last = self.nums[-1] # get the value of last index
            self.nums[idx] = last # place "last" on where val is located
            self.pos[last] = idx # update "last"'s index to val's index
            self.nums.pop() # get rid of "last" from it's original spot...it now has a new home elsewhere
            self.pos.pop(val) # pop out val's position value
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()