

def sum13(nums):
  sum = 0
  inside = False
  for i in range(len(nums)):
    if not inside and nums[i] !=13:
      sum = sum + nums[i]
    elif nums[i] ==13 :
      inside = True
    elif inside and nums[i] !=13:
      inside = False
    
  return sum

print(sum13([1,2,2,1]))

