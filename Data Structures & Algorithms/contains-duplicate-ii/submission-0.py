class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        wind = set()
        
        L = 0

        for R in range(0,len(nums)):

            if R - L  >k:
                wind.remove(nums[L])

                L +=1

            if nums[R] in wind:
                return True

            wind.add(nums[R])    

        return False        