import pandas as pd

# Load the CSV files in chunks
files = ["data/question_tags.csv", "data/questions.csv"]  # Correct file paths
count = 0

for file in files:
    try:
        # Read CSV in chunks
        for chunk in pd.read_csv(file, dtype=str, on_bad_lines="skip", chunksize=10000):
            # Check if column names exist in this chunk
            if "Tag" in chunk.columns:
                count += chunk["Tag"].astype(str).str.contains("GitHub", case=False, na=False).sum()

    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Print the total count
print(f"Total lines containing 'GitHub': {count}")

# Save the result to a text file
with open("_output/github_count.txt", "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")
    