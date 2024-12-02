class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate through the words and check for the prefix
        for index, word in enumerate(words):
            if word.startswith(searchWord):
                return index + 1  # Return 1-indexed position
        
        # If no word starts with the searchWord, return -1
        return -1
