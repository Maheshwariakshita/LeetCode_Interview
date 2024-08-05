class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort() # or a=sorted(intervals)
        # a=[]

        # if len(intervals)<2:
        #     return intervals
                
        # for i in range(len(intervals)-1):
        #     if intervals[i][1]>=intervals[i+1][0]:
        #         a.append([intervals[i][0], intervals[i+1][1]])
        #     else:
        #         # a.append([intervals[i][0], intervals[i][1]])
        #         # a.append(intervals[i])
        #         a.append(intervals[i+1])
        # return a









        
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # Sort intervals based on the start value
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            previous_interval = merged_intervals[-1]

            if previous_interval[1] >= current_interval[0]:
                # Merge the overlapping intervals
                merged_intervals[-1] = [previous_interval[0], max(previous_interval[1], current_interval[1])]
            else:
                # Add non-overlapping interval to the result
                merged_intervals.append(current_interval)

        return merged_intervals
