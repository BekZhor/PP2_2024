def has_33(nums):
    y=0
    for i in range(len(nums)):
        if i==len(nums)-1:
            break
        if nums[i]==3 and nums[i+1]==3:
            y=y+1
            break
    
    if y>0:
        print("True")
    else:
        print("False")

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3])
has_33([3, 1, 3]) 