class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        endpoint = 0
        meetingroom = 0
        for i in range(len(intervals)):
            if start[i]<end[endpoint]:
                meetingroom += 1
            else:
                endpoint += 1
        return meetingroom
