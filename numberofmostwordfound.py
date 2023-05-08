class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        
        answer  = 0
        for s in sentences:
            temp = s.split(' ')
            answer = max(answer, len(temp))
            
        return answer