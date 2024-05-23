cant = int( input() )
texts = input().split()
nums = [int(i) for i in texts]

nums.sort(reverse=True)
# after sorting list should look like this:
# [ 4, ..., 3, ..., 2..., 1, ... ]
# 4s together at the start of the list

taxis = 0

# group of 4 people at the start of the list
# the group needs their own taxi
while (len(nums) > 0) and (nums[0] == 4):
  nums.pop(0)
  taxis = taxis + 1

# group of 3 people at the start of the list...
# ...AND group of 1 person at the end of the list
# together they use a single taxi
while (len(nums) > 0) and (nums[0] == 3) and (nums[-1] == 1):
  nums.pop(0)    # first (3 people)
  nums.pop()     # last (1 person)
  taxis = taxis + 1

# leftover groups of 3 people at the start of the list
# since we ran out of groups of 1 person
# the groups of 3 cannot be paired with anyone
# so each group needs their own taxi
while (len(nums) > 0) and (nums[0] == 3):
  nums.pop(0)
  taxis = taxis + 1

# (we do not care about leftover groups of 1 people yet)


# not we have a list like this
# [ 2, ..., 1, ... ]
# only groups of 2 people and 1 person left
acc = 0                     # empty taxi
for n in nums:
  acc = acc + n             # add some people

  if (acc == 4):            # is the taxi full?
    taxis = taxis + 1       # need another taxi...
    acc = 0                 # ...and that taxi starts empty

if (acc != 0):              # did we end up with a non-empty taxi?
  taxis = taxis + 1         # it counts even if not full

print(taxis)