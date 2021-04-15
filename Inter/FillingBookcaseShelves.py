# https://leetcode.com/problems/filling-bookcase-shelves/
# Time: O(n^2)
# Time: O(n)

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)] # if i is the index of dp, minimum height when using books[:i]
        dp[0] = 0
        
        for i in range(1, n + 1): # goes over each book
            left_width = shelf_width
            max_height = 0
            j = i - 1
            
            #below while loop is basically keep adding on books to the newly checked book, because adding on before books were all done already before
            while j >= 0 and left_width - books[j][0] >= 0: # if there are still books to check and the width of next book to check is within left_width
                left_width -= books[j][0]
                max_height = max(max_height, books[j][1]) # gets the maximum height of books in books[:i]
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1 # next book
                
        return dp[-1]