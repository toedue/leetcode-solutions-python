class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: #
        result = []
        result2= []

        for i in arr2:
            for j in arr1:
                if j == i:
                    result.append(j)


        for i in arr1:
            if i not in arr2:
                result2.append(i)
        result2.sort()
        result.extend(result2)

        return result

