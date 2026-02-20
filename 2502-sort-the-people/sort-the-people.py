class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        size = len(heights)
        
        for i in range(size):
            swaped = False
            for j in range(size - 1, 0, -1):
                if heights[j] > heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
                    names[j], names[j-1] = names[j-1], names[j]
                    swaped = True
            if swaped == False: break

        return names