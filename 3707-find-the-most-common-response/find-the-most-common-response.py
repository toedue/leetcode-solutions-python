from collections import Counter

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        for i in range(len(responses)):
            temp_set = set(responses[i])
            responses[i] = list(temp_set)

        flat_list = [response for row in responses for response in row]
        d = Counter(flat_list)

        sorted_items = sorted(d.items(), key= lambda x: (-x[1], x[0]))

        return sorted_items[0][0]