class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 0
        left = 0
        for right, symb in enumerate(s):
            if symb not in s[left:right]:
                right += 1
            else:
                while symb in s[left:right]:
                     left += 1
            if len(s[left:right]) > max_lenght:
                max_lenght = len(s[left:right])
        return max_lenght
