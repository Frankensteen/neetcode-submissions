class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Map each value to its LAST seen index to prevent self-matching
        lookup = {num: i for i, num in enumerate(nums)}
        
        # Use a set to automatically filter out duplicate triplets
        unique_triplets = set()
        n = len(nums)
        
        # O(N^2) Nested loops to pick the first two numbers
        for i in range(n):
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])
                
                # Check if complement exists and its index is not i or j
                if complement in lookup and lookup[complement] > j:
                    # Sort the triplet before turning it into a tuple 
                    # This ensures [-1, 0, 1] and [1, 0, -1] are seen as identical
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    unique_triplets.add(triplet)
                    
        # Convert the set of tuples back into a list of lists
        return [list(t) for t in unique_triplets]