class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        output = 0
        current_sum = 0
        required_sum = k*threshold
        for R in range(len(arr)):

            current_sum += arr[R]

            if R - L +1 == k:

                if current_sum >= required_sum:

                    output += 1
            
                current_sum -= arr[L]
                L += 1

        return output    


            

