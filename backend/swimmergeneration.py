import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating random names
fake = Faker()

# Define the Swimmer class
class Swimmer:
    def __init__(self, name, gender, age, time, stroke):
        self.name = name
        self.gender = gender
        self.age = age
        self.time = time
        self.stroke = stroke

# Function to generate a random swimmer with a realistic name
def generate_swimmer_with_name():
    name = fake.name()
    age = random.randint(25, 90)
    gender = random.choice(['M', 'F'])
    stroke = random.choice(['backstroke', 'freestyle', 'breaststroke', 'butterfly'])
    
    # Time calculation based on age with some variation to simulate outliers
    if age < 40:
        time = random.uniform(60, 100)
    elif age < 60:
        time = random.uniform(90, 120)
    elif age < 75:
        time = random.uniform(110, 150)
    else:
        time = random.uniform(130, 180)
    
    # Adding some outliers
    if random.random() < 0.05:  # 5% chance for an outlier
        time += random.uniform(10, 30)
    
    return Swimmer(name, gender, age, round(time, 2), stroke)

# Generate 100 swimmers with realistic names and store them in a list
swimmers_with_names = [generate_swimmer_with_name() for _ in range(100)]

# Convert the list of swimmers to a DataFrame
swimmer_data_named = {
    "Name": [swimmer.name for swimmer in swimmers_with_names],
    "Gender": [swimmer.gender for swimmer in swimmers_with_names],
    "Age": [swimmer.age for swimmer in swimmers_with_names],
    "Time (seconds)": [swimmer.time for swimmer in swimmers_with_names],
    "Stroke": [swimmer.stroke for swimmer in swimmers_with_names]
}
swimmer_df_named = pd.DataFrame(swimmer_data_named)

# Export to CSV with realistic names
output_path_named = "generated_swimmers_with_names.csv"
swimmer_df_named.to_csv(output_path_named, index=False)


print(f"CSV file saved at: {output_path_named}")
