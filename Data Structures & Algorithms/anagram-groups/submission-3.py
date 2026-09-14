class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for word in strs:
            # word_dic = dict()
            word_list = [0] * 26
            for char_j in word:
                # print(ord(char_j)-ord('a'))
                word_list[ord(char_j)-ord('a')] += 1 
            #     word_dic[char_j] = 1 + word_dic.get(char_j, 0)

            ana_dict[tuple(word_list)].append(word)

            # ana_dict[tuple(sorted(word_dic.items()))].append(word)

        return list(ana_dict.values())
       
