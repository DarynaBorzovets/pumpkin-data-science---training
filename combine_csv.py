import pandas as pd
import os

def create_df() -> pd.DataFrame:
    """
    Reads multiple CSV files from a specified folder, combines them into a single DataFrame, 
    and returns the combined DataFrame. The files are processed in alphabetical order based on city names.
    
    Returns:
        pd.DataFrame: Combined DataFrame containing data from all CSV files.
    """
    # Path to the folder containing the CSV files
    data_folder = 'data/'  # Update this to the path where your CSV files are stored

    # List of city CSV filenames in alphabetical order
    city_files = [
        'atlanta.csv', 'baltimore.csv', 'boston.csv', 'chicago.csv', 'columbia.csv',
        'dallas.csv', 'detroit.csv', 'los_angeles.csv', 'miami.csv', 'new_york.csv',
        'philadelphia.csv', 'san_francisco.csv', 'st_louis.csv'
    ]

    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through the sorted city files and read each into a DataFrame
    for city_file in city_files:
        # Construct the full path to the CSV file
        file_path = os.path.join(data_folder, city_file)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)
    
    return combined_df

# Create the combined DataFrame
combined_df = create_df()

# Save the combined DataFrame to a new CSV file
combined_file_name = 'combined_pumpkin_sales.csv'
combined_df.to_csv(combined_file_name, index=False)

# Display the first few rows of the combined DataFrame (optional)
print(combined_df.head())
