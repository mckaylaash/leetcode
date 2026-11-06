class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}
        for i in range(0, len(strs)):
            sort_word = "".join(sorted(strs[i]))

            if sort_word in group:
                group[sort_word].append(i) # add index
            else: 
                group[sort_word] = [i]

        ret = []
        for key in group:
            ret.append([strs[i] for i in group[key]])
            
        return ret