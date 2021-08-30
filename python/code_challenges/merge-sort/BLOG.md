# Merge Sort

Merge sort is an efficient, general-purpose, and comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.

&nbsp;

## Pseudocode

    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
          DECLARE mid <-- n/2
          DECLARE left <-- arr[0...mid]
          DECLARE right <-- arr[mid...n]
          // sort the left side
          Mergesort(left)
          // sort the right side
          Mergesort(right)
          // merge the sorted left and right sides together
          Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
          set remaining entries in arr to remaining values in right
        else
          set remaining entries in arr to remaining values in left

&nbsp;

## Trace

**Sample Array: [8,4,23,42,16,15]**

### Pass01

![pass01](pictures/pass01.jpg)

&nbsp;

### Pass02

![pass02](pictures/pass02.jpg)

&nbsp;

### Pass03

![pass03](pictures/pass03.jpg)

&nbsp;

### Pass04

![pass04](pictures/pass04.jpg)

&nbsp;

### Pass05

![pass05](pictures/pass05.jpg)

&nbsp;

### Pass06

![pass05](pictures/pass06.jpg)

&nbsp;

### Pass07

![pass05](pictures/pass07.jpg)

&nbsp;

### Pass08

![pass05](pictures/pass08.jpg)

&nbsp;

### Pass09

![pass05](pictures/pass09.jpg)

&nbsp;

### Pass10

![pass05](pictures/pass10.jpg)

&nbsp;

### Pass11

![pass05](pictures/pass11.jpg)

&nbsp;

## Efficency

- **Time: O(n^2)**

  - The basic operation of this algorithm is comparison. This will happen n \* (n-1) number of times…concluding the algorithm to be n squared.

&nbsp;

- **Space: O(1)**

  - No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
