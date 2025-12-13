class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = sum(arr[:k])
        counter = 0
        for i in range(k,len(arr)):
            avg = summ/k
            if avg >= threshold:
                counter += 1
            summ = summ + arr[i] - arr[(i-k)]
        
        avg = summ/k
        if avg >= threshold:
                counter += 1

        
        return counter

            