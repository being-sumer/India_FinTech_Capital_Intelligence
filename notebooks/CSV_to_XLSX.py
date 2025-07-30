# csv to xlsx

import pandas as pd
import os

def convert_csvs_in_folder():
    """
    Converts all CSV files in a specified folder to XLSX format.
    You'll enter the folder path directly in the script.
    Includes error handling for common encoding issues.
    """
    # --- ENTER YOUR FOLDER PATH HERE ---
    folder_path = r"F:\Self Learning\Finance\FinTech Funding - Tableau\2022"
    # -----------------------------------

    if not os.path.isdir(folder_path):
        print(f"Error: The path '{folder_path}' is not a valid directory. Please check the path and try again.")
        return

    print(f"Scanning '{folder_path}' for CSV files...")
    converted_count = 0
    skipped_count = 0

    # List of common encodings to try
    # latin1 is often a good fallback for non-UTF-8 characters in CSVs
    # cp1252 (Windows-1252) is another very common one for European languages
    common_encodings = ['utf-8', 'latin1', 'cp1252', 'ISO-8859-1']

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            base_name = os.path.splitext(filename)[0]
            xlsx_file_path = os.path.join(folder_path, base_name + '.xlsx')

            print(f"Converting: '{filename}'...")
            df = None # Initialize df to None
            read_success = False

            for encoding in common_encodings:
                try:
                    df = pd.read_csv(csv_file_path, encoding=encoding)
                    print(f"  --> Read successfully with encoding: '{encoding}'")
                    read_success = True
                    break # Break out of the encoding loop if successful
                except UnicodeDecodeError:
                    # print(f"  --> Failed to read with encoding: '{encoding}'") # Uncomment to see all attempts
                    continue # Try the next encoding
                except pd.errors.EmptyDataError:
                    print(f"  --> Skipped '{filename}': File is empty.")
                    skipped_count += 1
                    read_success = False # Mark as not successfully read
                    break # No need to try other encodings if empty
                except Exception as e:
                    print(f"  --> An unexpected error occurred while reading '{filename}' with encoding '{encoding}': {e}")
                    skipped_count += 1
                    read_success = False # Mark as not successfully read
                    break # Stop trying other encodings for this file

            if read_success and df is not None:
                try:
                    df.to_excel(xlsx_file_path, index=False)
                    print(f"  --> '{os.path.basename(xlsx_file_path)}' created successfully.")
                    converted_count += 1
                except Exception as e:
                    print(f"  --> Error writing '{filename}' to XLSX: {e}")
                    skipped_count += 1
            elif not read_success and df is None and filename.lower().endswith('.csv'):
                 # This condition handles cases where all encoding attempts failed or an initial error occurred
                 # and the file wasn't marked as empty.
                print(f"  --> Failed to read '{filename}' with any of the attempted encodings ({', '.join(common_encodings)}). Skipping.")
                skipped_count += 1

        else:
            pass # Keep silent about non-CSV files for minimalism

    print("\n--- Conversion Complete ---")
    print(f"Successfully converted: {converted_count} files")
    print(f"Skipped/Errors: {skipped_count} files")

if __name__ == "__main__":
    convert_csvs_in_folder()