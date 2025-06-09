class Solution:
		# Simulation
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_dict = {val: idx for idx, val in enumerate(order)}
        
        def compare(word1, word2):
            for x, y in zip(word1, word2):
                if x != y:
                    return order_dict[x] < order_dict[y]
            return len(word1) <= len(word2)

        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        return True
