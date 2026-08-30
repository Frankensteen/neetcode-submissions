class Solution:
    def trap(self, height: List[int]) -> int:
        def ngl(height):
            result = []
            max_so_far = float('-inf')
            for i in range(len(height)):
                result.append(max_so_far)
                max_so_far = max(max_so_far, height[i])
            return result

        def ngr(height):
            result = [0] * len(height)
            max_so_far = float('-inf')
            for i in range(len(height) - 1, -1, -1):
                result[i] = max_so_far
                max_so_far = max(max_so_far, height[i])
            return result

        ngl_result = ngl(height)
        ngr_result = ngr(height)
        trapped = 0
        for i in range(len(height)):
            water_level = min(ngl_result[i], ngr_result[i])
            if water_level > height[i]:
                trapped += water_level - height[i]
        
        return trapped