def remove(list):
   position=3-1
   index=0
   len_list(len(list))
   while len_list>0:
     index=(position+index)%len_list
     print(int_list.pop(index))
     len_list-=1
 nums=[10,20,30,40,70]
 remove(nums)
