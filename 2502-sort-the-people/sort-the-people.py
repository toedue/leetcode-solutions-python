class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = {}
        sorted_names = []

        for i in range (len(names)):
            name = names[i]
            height = heights[i]
            height_dict[height] = name

        sorted_by_height = dict(sorted(height_dict.items(), reverse = True))

        for value in sorted_by_height.values():
            sorted_names.append(value)

        return sorted_names

            
        