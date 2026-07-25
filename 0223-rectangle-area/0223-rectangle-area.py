class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)


        overlapping_width = min(ax2, bx2) - max(ax1, bx1)
        if(overlapping_width < 0):
            overlapping_width = 0
        else:
            overlapping_width = max(0, overlapping_width)


        overlapping_height = min(ay2, by2) - max(ay1, by1)
        if(overlapping_height < 0):
            overlapping_height = 0
        else:
            overlapping_height = max(0, overlapping_height)
            
        
        overlap = overlapping_width * overlapping_height

        return areaA + areaB - overlap