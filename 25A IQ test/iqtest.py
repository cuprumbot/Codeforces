cant = int( input() )
nums = input().split()
nums = [int(n) for n in nums]

evenness = None

# first two are both even or odd
if (nums[0] % 2 == 0) == (nums[1] % 2 == 0):
  evenness = (nums[0] % 2 == 0)
  # start from the third element
  for pos in range(2, cant):
    # is that element of different evenness?
    # if it is, report it
    if (nums[pos] % 2 == 0) != evenness:
      print(pos + 1)

# the first two were different
else:
  # if the first is equal to the third...
  # ...the second one is reported
  if (nums[0] % 2 == 0) == (nums[2] % 2 == 0):
    print(2)
  # if the second is equal to the third...
  # ...the first one is reported
  elif (nums[1] % 2 == 0) == (nums[2] % 2 == 0):
    print(1)