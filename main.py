from integ import process_image
from matching.Name_match import name_match
from matching.Address_match import address_match
# from matching.UID_match import uid_match
import pandas as pd
import os

IMG_PATH = "2.jpg"
INPUT_PATH = "INPUT.xlsx"
OUTPUT_PATH = "OUTPUT.xlsx"
# folder_path = "C:/Users/chait/OneDrive/Desktop/AI based fraud managment for UID aadhar/test"
# files = os.listdir(folder_path)
# for file in files:
#     file_path = os.path.join(folder_path,file)
#     if os.path.isfile(file_path): #check if the file is a file or not
Data = process_image(IMG_PATH, OUTPUT_PATH)
Extracted_UID = Data.get("UID", "")
Extracted_ADD = Data.get("ADDRESS", "")
Extracted_Name = Data.get("NAME", "")
input_df = pd.read_excel(INPUT_PATH)
uid_exists = Extracted_UID in input_df["UID"].values
print(f"UID exists in the database: {uid_exists}")
if uid_exists:
    matching_row = input_df[input_df["UID"] == Extracted_UID]
    name_m = name_match(matching_row["NAME"].values[0], Extracted_Name) if not matching_row["NAME"].empty else False ##if any of the filelds not exist returning False Else move to match functins
    address_m = address_match(matching_row["ADDRESS"].values[0], Extracted_ADD) if not matching_row["ADDRESS"].empty else False
    
    # Update missing fields in the input file
    if matching_row["ADDRESS"].empty:
        input_df.loc[input_df["UID"] == Extracted_UID, "ADDRESS"] = Extracted_ADD
    if matching_row["NAME"].empty:
        input_df.loc[input_df["UID"] == Extracted_UID, "NAME"] = Extracted_Name
    input_df.to_excel(INPUT_PATH, index=False)
    
    output_df = pd.read_excel(OUTPUT_PATH)
    output_df["REMARKS"] = output_df["REMARKS"].astype(str)
    output_df["UID_MATCH"] = output_df["UID_MATCH"].astype(bool)
    output_df["ADDRESS_MATCH"] = output_df["ADDRESS_MATCH"].astype(bool)
    output_df["NAME_MATCH"] = output_df["NAME_MATCH"].astype(bool)
    output_df["OVERALL_MATCH"] = output_df["OVERALL_MATCH"].astype(bool)
    if name_m and address_m:
        output_df.loc[output_df["UID"] == Extracted_UID, ["REMARKS", "UID_MATCH", "ADDRESS_MATCH", "NAME_MATCH", "OVERALL_MATCH"]] = ["Name and Address match", True, True, True, True]
    elif name_m:
        output_df.loc[output_df["UID"] == Extracted_UID, ["REMARKS", "UID_MATCH", "ADDRESS_MATCH", "NAME_MATCH", "OVERALL_MATCH"]] = ["Name match", True, False, True, False]
    elif address_m:
        output_df.loc[output_df["UID"] == Extracted_UID, ["REMARKS", "UID_MATCH", "ADDRESS_MATCH", "NAME_MATCH", "OVERALL_MATCH"]] = ["Address match", True, True, False, False]
    else:
        output_df.loc[output_df["UID"] == Extracted_UID, ["REMARKS", "UID_MATCH", "ADDRESS_MATCH", "NAME_MATCH", "OVERALL_MATCH"]] = ["No match", True, False, False, False]
    
    output_df.to_excel(OUTPUT_PATH, index=False)
    print("Results have been updated in the output file.")
else:
    print("Data Not Found In The DataBase")
    user_input = int(input("Please Enter '1' To Upload OtherWise '0'"))
    if user_input == 1:
        new_data = {
            "UID": [Extracted_UID],
            "NAME": [Extracted_Name],
            "ADDRESS": [Extracted_ADD]
        }
        new_df = pd.DataFrame(new_data)
        input_df = pd.concat([input_df, new_df], ignore_index=True)
        input_df.to_excel(INPUT_PATH, index=False)
        print("Data has been uploaded to the database.")
    else:
        quit()
