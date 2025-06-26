class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def check_speed(speed):
            total = 0
            for i in range(len(dist)-1):
                total += ceil(dist[i]/speed)
            total += dist[-1]/speed
            return total

        left = 1
        right = 10 ** 7
        result = -1

        while left <= right:
            speed = left + (right - left) // 2
            if check_speed(speed) <= hour:
                result = speed
                right = speed - 1
            else:
                left = speed + 1
        return result