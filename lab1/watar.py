class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_water = max(max_water, area)
        return max_water


"""class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Вычисляем текущую площадь
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_water = max(max_water, area)
            
            # Двигаем указатель с меньшей высотой
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
