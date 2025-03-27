import csv

class MedicalCostAnalyzer:
    def __init__(self, filename):
        """Initialize the class by reading data from a CSV file."""
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Reads CSV data into a list of lists."""
        with open(self.filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            return [row for row in csv_reader]

    def __str__(self):
        """User-friendly preview of data."""
        preview = "\n".join([", ".join(row) for row in self.data[:5]])
        return f"MedicalCostAnalyzer Data Preview (First 5 rows):\n{preview}"
    
    def average_cost_by_age_group(self):
        """Calculates average cost per age group."""
        age_groups = {
            "Under 25": [],
            "25-50": [],
            "50-75": []
        }

        for row in self.data:
            age = int(row[0])
            cost = float(row[6])

            if age < 25:
                age_groups["Under 25"].append(cost)
            elif 25 <= age <= 50:
                age_groups["25-50"].append(cost)
            else:
                age_groups["50-75"].append(cost)

        return {group: round((sum(costs) / len(costs) if costs else 0), 2) for group, costs in age_groups.items()}

    def average_cost_by_children(self):
        """Calculates average cost based on number of children."""
        costs_by_children = {}

        for row in self.data:
            num_children = int(row[3])
            cost = float(row[6])

            if num_children not in costs_by_children:
                costs_by_children[num_children] = []
            
            costs_by_children[num_children].append(cost)

        return {children: round(sum(costs) / len(costs), 2) for children, costs in costs_by_children.items()}

    def average_cost_by_smoking_status(self):
        """Calculates average cost based on smomking status."""
        smoker_costs = []
        non_smoker_costs = []

        for row in self.data:
            smoker_status = row[4]
            cost = float(row[6])
            
            if smoker_status.lower() == "yes":
                smoker_costs.append(cost)
            else:
                non_smoker_costs.append(cost)

        average_smoker_cost = round(sum(smoker_costs) / len(smoker_costs), 2) if smoker_costs else 0
        average_non_smoker_cost = round(sum(non_smoker_costs) / len(non_smoker_costs), 2) if non_smoker_costs else 0

        return {'Average cost for smokers': average_smoker_cost, 'Average cost for nonsmokers': average_non_smoker_cost}

    def average_cost_by_BMI(self):
        """Calculates average cost based on BMI."""
        bmi_categories = {
        "Underweight": [],
        "Normal weight": [],
        "Overweight": [],
        "Obese": []
    }

        for row in self.data:
            bmi = float(row[2])
            cost = float(row[6])

            if bmi < 18.5:
                bmi_categories["Underweight"].append(cost)
            elif 18.5 <= bmi < 24.9:
                bmi_categories["Normal weight"].append(cost)
            elif 25 <= bmi < 29.9:
                bmi_categories["Overweight"].append(cost)
            else:
                bmi_categories["Obese"].append(cost)
        
        return {category: round(sum(cost) / len(cost), 2) if cost else 0 for category, cost in bmi_categories.items()}

    def average_cost_by_sex(self):
        """Calculates average cost based on sex."""
        male_costs = []
        female_costs = []

        for row in self.data:
            sex = row[1]
            cost = float(row[6])
            
            if sex.lower() == "male":
                male_costs.append(cost)
            else:
                female_costs.append(cost)

        average_male_cost = round(sum(male_costs) / len(male_costs), 2) if male_costs else 0
        average_female_cost = round(sum(female_costs) / len(female_costs), 2) if female_costs else 0

        return {'Average cost for males': average_male_cost, 'Average cost for females': average_female_cost}

    # def cost_difference(self, category_data):
    #     """Calculates percentage increase/decrease between categories."""
    #     sorted_data = sorted(category_data.items())
    #     cost_changes = {}

    #     for i in range(1, len(sorted_data)):
    #         prev_group, prev_cost = sorted_data[i-1]
    #         curr_group, curr_cost = sorted_data[i]

    #         percentage_change = ((curr_cost - prev_cost) / prev_cost) * 100
    #         cost_changes[f"{prev_group} → {curr_group}"] = percentage_change

    #     return cost_changes

##########################################################

medical_cost_data = MedicalCostAnalyzer('insurance.csv')

avg_cost_by_age = medical_cost_data.average_cost_by_age_group()
avg_cost_by_children = medical_cost_data.average_cost_by_children()
avg_cost_by_smoking_status = medical_cost_data.average_cost_by_smoking_status()
avg_cost_by_BMI = medical_cost_data.average_cost_by_BMI()
avg_cost_by_sex = medical_cost_data.average_cost_by_sex()

print(avg_cost_by_age)
print(avg_cost_by_children)
print(avg_cost_by_smoking_status)
print(avg_cost_by_BMI)
print(avg_cost_by_sex)

##########################################################

