class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(O,C,curr):
            if O==C==0:  #base case
                result.append(curr)
                return
            if O>0:
                generate(O-1,C,curr+'(')
            if O<C:
                generate(O,C-1,curr+')')
        generate(n,n,'')
        return result

S = Solution()
print(S.generateParenthesis(3))





