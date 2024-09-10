# Project:Find even and odd numbers from a list, and store them separately in a new list

a=[87,7987697,575487942,879879845,6678764,786578054,1,0,868,999,70,33]
odd_list=[]
even_list=[]
for i in a:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even list are:",even_list)
print("odd list are:",odd_list)