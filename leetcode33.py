#Rearrange Spaces Between Words



class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        # Count total spaces in the text
        total_spaces = text.count(' ')
        
        # Extract all words by splitting the text
        words = text.split()
        num_words = len(words)
        
        if num_words == 1:
            # If there's only one word, all spaces go to the end
            return words[0] + ' ' * total_spaces
        else:
            # Distribute spaces evenly between words
            space_between = total_spaces // (num_words - 1)
            extra_spaces = total_spaces % (num_words - 1)
            
            # Join words with the even spaces and add extra spaces at the end
            return (' ' * space_between).join(words) + ' ' * extra_spaces
