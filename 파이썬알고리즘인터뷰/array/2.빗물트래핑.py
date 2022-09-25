class Solution:
    def trap(self, height: list[int]) -> int:

        # 1. 투포인터
        left, right = 0, len(height) - 1

        water = 0
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max = max(height[left], l_max)
            r_max = max(height[right], r_max)

            if l_max <= r_max:
                water += (l_max - height[left])
                left += 1
            else:
                water += (r_max - height[right])
                right -= 1
        return water

        # 2. 스택
        stack = []
        water = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                water += (distance * waters)

            stack.append(i)
        return water