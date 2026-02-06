class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        output = []
        for word in strs:
            store["".join(sorted(word))].append(word)
        for v in store.values():
            output.append(v)
        return output