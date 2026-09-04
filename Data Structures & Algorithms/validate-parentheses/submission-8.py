class Solution:
    def isValid(self, s: str) -> bool:
        # print(len(s))
        s_length = len(s)

        opening_bracket = ['(', '{', '[']
        closing_bracket = [')', '}', ']']

        an_open_bracket_exist = False

        # First check if the array size module 2 = 0 
        if s_length % 2 == 1:
            return False
        else:
            search_start_index = 0
            search_end_index = s_length
            s_substring = s[search_start_index:search_end_index]
            s_substring_length = len(s_substring)

            while s_substring_length != 0:
                # print("N_iteration:", N_iteration)
                # print("search_start_index:", search_start_index)
                # print("search_end_index:", search_end_index)
                # print(s[search_start_index:search_end_index])
                # print("lengh:", len(s[search_start_index:search_end_index]))

                si_an_opener = s[search_start_index] in opening_bracket

                # print("Checking for closing bracket...")
                if not si_an_opener and not an_open_bracket_exist:
                    return False
                elif si_an_opener:
                    index_i = opening_bracket.index(s_substring[0])
                    # print("s_substring[0] is index", index_i)
                    target_closing_i = closing_bracket[index_i]

                    if s_substring[1] == target_closing_i:
                        # print('case 1')
                        search_start_index = search_start_index + 2 
                        # search_end_index = search_end_index - 1 
                        has_an_open_bracket = False

                    elif s_substring[-1] == target_closing_i:
                        # print('case 2')
                        # i = i + 1 
                        search_start_index = search_start_index + 1 
                        search_end_index = search_end_index - 1 
                        
                        has_an_open_bracket = False
                    else:
                        # print("No closing bracket found!!!!")
                        return False
                    
                    s_substring = s[search_start_index:search_end_index]
                    s_substring_length = len(s_substring)

                    # print("Adjusting indices to", search_start_index, search_end_index)
                    # print("Adjusting substring length to", s_substring_length)
                    # print()
                    # print()

            return True

          
        