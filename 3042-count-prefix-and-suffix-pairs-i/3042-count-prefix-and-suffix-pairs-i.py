class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n =len(words)
        count =0
        for i in range(n):
            for j in range(1,n):
                if i!=j:
                    wi,wj = words[i] ,words[j]
                    if wj.startswith(wi) and wj.endswith(wi):
                        count+=1
        return count

        