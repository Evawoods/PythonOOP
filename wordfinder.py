"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from a dictionary
    >>> wf_test = WordFinder(path = 'words.txt')
    235886 words read
    """
    def __init__(self, path):
        """Read dictonary and reports num of items read"""
    
        dict_file = open(path)

        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file to list of words"""
        return [word.strip() for word in dict_file]
    
    def random(self):
        """Return a random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized word finder that ignores comments and empty liens
    >>> swf_test = SpecialWordFiner(path= 'words2.txt')
    4 words read

    >>> swf_test.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """

    def parse(self, dict_file):
        """Parse dict_file to list of words not containing blank lines or comments"""
        return [word.strip() for word in dict_file if word.strip() and not word.startswith('#')]