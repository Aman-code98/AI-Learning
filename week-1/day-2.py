# name = input("What is your name? ").strip().title()
# age = input("What is your age? ")
# income = int(input("What is your income? "))

# if income < 2000:
#     category = "low income"
#     advice= "Focus on building emergency funds."
# elif income <5000:
#     category = "middle income"
#     advice = 'start investing 20% of your income'
# elif income <15000:
#     category= 'High income'
#     advice = 'diversify into stocks, real estate and business'
# else: 
#     category = "wealthy"
#     advice = 'Consider preserving wealth'

# print('------------------------------------------------')
# print(f'name: {name}')
# print(f'age: {age}')
# print(f'income: {income}')
# print(f'category: {category}')
# print(f'advice: {advice}')
# print('------------------------------------------------')




# 1. Create empty list to store scores
# 2. Ask user for 5 scores, add each to list
# 3. Loop through list
#    - if score >= 90 print A
#    - if score >= 80 print B
#    - if score >= 70 print C
#    - else print Fail
# 4. Print highest, lowest, average

total_scores = []
for i in range(5):
    score = int(input(f"Enter score : "))
    total_scores.append(score)
    if score >=90:
        print("Grade: A")
    elif score >=80:
        print("Grade: B")
    elif score >=70:
        print("Grade: C")
    else:
        print("Grade: Fail")
print(f'highest score :{max(total_scores)}')
print(f'lowest score :{min(total_scores)}')
print(f' average score :{sum(total_scores)/len(total_scores)}')