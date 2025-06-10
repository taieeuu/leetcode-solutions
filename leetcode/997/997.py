class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_score = {i: 0 for i in range(1, n+1)}
        
        for a, b in trust:
            if a in trust_score:
                trust_score[a] -= 1
            if b in trust_score:
                trust_score[b] += 1

        for person, score in trust_score.items():
            if score == n-1:
                return person
        return -1
        