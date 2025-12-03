'''
ek array of integer hai List[int] and ek integer hai target which is n

return karna hai two index number jinka sum target ke equal ho

example - 
Input: nums = [3,2,4], target = 6
Output: [1,2] 
explanation - index number 1 pe 2 hai or 2 pe 4 hai to total sum target = 6 horaha hai

Note - code time complexity must/should be less than O(n^2)
'''

# mera solution
'''
pehle to loop chalega array pe 
agar arr[0] > target , to aage badh jao arr[1] ki taraf
(Brute force approach) agar arr[0] < target, then bache hue elements ko add karke dekho for ex- arr[0] + arr[1], arr[0] + arr[2],....
agar arr[0] == target hai to dusra element find karo jiski value 0 ho


par negative number ke liye nahi socha
kyuki
Aapne logical reasoning achi lagayi hai, lekin isme 2 problems hain. Ek problem "logic" mein hai aur dusri "efficiency" mein.

Chaliye ise todte hain:

1. Logic ki Galti (The "Negative Number" Trap) ⚠️
Aapne socha: Agar arr[0] > target, to aage badh jao. Ye tabhi sahi hota agar sare numbers Positive hote. Lekin Question ke constraints dekho:

-10^9 <= nums[i] <= 10^9 (Matlab negative numbers bhi ho sakte hain).

Example:

Target: 2

Array: [5, -3]

Aapke logic se:

5 check kiya.

5 > 2 hai (Target se bada hai).

Aapne 5 ko skip kar diya. Galti!

Asal mein 5 + (-3) = 2 hota hai. 5 ki zaroorat thi!
'''



'''
We will use "FINDING THE MISSING PARTNER" method to solution

Maanlo ki,
target = 9
arr = [11, 15, 2, 7]

jab tum number 11 pe khade ho to tumhe kese pata lagega ki tumhe or konsa number chaiye target laane ke liye - 
target - currentValue = NeededValue
to fir tum dekhoge ki needed value arr me present hai?
agar ha, to dono value ka index number return kardo
agar nahi, to fir aage badho fir same steps follow karo
'''
arr = [3,2,4]
target = 6
# code without hashtable
# time complexity = O(n^2)
'''for i in range(0,len(arr)):
    current = arr[i]
    needed = target - current
    if needed in arr:
        j = arr.index(needed)
        if j != i:
            print([min(i,j),max(i,j)])
            break'''

# code with hash table

def twoSum(arr,target):
    # ek hashtable banayenge value aur index store karne ke liye
    hashtable = {} # value:index formate me hoga isme

    for i,n in enumerate(arr):
        # Step1 - pata karo ki parnter(needed value) kaun hai
        needed = target - n

        # step2 - check karo kya partner already hashtable me hai
        if needed in hashtable:
            return [hashtable[needed],i]
        
        hashtable[n] = i

print(twoSum(arr,target))


'''What enumerate() Does

It adds a counter to an iterable and returns pairs of:

(index, value)


So instead of writing:

i = 0
for item in arr:
    print(i, item)
    i += 1


you simply write:

for i, item in enumerate(arr):
    print(i, item)'''