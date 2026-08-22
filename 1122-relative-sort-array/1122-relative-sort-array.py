class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = {}
        #count the freq in arr1
        for num in arr1:
            if num not in count:
                count[num]=0
            count[num]+=1

        result=[]    

        #bring in arr2 order
        for num in arr2:
            for i in range(count[num]):
                result.append(num)
            del count[num]

        #remaining elements
        remaining = []
        for num in count:
            for i in range(count[num]):
                remaining.append(num)

        remaining.sort()
        result.extend(remaining)
        return result                
        