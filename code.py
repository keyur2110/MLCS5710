#Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #sort function to sort list
max=max(ages) #max function to find max from list
min = min(ages) #min function to find min from list
print("1) list={}, max={}, min={}".format(ages,max,min))

ages.append(max) #Append the max to the list again
ages.append(min) #Append the min to the list again
print("2) list with max and min:{}".format(ages))

#function to find the median 
def median(nums): 
    nums.sort()
    n = len(nums)
    m = n // 2
    if n % 2 == 0:
        return (nums[m - 1] + nums[m]) / 2
    else:
        return nums[m]

print("3) median:{}".format(median(ages)))

#function to find average
def avg(nums):
    sum = 0
    n = len(nums)
    for i in nums:
        sum=sum+i
    return sum/n
print("4) average:{}".format(avg(ages)))

#function to find range of the list
def ran(nums):
    return max-min
print("5) range:{}".format(ran(ages)))

#Question 2
dog = {} #empty dictionary
dog = {"name": "puppy", "color":"black", "breed":"bulldog", "legs":"4", "age":"5"}
print(dog)

student = {"first_name":"keyur", "last_name":"patel", "gender":"male", "age":"25", "marital status":"single",
"skills":["Leadership","communications"], "country":"usa", "city":"kansas","address":"lee sumit"}
print(student)
print("\nlength of student dict: {}".format(len(student))) #len() funtion to get length of the dictionary


print("\nvalues of skills: {}".format(student['skills'])) # printing the values of key skills
print("\nType of skills: {}".format(type(student.get("skills")))) # checking the type of skills

student['skills'].append('Critical thinking') #Adding the new value to skills
print("\nstudent after adding new values to skills:")
print(student)

k = student.keys() #keys() function to get keys of dictionary
print("\n {}".format(k))

v = student.values() #values() function to get values of dictionary
print("\n {}".format(v))

brothers = ("rutal","savan") 
sisters = ("kirti","devu")
siblings = brothers + sisters # combining two tuples into siblings
print(siblings)
print(f'length of tuple siblings: {len(siblings)}') # len() function to get length of tuples

family_members = siblings + ('dharmesh','nayana') # adding two new values to siblings and creating new tuple
print(family_members)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'length of the set:{len(it_companies)}\n') #len() function to get length of set
it_companies.add('twitter') #adding the new value to the set
print(it_companies)
it_companies.update(['salesforce','giveo']) #adding multiple values to the set
print(it_companies)
it_companies.remove('IBM') #removing item from set
print(it_companies)

'''remove() will give an error if element is not in the set and discard will not give any error if the elemtent is not in the set '''

print(f'A Join B: {A.union(B)}') # A join B
print(f'A intersection B: {A.intersection(B)}') # A intersection B
print(f'A is subset of B ? {A.issubset(B)}') # checking if A is subset of B
print(f'A and B are disjoint sets ? {A.isdisjoint(B)}') #checking if A and B are disjoint
print(f'Join A with B :{A.union(B)}') #union function to join A with B
print(f'JOin B with A : {B.union(A)}') #union function to join B with A
print(f'symmetric difference between A and B: {A.symmetric_difference(B)}')
del A #deleting set A
del B #deleting set B
print("set age:{}".format(set(age))) #conveting age list to set
print(len(set(age)) == len(age)) #comparing the length of set and list

radius = 30 #radius of circle 30
_area_of_circle = 3.14*radius*radius #computing area of a circle PI*r*r
print(f'Area of circle: {_area_of_circle}')

_circum_of_circle_ = 2*3.14*radius #computing circumference of a circle 2*PI*r
print(f'circumference of a circle: { _circum_of_circle_}')

r = int(input("enter the radius of a circle:")) #getting input from user for radius
area = 3.14*r*r #computing area with user input
print(f'Area of a circle with user input {area}')

#question 6
s = "I am a teacher and I love to inspire and teach people"
print("unique words in s: {} \n".format(len(set(s.split())))) #using split function to split string and converting into set to get unique words

#question 7
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki\n") #tab escape sequence to print in specific format

#question 8
print(f'\nradius = {10}')
print(f'area = {3.14} * radius ** {2}')
print(f'The area of a circle with radius {10} is {314} meters square.')

lst = [] #empty list
print("enter 5 weight in lbs:")
for i in range(0, 5): #for loop to get input from user
    ele = float(input())
  
    lst.append(ele) #Appending element to list
print(f'List of weight in lbs: {lst}')

lst1 = []
for i in range(0,len(lst)): #for loop to convert lbs into kgs
    kg = lst[i]*0.453592
    lst1.append(kg)
print(f' List of weight in kgs: {lst1}')