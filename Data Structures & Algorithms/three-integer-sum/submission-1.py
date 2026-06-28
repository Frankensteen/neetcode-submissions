class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array (Mandatory for two-pointer tracking)
        result = []
        n = len(nums)
        
        # Step 2: Fix the first element using an outer loop
        for i in range(n - 2):
            # Optimization: If the lowest number is greater than 0, 
            # three positive numbers can never sum up to 0. Stop early.
            if nums[i] > 0:
                break
                
            # Skip duplicates for the first element to ensure unique triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Initialize the inner two pointers
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for 'left' pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for 'right' pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward after finding a valid match
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Sum is too small; move left pointer rightward to get a larger value
                    left += 1
                else:
                    # Sum is too large; move right pointer leftward to get a smaller value
                    right -= 1
                    
        return result