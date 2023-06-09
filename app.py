import sys
import pandas as pd
import os


def calculate_money_flow_index(m, path, directory_default):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path)

    # Calculate the 'Typical Price'
    df['Typical Price'] = (df['High'] + df['Low'] + df['Close']) / 3

    # Calculate the 'Money Flow'
    df['Money Flow'] = df['Typical Price'].diff() * df['Volume']
    df.loc[0, 'Money Flow'] = 0

    # Calculate the 'Positive Money Flow' and 'Negative Money Flow'
    df['Positive Money Flow'] = df['Money Flow'].apply(lambda x: x if x > 0 else 0).rolling(m).sum()
    df['Negative Money Flow'] = df['Money Flow'].apply(lambda x: x if x < 0 else 0).rolling(m).sum()

    # Calculate the 'Money Flow Index'
    df['Money Flow Index'] = 100 * (df['Positive Money Flow'] / df['Negative Money Flow']) / (1 + (df['Positive Money Flow'] / df['Negative Money Flow']))

    # Export the DataFrame to a CSV file
    output_path = f"sample_output_{m}.csv"

    file_path = os.path.join(directory_default, output_path)

    df.to_csv(file_path, index=False)
    print(f"Output file saved at {file_path}")

# Get the command-line arguments
m = int(sys.argv[1])
path = sys.argv[2]
directory_default = sys.argv[3]

# Call the function with the provided arguments
calculate_money_flow_index(m, path, directory_default)
