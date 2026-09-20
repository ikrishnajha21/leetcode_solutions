class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for i,char in enumerate(s):
            rev_alpha_index = 26 - (ord(char)-ord('a'))
            string_value= i + 1
            total_degree += rev_alpha_index*string_value
        return total_degree        