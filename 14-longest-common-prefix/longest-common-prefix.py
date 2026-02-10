class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # lexicographical sort
        strs.sort()

        first = strs[0]
        last = strs[-1]
        arr =[]

        # edge case: empty list
        if not strs:
            return ""

        # edge case: if any string is empty
        if "" in strs:
            return ""

        for i , j in zip(first, last):
            if i == j:
                arr.append(i)
            else:
                break

        return "".join(arr)

        