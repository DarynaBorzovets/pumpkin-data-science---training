import pandas as pd

def average_organic_price(df: pd.DataFrame) -> float:
    """
    Calculate the average 'High Price' of pumpkins where the 'Type' is 'Organic'.

    Parameters:
        df (pd.DataFrame): DataFrame containing pumpkin price data.

    Returns:
        float: The average 'High Price' of organic pumpkins.
    """
    # Filter rows where 'Type' is 'Organic'
    organic_df = df[df['Type'] == 'Organic']
    
    # Check if there are any organic pumpkins to avoid division by zero
    if organic_df.empty:
        return float('nan')  # Return NaN if no organic pumpkins are found
    
    # Calculate the average of 'High Price'
    average_price = organic_df['High Price'].mean()
    
    return average_price

# Example usage (optional)
if __name__ == "__main__":
    # Example DataFrame (replace this with your actual DataFrame)
    data = {
        'City Name': ['New York', 'Chicago', 'Boston', 'New York', 'Boston'],
        'Date': ['2024-08-01', '2024-08-01', '2024-08-02', '2024-08-02', '2024-08-03'],
        'Type': ['Organic', 'Conventional', 'Organic', 'Organic', 'Conventional'],
        'High Price': [5.00, 4.00, 6.00, 7.00, 4.50],
        'Low Price': [3.00, 2.50, 4.00, 5.00, 3.00],
        'Variety': ['Pie Pumpkin', 'Carving Pumpkin', 'Sugar Pumpkin', 'Pie Pumpkin', 'Carving Pumpkin']
    }
    df = pd.DataFrame(data)

    # Calculate average organic price
    average_price = average_organic_price(df)
    print(f"The average high price for organic pumpkins is: ${average_price:.2f}")
