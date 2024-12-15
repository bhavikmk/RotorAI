import scipy.io
import pandas as pd

csv_file_path = "/data_csv/"  # Replace with desired CSV file path

# Path to the merged .mat file
mat_file_path = "data/data-20130307T015746Z.mat"  # Replace with your actual file name

# Load the .mat file
mat_data = scipy.io.loadmat(mat_file_path)

# Extract 'tach' and 'vibration' data
tach = mat_data.get("tach", None)  # Tachometer data
vibration = mat_data.get("vibration", None)  # Vibration data

if tach is None or vibration is None:
    raise ValueError("Tach or vibration data not found in the .mat file.")

## Load Data of 50 days in for loop and save vbration & tach data in different CSV

# Convert to DataFrame for easier handling
tach_df = pd.DataFrame(tach, columns=["Tach (RPM)"])
vibration_df = pd.DataFrame(vibration, columns=["Vibration (Amplitude)"])


# Save to a CSV file
tach_df.to_csv("tach{n}.csv")
vibration_df.to_csv("vibration{n}.csv")
print("Saved data for {n} iterations")
