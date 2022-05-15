#question6

a=int(input("Enter any number: "))
b=int(input("Enter other number : "))
ab_xor=a^b
count=0
while ab_xor:
    count=count+(ab_xor&1)
    ab_xor=ab_xor>>1
print(count)
