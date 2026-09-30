# Wah Cantt Health Research - By Khansa Badsha

print("Welcome to Wah Cantt Health Research Project")

# Sample health data
health_issues = ["Fever", "Diabetes", "High Blood Pressure", "Cold"]

print("\nCommon health issues in Wah Cantt:")
for issue in health_issues:
    print(f"- {issue}")

# Simple survey function
def health_survey():
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    print(f"\nThank you {name}, your data is saved for research!")

health_survey()
