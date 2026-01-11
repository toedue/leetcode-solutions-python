class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #
        idexed_score = [(x,y) for y,x in enumerate(score)]
        output = [""] * len(score)
        sorted_idexed_score = sorted(idexed_score, key = lambda x: x[0], reverse = True)

        for i , (x,y) in enumerate(sorted_idexed_score):   #[(10, 0), (9, 3), (8, 2), (4, 4), (3, 1)]
            if i == 0:
                output[y] = "Gold Medal"
            elif i == 1:
                output[y] = "Silver Medal"
            elif i == 2:
                output[y] = "Bronze Medal"
            else:
                output[y] = str(i+1)

        return output



