import csv
import matplotlib.pyplot as plt

print('this is a test')
print('still testing')

# Initialize a list for our data
data = []

# Open csv and add data to list
with open('insurance.csv', 'r') as insurance_csv:
    csv_read = csv.reader(insurance_csv)

    header = next(csv_read) 
    # print("Header:", header)

    for row in csv_read:
        data.append(row)

# Create a list of each column of csv
ages = [int(row[0]) for row in data]
sexes = [row[1] for row in data]
bmis = [float(row[2]) for row in data]
number_of_children = [int(row[3]) for row in data]
smoking_status = [row[4] for row in data]
regions = [row[5] for row in data]
medical_costs = [float(row[6]) for row in data]

# Initialize counters for age groups
ages_under_25 = 0
ages_25_to_50 = 0
ages_50_to_75 = 0
ages_75_and_above = 0

# Loop through the ages and classify

for age in ages:
    if age < 25:
        ages_under_25 += 1
    elif 25 <= age < 50:
        ages_25_to_50 += 1
    else:
        ages_50_to_75 += 1

# # Print the results
# print("Number of Customers by Age Group:")
# print(f"Under 25: {ages_under_25}")
# print(f"25 to 50: {ages_25_to_50}")
# print(f"50 to 75: {ages_50_to_75}")

# # Data for visualization
# age_groups = ['Under 25', '25-50', '50-75']
# customer_counts = [ages_under_25, ages_25_to_50, ages_50_to_75]

# # Create the bar chart
# plt.bar(age_groups, customer_counts, color='blue')

# # Add title and labels
# plt.title('Number of Customers by Age Group')
# plt.xlabel('Age Group')
# plt.ylabel('Number of Customers')

# # Show the plot
# plt.show()


# Calculating Average Costs | Smoking Status
smoker_costs = []
non_smoker_costs = []

for row in data:
    smoker_status = row[4]
    cost = float(row[6])
    
    if smoker_status == "yes":
        smoker_costs.append(cost)
    else:
        non_smoker_costs.append(cost)

average_smoker_cost = sum(smoker_costs) / len(smoker_costs)
average_non_smoker_cost = sum(non_smoker_costs) / len(non_smoker_costs)
#future opportunities for statistical analysis once pandas is available to determine if there is a statistically significant difference

print("_________________________________________________________________")
print("Average Cost by Smoking Status:")
print(f"Average Insurance Cost for Smokers: ${average_smoker_cost:.2f}")
print(f"Average Insurance Cost for Non-Smokers: ${average_non_smoker_cost:.2f}")

# Calculating Average Costs | Sex
male_costs = []
female_costs = []

for row in data:
    sex = row[1]
    cost = float(row[6])
    if sex == 'male':
        male_costs.append(cost)
    else:
        female_costs.append(cost)

avg_male_costs = sum(male_costs) / len(male_costs) if male_costs else 0
avg_female_costs = sum(female_costs) / len(female_costs) if female_costs else 0

print("_________________________________________________________________")
print("Average Cost by Sex:")
print(f"Male Average Cost: ${avg_male_costs:.2f}")
print(f"Female Average Cost: ${avg_female_costs:.2f}")

# Calculating Average Costs | Age Group
costs_by_age_group = {"0-25": [],
    "25-50": [],
    "50-75": []}

for row in data:
    age = int(row[0])
    costs = float(row[6])

    if age < 25:
        costs_by_age_group["0-25"].append(costs)
    elif age >= 25 and age < 50:
        costs_by_age_group["25-50"].append(costs)
    elif age > 50:
        costs_by_age_group["50-75"].append(costs)
    
print("_________________________________________________________________")
for age_group, costs in sorted(costs_by_age_group.items()):
    avg_cost = sum(costs) / len(costs) if costs else 0
    if len(costs) == 1:
        print(f"Average Medical Cost for {age_group}: ${avg_cost:.2f} (1 person)")
    else:
        print(f"Average Medical Cost for {age_group}: ${avg_cost:.2f} ({len(costs)} people)")

# Calculating Average Costs | Number of Children
costs_by_children = {}

for row in data:
    num_children = int(row[3])
    cost = float(row[6])

    if num_children not in costs_by_children: # Adds number of children if not in the dictionary already
        costs_by_children[num_children] = []
    
    costs_by_children[num_children].append(cost)

print("_________________________________________________________________")
print("Average Cost by Number of Children:")
for num_children, costs in sorted(costs_by_children.items()):
    avg_cost = sum(costs) / len(costs)
    if num_children == 1:
        print(f"Average Medical Cost for {num_children} Child: ${avg_cost:.2f}")
    else:
        print(f"Average Medical Cost for {num_children} Children: ${avg_cost:.2f}")


# Calculating Average Costs | BMI
underweight = []
normal = []
overweight = []
obese = []

for row in data:
    bmi = float(row[2])
    cost = float(row[6])

    if bmi < 18.5:
        underweight.append(cost)
    elif 18.5 <= bmi < 25:
        normal.append(cost)
    elif 25 <= bmi < 30:
        overweight.append(cost)
    else:
        obese.append(cost)

avgcost_underweight = sum(underweight) / len(underweight) if underweight else 0
avgcost_normal = sum(normal) / len(normal) if normal else 0
avgcost_overweight = sum(overweight) / len(overweight) if overweight else 0
avgcost_obese = sum(obese) / len(obese) if obese else 0

print("_________________________________________________________________")
print("Average Cost by BMI:")
print(f"Underweight BMI Avg Cost: ${avgcost_underweight:.2f}")
print(f"Normal BMI Avg Cost: ${avgcost_normal:.2f}")
print(f"Overweight BMI Avg Cost: ${avgcost_overweight:.2f}")
print(f"Obese BMI Avg Cost: ${avgcost_obese:.2f}")
print("_________________________________________________________________")

