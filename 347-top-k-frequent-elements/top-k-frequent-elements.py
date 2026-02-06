class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums)
        sorted_store = sorted(store.items(),key = lambda x:x[1], reverse= True)
        # output = []
        # for i in range(k):
        #     output.append(sorted_store[i][0])
        # return output

        return [key for key, val in sorted_store[:k]]