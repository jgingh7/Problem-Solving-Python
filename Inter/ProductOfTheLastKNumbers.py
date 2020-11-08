# https://leetcode.com/problems/product-of-the-last-k-numbers/
# Time: O(1) for both
# Space: O(n) for the extra prodNum array

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prodNums = [1]

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.prodNums = [1]
        else:
            self.prodNums.append(self.prodNums[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prodNums):
            return 0
        return self.prodNums[-1] // self.prodNums[-k - 1]
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)