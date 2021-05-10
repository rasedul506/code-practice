# heap sort
class heap:
    def __init__(self) -> None:
        pass

    def heapify(self, arr: list, length: int, root: int):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < length and arr[left] > arr[root]:
            largest = left
        if right <length and arr[right] > arr[largest]:
            largest = right
        
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            self.heapify(arr, length, largest)

    def sort(self, arr: list):
        if not arr: return arr
        length = len(arr)

        # max heap
        for i in range(length//2,-1,-1):
            self.heapify(arr, length, i)
        # sort
        for i in range(length-1,0,-1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

    def insert(self, arr: list,n: int):
        if not arr or not n: return arr

        arr.append(n)
        self.sort(arr)

    def delete(self, arr: list, n: str):
        if not arr or not n: return arr

        if n in arr:
            arr.remove(n)
            self.delete(arr, n)
        else:
            self.sort(arr)

test = [1, 12, 9, 30, 6, 20, 5]
heap().sort(test)
print(test)

heap().insert(test, 18)
print(test)

heap().insert(test, 3)
print(test)

heap().insert(test, 6)
print(test)

heap().delete(test, 6)
print(test)
