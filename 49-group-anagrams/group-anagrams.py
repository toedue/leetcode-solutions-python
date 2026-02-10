class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            d["".join(sorted(word))]

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in d:
                d[sorted_word].append(word)
                
        return [val for val in d.values()]
         

