class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        if len(s1) > len(s2):
            return False

        L = 0
        s1_count = {}
        window_count = {}

        for char in s1:

            s1_count[char] = s1_count.get(char,0) + 1

        for R in range(len(s2)):

            window_count[s2[R]] = window_count.get(s2[R],0) + 1

            if R-L+1 > len(s1):
                window_count[s2[L]] -= 1

                if window_count[s2[L]] ==0:
                    del window_count[s2[L]]

                L += 1                        

            if window_count == s1_count:
                return True              
        return False