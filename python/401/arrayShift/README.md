# Challenge Title

Array-insert-shift

## Whiteboard Process

![arrayShift](/401/arrayShift/arrayShift.jpg)

## Approach & Efficiency

Time: O(n)
Space: O(1)

## Solution

      def insertShiftArray(arr, num):
          arrLen = len(arr)
          if arrLen %2 ==0:
                evenVar = arrLen / 2
            arr.insert(evenVar, num)
            else:
            oddVar = (arrLen/2) +1
            arr.insert(oddVar, num)

## contribution

Slava Makeev,
