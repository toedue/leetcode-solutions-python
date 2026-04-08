class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,1,2,2,3], k = 4
        # [[], [3], [2], [1, 6, 7]]
        #  0   1    2   3
        #  answer = [1, 6, 7, 2]   

        # freq, values, buckets
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]
        print(freq)
        for key, value in freq.items():
            buckets[value].append(key) # value = frequency, key = value

        answer = []
        for i in range(len(buckets) - 1, -1, -1):
            for element in buckets[i]:
                answer.append(element)
                if len(answer) == k:
                    return answer