import time
def binarysearch(a,key):
      low = 0
      high = len (a)-1
      while low<=high:
       mid = (high + low )// 2
       if a[mid]==key:
           return mid
       elif key < a[mid]:
            high=mid-1
       else:
            low=mid+1
            return -1
start = time.time()
a=[13,44,75,25,94,49,75,27,19]
print("the array elements are;",a)
k=int(input("enter the key element to search:"))
r = binarysearch(a,k)
if r==-1:
  print ("search unsuccessful")
else:

    print("search successful key found at location:",r+1)
end=time.time()
print("runtime of the program is:",end-start)
    
  