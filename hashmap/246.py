class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
       
        hashmap = {
                   "0": "0",
                   "1": "1",
                   "8": "8",
                   "6": "9",
                   "9": "6"
                  }
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in hashmap or num[right] != hashmap[num[left]]:  
                return False
            left += 1
            right -= 1
        return True