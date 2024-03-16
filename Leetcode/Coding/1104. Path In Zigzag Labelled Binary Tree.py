import math

class Solution:
    #Python uses banker's rounding - "round half to even". 
    #This is done to avoid rounding errors. However, this rounding is not helpful for rounding numbers
    #So a customized rounding function will be helpful for rounding numbers
    def col_round(self,x):
        frac = x - math.floor(x)
        if frac < 0.5: return math.floor(x)
        return math.ceil(x)

    #Get the Height 
    #Calculate distance from right most end node to the label
    #For[h....0] 
        #Keep finding the parent and divide the distance/2 and use custom round function to round the digits
    def pathInZigZagTree(self, label: int) -> List[int]:
        label_end = 1
        height = 1
        h = 0
        while label > label_end:
            height = height << 1
            label_end = 2*height - 1
            h +=1

        if h%2 == 0:
            right_mostNode = 2*(1<<h)-1
            dist = right_mostNode - label  + 1
            
        else:
            right_mostNode = (1<<h) 
            dist = label - right_mostNode + 1
            
        res_set = []
        for i in range(h,-1,-1):
            if(i%2 == 0):
                label = 2*(1<<i) - 1 - dist + 1
            else:
                label = (1<<i) + -1 + dist 
            res_set += [label]
            
            dist = self.col_round(dist/2)

        return res_set[::-1]
