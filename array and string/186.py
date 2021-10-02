class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(ls, left, right):
            while left < right:
                ls[left], ls[right] = ls[right], ls[left]
                left, right = left + 1, right - 1
        def reverse_each_word(ls):
            start, end = 0, 0
            while start < len(ls):
                while end < len(ls) and ls[end] != ' ':
                    end +=1 
                reverse(ls, start, end - 1)
                start = end + 1
                end = start
                
        reverse(s, 0, len(s) - 1)
        reverse_each_word(s)