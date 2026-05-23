name = input("What is your name? ").strip().title()
age = input("What is your age? ")
income = int(input("What is your income? "))

if income < 2000:
    category = "low income"
    advice= "Focus on building emergency funds."
elif income <5000:
    category = "middle income"
    advice = 'start investing 20% of your income'
elif income <15000:
    category= 'High income'
    advice = 'diversify into stocks, real estate and business'
else: 
    category = "wealthy"
    advice = 'Consider preserving wealth'

print('------------------------------------------------')
print(f'name: {name}')
print(f'age: {age}')
print(f'income: {income}')
print(f'category: {category}')
print(f'advice: {advice}')
print('------------------------------------------------')