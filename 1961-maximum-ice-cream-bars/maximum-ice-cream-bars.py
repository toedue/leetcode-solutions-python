class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter = 0
        i =0

        while costs[i] <= coins:
            coins -= costs[i]
            i+=1
            counter +=1
            if i == len(costs):
                break
        return counter
