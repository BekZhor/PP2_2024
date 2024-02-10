def spy_game(nums):
    y=0
    for i in range(len(nums)):
        if nums[i]==0 :
            y+=1
            continue

        if y==1 and nums[i]==0:
            y+=1
            continue
        
        if y==2 and nums[i]==7:
            y+=1
            print("True")
            break
    if y!=3:
        print ("False")

        

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 