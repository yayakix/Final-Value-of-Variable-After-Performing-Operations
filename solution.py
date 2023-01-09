class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        count = 0 
        for x in range(len(operations)):
            if operations[x] in ('++X', 'X++'):
                count = count + 1
            elif operations[x] in ('--X', 'X--'):
                count = count - 1
            print(count)
        return count
