# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
item_dict_ordered=OrderedDict()
n=int(input())
for i in range(n):
    item , price =input().strip().rsplit(' ',1)
    price=int(price)
    
    if item in item_dict_ordered:
        item_dict_ordered[item]+=price
    else:
        item_dict_ordered[item]=price
for item , price in item_dict_ordered.items():
    print (item , price ) 

    
    
