def twoSum(nums, target):
    l=[]
    m=[]
    k=[]
    output =[]
    for i in range(len(nums)):
        if nums[i]<=target:
            l.append(nums[i])
    print(l)
    for i in range(len(l)):
        if max(l)==target:
            k.append(i)
            break
        elif max(l)<=target:
                m.append(max(l))
                final_num=target-max(m)
                if final_num == l[i]:
                    m.append(l[i])
                    m.sort()
                    break
    print(m)
    for num in range(len(nums)):
        for j in range(len(m)):
            if m[j]==nums[num]:
                k.append(nums[num])
    print(k)
    for i in range(len(k)):
        output.append(i)
        # return output
        print(output)

a=twoSum(nums =[3,2,4],target = 6)
a


