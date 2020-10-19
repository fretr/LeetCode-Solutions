class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initialize left and right indices, as well as max water
        left_idx = 0
        right_idx = len(height) - 1
        max_water = 0

        # while our left and right indices aren't the same ...
        while left_idx < right_idx:

            # calculate water amount
            water_value = (right_idx - left_idx) * min(height[left_idx], height[right_idx])

            # make this our max water amount if it's greater than previous maxes
            if (right_idx - left_idx) * min(height[left_idx], height[right_idx]) > max_water:
                max_water = water_value

            # move the index with the smaller height value inward
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return max_water

            
