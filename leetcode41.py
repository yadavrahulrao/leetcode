#Sort the People


class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Pair up names and heights, sort by height in descending order
        sorted_people = sorted(zip(heights, names), reverse=True)
        # Extract and return just the names from the sorted list
        return [name for height, name in sorted_people]
