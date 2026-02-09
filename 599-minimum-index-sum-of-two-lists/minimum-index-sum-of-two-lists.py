class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = float(inf)
        index_map = {v: i for i, v in enumerate(list1)}
        my_dict = {}

        for i, val in enumerate(list2):
            if val in index_map:
                s = index_map[val] + i
                minimum = min(minimum , s)
                my_dict[val] = s

        return [k for k, v in my_dict.items() if v == minimum]



