class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        point = 0
        points = []
        points.insert(0,point)

        for i in gain:
            point += i
            points.append(point)
        
        points.sort()

        return points[-1]
