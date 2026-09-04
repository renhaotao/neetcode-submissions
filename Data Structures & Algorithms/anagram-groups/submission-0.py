class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        all_dict = []
        for str in strs:

            dict = {}
            for char in str:
                dict[char] = 1 + dict.get(char, 0)

            all_dict.append([dict, str])

        # print(all_dict)
        new_dic = {}
        for i in all_dict[:]:
            dict_i = i[0]
            pos_vec = [ 0 for i in range(26)]

            # print(pos_vec)
            for j in dict_i.keys():
                pos_vec[ord(j)-ord('a')] = dict_i[j]

            # print(dict_i, dict_i.keys())

            # print(tuple(pos_vec))

            new_dic[tuple(pos_vec)] = [i[1]] + new_dic.get(tuple(pos_vec), [])


        # print(len(new_dic))
        # print(new_dic.items())
        return [k[1] for k in new_dic.items()]
