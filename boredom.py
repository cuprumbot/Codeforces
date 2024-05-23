cant = int( input() )
nums = input().split()
nums = [int(n) for n in nums]
nums.sort(reverse=True)

score = 0

while (len(nums) > 0):
  # take the highest number
  high = nums[0]
  minusOne = high - 1     # we will use this very often, so store the result
  minusTwo = high - 2

  sumHigh = 0
  sumMinusOne = 0
  sumMinusTwo = 0

  for index, n in enumerate(nums):
    if n == high:
      sumHigh = sumHigh + n
    elif n == minusOne:
      sumMinusOne = sumMinusOne + n
    elif n == minusTwo:
      sumMinusTwo = sumMinusTwo + n
    else:
      break                         # we don't care about high-3 onwards

  if (sumHigh + sumMinusTwo > sumMinusOne):
    
    score = score + high
    nums.pop(0)

    pos = 0
    while (pos < len(nums)):
      if (nums[pos] == minusOne):
        nums.pop(pos)
      elif (nums[pos] < minusOne):
        break
      else:
        pos = pos + 1

  else:

    score = score + minusOne
    needToPop = True

    pos = 0
    while (pos < len(nums)):
      if (nums[pos] == high):
        nums.pop(pos)
      elif (nums[pos] == minusTwo):
        nums.pop(pos)
      elif (nums[pos] == minusOne) and needToPop:
        nums.pop(pos)
        needToPop = False
      elif (nums[pos] < minusTwo):
        break
      else:
        pos = pos + 1

print(score)

