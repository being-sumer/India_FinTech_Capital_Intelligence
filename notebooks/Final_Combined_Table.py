# Append xlsx files below each other

import pandas as pd
import os

def append_xlsx_files():
    """
    Appends multiple XLSX files from a specified folder into a single
    XLSX file, ensuring no data loss.
    """
    # --- CONFIGURATION ---
    # Enter the path to the folder containing your XLSX files.
    # Example for Windows: r"C:\Users\YourUser\Documents\YourExcelFiles"
    # Example for macOS/Linux: r"/Users/youruser/Documents/YourExcelFiles"
    folder_path = r"F:\Self Learning\Finance\FinTech Funding - Tableau\2022" # <--- IMPORTANT: SET YOUR FOLDER PATH HERE

    # Enter the desired name for the final combined XLSX file.
    # It will be saved in the same 'folder_path'.
    output_filename = "Combined_Data.xlsx" # <--- IMPORTANT: SET YOUR OUTPUT FILENAME HERE
    # ---------------------

    output_file_path = os.path.join(folder_path, output_filename)

    if not os.path.isdir(folder_path):
        print(f"Error: The path '{folder_path}' is not a valid directory. Please check the path and try again.")
        return

    all_dataframes = []
    processed_files_count = 0
    skipped_files_count = 0

    print(f"Scanning '{folder_path}' for XLSX files to append...")

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.xlsx') and not filename == output_filename:
            file_path = os.path.join(folder_path, filename)
            print(f"Processing: '{filename}'...")
            try:
                # Read the Excel file into a DataFrame
                # By default, pd.read_excel reads the first sheet.
                # If your files have multiple sheets and you need specific ones,
                # you might need to add sheet_name parameter (e.g., sheet_name=0 or sheet_name='Sheet1')
                df = pd.read_excel(file_path)
                all_dataframes.append(df)
                processed_files_count += 1
                print(f"  --> Successfully loaded '{filename}'.")
            except pd.errors.EmptyDataError:
                print(f"  --> Skipped '{filename}': File is empty.")
                skipped_files_count += 1
            except Exception as e:
                print(f"  --> Error reading '{filename}': {e}. Skipping this file.")
                skipped_files_count += 1
        elif filename == output_filename:
            print(f"Skipping output file '{filename}' to prevent self-appending.")
            skipped_files_count += 1
        else:
            # print(f"Skipping '{filename}': Not an XLSX file.") # Uncomment to see non-XLSX files being skipped
            pass

    if not all_dataframes:
        print("\nNo valid XLSX files found to append (or all were empty/errored). No output file created.")
        return

    print(f"\nAppending {processed_files_count} files...")
    try:
        # Concatenate all DataFrames.
        # ignore_index=True resets the index of the combined DataFrame,
        # which is usually desired when appending.
        combined_df = pd.concat(all_dataframes, ignore_index=True)

        # Export the combined DataFrame to a new XLSX file.
        # index=False prevents pandas from writing the DataFrame index as a column.
        combined_df.to_excel(output_file_path, index=False)

        print(f"\nSuccessfully created '{output_filename}' in '{folder_path}'.")
        print(f"Total rows in combined file: {len(combined_df)}")
        print("All specified XLSX files have been appended without data loss.")

    except Exception as e:
        print(f"\nAn error occurred during concatenation or writing the output file: {e}")

if __name__ == "__main__":
    append_xlsx_files()