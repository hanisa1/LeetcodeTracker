class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = []
        #create enumerated array
        for i in range(len(nums)):
            value = nums[i]
            arr.append((value, i))
        
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            sum = arr[left][0] + arr[right][0]

            if sum == target:
                return [arr[left][1], arr[right][1]]
            
            if sum > target:
                right -= 1
            else:
                left += 1


        return result

# Time: O(nlogn)
# Space O(n)
