# Chapter1 
## 1.1 python快排
```python
def quicksort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[int(len(arr)/2)]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,58,9,1,1,4,7,8,9]))
```
