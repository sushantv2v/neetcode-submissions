class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        uniq_char = set()
        L = 0
        max_string = 0

        for R in range(0,len(s)):

            while s[R] in uniq_char:

                uniq_char.remove(s[L])
                L += 1

            uniq_char.add(s[R])
            max_string = max(max_string, len(s[L:R+1]))     
        return max_string



        