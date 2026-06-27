class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Place pointers at both ends of the sorted array
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Target found! Return 1-based indices
                return [left + 1, right + 1]
            
            elif current_sum < target:
                # The sum is too small; move the left pointer up to increase it
                left += 1
                
            else:
                # The sum is too large; move the right pointer down to decrease it
                right -= 1
                
        return [0, 0]