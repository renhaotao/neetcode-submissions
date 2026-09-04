class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        # to char list 
        s_char_list = [a for a in s]
        t_char_list = [a for a in t]

        s_char_list.sort()
        t_char_list.sort()

        for i in range(len(s_char_list)):
            if s_char_list[i] == t_char_list[i]:
                pass
            else:
                return False
        
        return True
    
        