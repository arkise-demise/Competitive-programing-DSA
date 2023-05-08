class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = []
        for strs in address:
            if strs == '.':
                answer.append('[.]')
            else:
                answer.append(strs)
        
        return ''.join(answer)