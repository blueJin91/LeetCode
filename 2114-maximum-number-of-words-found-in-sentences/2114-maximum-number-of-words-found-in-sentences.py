class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length_list = [len(sentence.split()) for sentence in sentences]
        
        return max(length_list)