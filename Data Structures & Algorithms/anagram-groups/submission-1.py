class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for word in strs:
            word_dic = dict()
            for char_j in word:
                word_dic[char_j] = 1 + word_dic.get(char_j, 0)

            ana_dict[tuple(sorted(word_dic.items()))].append(word)
            # print(tuple(sorted(word_dic.items())))
            # print(word_dic, set(word_dic.keys()), set(word_dic.items()))

        return list(ana_dict.values())
       
