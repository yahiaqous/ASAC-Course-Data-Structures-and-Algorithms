# Merge Sort

## Code Challenge 27

### **Feature Tasks**

- Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

      ALGORITHM QuickSort(arr, left, right)
          if left < right
              // Partition the array by setting the position of the pivot value
              DEFINE position <-- Partition(arr, left, right)
              // Sort the left
              QuickSort(arr, left, position - 1)
              // Sort the right
              QuickSort(arr, position + 1, right)

      ALGORITHM Partition(arr, left, right)
          // set a pivot value as a point of reference
          DEFINE pivot <-- arr[right]
          // create a variable to track the largest index of numbers lower than the defined pivot
          DEFINE low <-- left - 1
          for i <- left to right do
              if arr[i] <= pivot
                  low++
                  Swap(arr, i, low)

          // place the value of the pivot location in the middle.
          // all numbers smaller than the pivot are on the left, larger on the right.
          Swap(arr, right, low + 1)
          // return the pivot index point
          return low + 1

      ALGORITHM Swap(arr, i, low)
          DEFINE temp;
          temp <-- arr[i]
          arr[i] <-- arr[low]
          arr[low] <-- temp

- Provide a visual step through for each of the sample arrays based on the provided pseudo code

- Convert the pseudo-code into working code in your language

- Present a complete set of working tests

&nbsp;

### **Whiteboard Process**

![CC28](pictures/CC28.jpg)

&nbsp;

### **PR Link**

<https://github.com/YAHIAQOUS/data-structures-and-algorithms/pull/53>
