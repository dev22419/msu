sum=0
given_nums=[1,2,3,4,5,6,7,8,9,10]
for i in given_nums:
    sum=sum+i
average=sum/10
print(f'The average of these number is : {average}')

####
sum=0
count=0
while count<5:
    n=float(input('Enter a number : '))
    sum=sum+n
    count=count+1
average=sum/10
print(f'The average of these number is : {average}')
