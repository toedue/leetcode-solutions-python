class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = float(inf)

        my_dict = {}
        result= []

        for i in range(len(list2)):
            if list2[i] in list1:
                index = list1.index(list2[i])
                minimum = min(minimum , (index+i))
                my_dict[list2[i]] = (index+i)

        for k, v in my_dict.items():
            if v == minimum:
                result.append(k)

        return result


