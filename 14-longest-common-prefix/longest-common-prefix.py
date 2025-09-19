class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]

        # for i in range(len(prefix)):
        #     for word in strs:
        #         if i == len(word) or prefix[i] != word[i]:
        #             return prefix[:i]
        # return prefix

        result = ""
        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]



        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return result
            result +=first[i]
        
        return result 


        