# Function to calculate bonus
def calculate_bonus(salary, years):
    
    if years > 10:
        bonus = 0.20 * salary
    elif 5 <= years <= 10:
        bonus = 0.10 * salary
    else:
        bonus = 0.05 * salary
    
    total_salary = salary + bonus
    
    print("Bonus:", bonus)
    print("Total Salary:", total_salary)
    print("----------------------")

# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEmployee {i+1}")
    
    salary = float(input("Enter salary: "))
    years = int(input("Enter years of experience: "))
    
    calculate_bonus(salary, years)