class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = { i:[] for i in range(numCourses)}
        visitedCourse = set()
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)
        print(courseMap)
        
        def helper(crs):
            if crs in visitedCourse:
                return False
            if not courseMap[crs]:
                return True
            
            visitedCourse.add(crs)
            for pre in courseMap[crs]:
                if not helper(pre):
                    return False
            visitedCourse.remove(crs)
            courseMap[crs] = []
            
            return True
        
        for crs in range(numCourses):
            if not helper(crs):
                return False
        return True
