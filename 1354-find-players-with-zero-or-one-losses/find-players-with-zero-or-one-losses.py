class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[],[]]

        winners=[]
        losers=[]
        dic={}

        for match in matches:
            dic[match[0]] = dic.get(match[0],0) 
            dic[match[1]] = dic.get(match[1],0) +1

        for key in sorted(dic.keys()):
            if dic[key] == 0:
                answer[0].append(key)
            elif dic[key] == 1:
                answer[1].append(key)
        return answer

       
            