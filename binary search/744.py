class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left, right = 0, len(letters) - 1
        result = 0
        while left <= right:
            middle = (left + right) // 2
            if letters[middle] > target:
                result = middle
                right = middle - 1                
            else:
                left = middle + 1

        return letters[result]