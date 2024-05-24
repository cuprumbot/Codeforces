cant = int( input() )
nums = input().split()
nums = [int(n) for n in nums]
nums.sort(reverse=True)

debug = False
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
    
    #print("\n\ncaso A")
    score = score + high
    nums.pop(0)

    pos = 0
    endOfHigh = None
    endOfMinusOne = None
    while (pos < len(nums)):
      if (nums[pos] < high):
        if (endOfHigh is None):
          endOfHigh = pos

      if (nums[pos] < minusOne):
        if (endOfMinusOne is None):
          endOfMinusOne = pos
          break
      
      pos = pos + 1

    if (endOfHigh is None):
      first = []
    else:
      first = nums[ :endOfHigh]

    if (endOfMinusOne is None):
      second = []
    else:
      second = nums[endOfMinusOne: ]

    if (endOfHigh is None) and (endOfMinusOne is None):
      first = nums

    if debug:
      print("endOfHigh", endOfHigh)
      print("first", first)
      print("endOfMinusOne", endOfMinusOne)
      print("second", second)
    nums = first + second
    #print(nums)

  else:

    #print("\n\ncaso B")
    score = score + minusOne

    pos = 0
    endOfHigh = None
    endOfMinusOne = None
    endOfMinusTwo = None
    while (pos < len(nums)):
      if (nums[pos] < minusOne):
        if (endOfMinusOne is None):
          endOfMinusOne = pos
      
      if (nums[pos] < high):
        if (endOfHigh is None):
          endOfHigh = pos

      if (nums[pos] < minusTwo):
        if (endOfMinusTwo is None):
          endOfMinusTwo = pos
          break
      
      
      pos = pos + 1

    if (endOfMinusOne is None):
      first = nums[endOfHigh: ]
    else:
      first = nums[endOfHigh:endOfMinusOne]

    if (endOfMinusTwo is None):
      second = []
    else:
      second = nums[endOfMinusTwo: ]

    nums = first + second
    nums.pop(0)
    #print(nums)

print(score)
