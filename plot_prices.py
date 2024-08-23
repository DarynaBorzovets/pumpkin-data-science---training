import pandas as pd
import matplotlib.pyplot as plt

def plot_prices(df: pd.DataFrame, city: str, variety: str) -> None:
    """
    Plot the minimum 'Low Price' of a given pumpkin variety in a specific city over time.

    Parameters:
        df (pd.DataFrame): DataFrame containing pumpkin sales data.
        city (str): The city to filter the sales data.
        variety (str): The pumpkin variety to filter the sales data.
    """
    # Ensure 'Date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Filter data for the specified city and pumpkin variety
    filtered_df = df[(df['City Name'] == city) & (df['Variety'] == variety)]
    
    # Aggregate to find the minimum 'Low Price' for each date
    aggregated_df = filtered_df.groupby('Date')['Low Price'].min().reset_index()
    
    # Check if there is data to plot
    if aggregated_df.empty:
        print(f"No data available for {variety} in {city}.")
        return

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(aggregated_df['Date'], aggregated_df['Low Price'], color='blue', marker='o', linestyle='-')
    
    # Set plot title and labels
    plt.title(f'{city} LOW PRICES FOR {variety}')
    plt.xlabel('Date')
    plt.ylabel('Low Price')
    
    # Rotate x-axis labels
    plt.xticks(rotation=60)
    
    # Save the plot as 'prices_plot.png'
    plt.savefig('prices_plot.png', bbox_inches='tight')
    
    # Show the plot
    plt.show()

# Sample data to test the function
data = {
    'City Name': ['New York', 'New York', 'New York', 'Chicago', 'Chicago'],
    'Date': ['2024-08-01', '2024-08-01', '2024-08-02', '2024-08-01', '2024-08-02'],
    'Type': ['Organic', 'Organic', 'Organic', 'Conventional', 'Organic'],
    'High Price': [5.00, 6.00, 7.00, 4.00, 5.50],
    'Low Price': [3.00, 4.00, 5.00, 2.50, 3.50],
    'Variety': ['Sugar Pumpkin', 'Sugar Pumpkin', 'Sugar Pumpkin', 'Carving Pumpkin', 'Sugar Pumpkin']
}

# Create DataFrame from sample data
df = pd.DataFrame(data)

# Call the function with sample data
plot_prices(df, 'New York', 'Sugar Pumpkin')
