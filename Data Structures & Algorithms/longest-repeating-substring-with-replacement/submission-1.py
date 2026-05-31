class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        L = 0
        max_substring = 0
        output = 0

        for R in range(len(s)):

            if s[R] in count:
                count[s[R]] +=1
            else:
                count[s[R]] = 1
            max_substring = max(max_substring,count[s[R]])
            while (R-L+1) - max_substring > k:

                count[s[L]] -=1
                L +=1

            output = max(max_substring, R-L+1)            
        return output