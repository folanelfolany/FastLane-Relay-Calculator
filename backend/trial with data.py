import pandas as pd
import itertools

class Swimmer:
    def __init__(self, name, gender, age, time, stroke):
        self.name = name
        self.gender = gender
        self.age = age
        self.time = time  # Time in seconds
        self.stroke = stroke
    
    def display_data(self):
        formatted_time = self.format_time(self.time)
        print(f"Name: {self.name} | Gender: {self.gender} | Age: {self.age} | Stroke: {self.stroke} | Time: {formatted_time}")
    
    @staticmethod
    def format_time(seconds):
        minutes = int(seconds // 60)
        remaining_seconds = int(seconds % 60)
        return f"{minutes:02}:{remaining_seconds:02}"

# Load swimmer data from CSV
file_path = r"/workspaces/FastLane-Relay-Calculator/backend/generated_swimmers_with_names.csv"  # Ensure this file exists in the correct directory
swimmer_df = pd.read_csv(file_path)

# Convert DataFrame rows to Swimmer objects with adjusted gender and stroke parsing
swimmers = [
    Swimmer(
        row["Name"],
        "male" if row["Gender"].strip().upper() == "M" else "female",
        row["Age"],
        row["Time (seconds)"],
        row["Stroke"].strip().lower()
    )
    for _, row in swimmer_df.iterrows()
]

# Display counts to check if data loaded correctly
print(f"Total swimmers loaded: {len(swimmers)}")
print(f"Swimmer gender breakdown: Males - {sum(s.gender == 'male' for s in swimmers)}, Females - {sum(s.gender == 'female' for s in swimmers)}")
print(f"Stroke breakdown:")
for stroke in ["backstroke", "freestyle", "breaststroke", "butterfly"]:
    print(f"  {stroke.capitalize()}: {sum(s.stroke == stroke for s in swimmers)} swimmers")

# Prompt the user to select gender and stroke
selected_gender = input("Please select the gender for the relay (M for male, F for female, Mixed for mixed relay): ").strip().lower()
selected_stroke = input(f"Please select a stroke for the relay (backstroke, freestyle, breaststroke, butterfly, or 'IM' for Individual Medley): ").strip().lower()

# Find the fastest swimmer for each stroke
stroke_groups = {}
for stroke in ["backstroke", "freestyle", "breaststroke", "butterfly"]:
    sorted_swimmers = sorted([s for s in swimmers if s.stroke == stroke], key=lambda s: s.time)
    stroke_groups[stroke] = sorted_swimmers[:2]  # Keep top 2 fastest swimmers for each stroke
    print(f"Top swimmers for {stroke.capitalize()}:")
    for swimmer in stroke_groups[stroke]:
        swimmer.display_data()

# Select the top swimmers for each stroke, maintaining the 2-male, 2-female constraint
combinations = []
if selected_stroke == "im":
    # Individual Medley (IM) requires one swimmer for each stroke
    for backstroke_swimmer in stroke_groups['backstroke']:
        for freestyle_swimmer in stroke_groups['freestyle']:
            for breaststroke_swimmer in stroke_groups['breaststroke']:
                for butterfly_swimmer in stroke_groups['butterfly']:
                    combo = [backstroke_swimmer, freestyle_swimmer, breaststroke_swimmer, butterfly_swimmer]
                    male_count = sum(1 for swimmer in combo if swimmer.gender == "male")
                    female_count = sum(1 for swimmer in combo if swimmer.gender == "female")
                    if male_count == 2 and female_count == 2:
                        combined_time = sum(swimmer.time for swimmer in combo)
                        combinations.append((combo, combined_time))
else:
    # For other strokes, filter swimmers based on the stroke selected
    filtered_swimmers = [swimmer for swimmer in swimmers if swimmer.stroke == selected_stroke]
    print(f"Swimmers available for {selected_stroke.capitalize()}: {len(filtered_swimmers)}")
    
    # Check if there are enough swimmers for the selected relay type
    if selected_gender == "mixed":
        # Mixed relay requires exactly two males and two females
        for combo in itertools.combinations(filtered_swimmers, 4):
            male_count = sum(1 for swimmer in combo if swimmer.gender == "male")
            female_count = sum(1 for swimmer in combo if swimmer.gender == "female")
            if male_count == 2 and female_count == 2:
                combined_time = sum(swimmer.time for swimmer in combo)
                combinations.append((combo, combined_time))
    else:
        # Single-gender relay
        if len(filtered_swimmers) < 4:
            print(f"Error: Not enough swimmers available for the stroke '{selected_stroke}' to form a relay.")
            exit()
        combinations = [(combo, sum(swimmer.time for swimmer in combo)) 
                        for combo in itertools.combinations(filtered_swimmers, 4)]

# Sort combinations by their combined time to find the top three fastest
if combinations:
    combinations.sort(key=lambda x: x[1])

    # Display the top three fastest combinations in MM:SS format
    print("\nTop 3 Winning Combinations:")
    for rank, (combo, combined_time) in enumerate(combinations[:3], start=1):
        formatted_combined_time = Swimmer.format_time(combined_time)
        print(f"\nRank {rank}: Combined Time = {formatted_combined_time}")
        for swimmer in combo:
            swimmer.display_data()
else:
    print("Error: No valid relay combinations found based on the selected criteria.")
