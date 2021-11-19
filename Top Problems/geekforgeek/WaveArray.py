class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,arr,N):
        #Your code here
        for i in range(1, N, 2):
            arr[i], arr[i-1] = arr[i-1], arr[i]
    
