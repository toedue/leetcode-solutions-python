class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #
        d = defaultdict(list)
        for str in strs:
            count = [0] *26
            for char in str:
                count[ord(char)- ord('a')] +=1
            d[tuple(count)].append(str)
        return list(d.values())
