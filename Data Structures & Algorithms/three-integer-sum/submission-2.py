class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            # two sum
            l, r = i + 1, len(nums) - 1 
            while l < r:
                triplet_sum = val + nums[l] + nums[r]

                if triplet_sum > 0:
                    r-=1
                elif triplet_sum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    # ensure no duplicate sum
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res