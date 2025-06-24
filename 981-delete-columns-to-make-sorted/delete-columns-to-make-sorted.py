class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n= len(strs[0])
        columns=[[] for x in range(n)]
        for i in range (n):
            for s in strs:
                columns[i].append(s[i])


        counter =0

        for column in columns:
            if (sorted(column) != column):
                counter+=1
        return counter

