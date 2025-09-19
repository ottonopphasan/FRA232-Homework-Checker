import pandas as pd
import io
import contextlib
from sympy import symbols, sin, sqrt, sympify
import math
from utils import is_key_correct, update_correctness_with_calc
from Sub_calcuration import cal_program

def check_excel(input_excel_path, tolerance, output_excel_path):
    df = pd.read_excel(input_excel_path)
    answer_key = {}

    # Remove the column named 'Timestamp' if it exists
    if 'Timestamp' in df.columns:
        df = df.drop(columns=['Timestamp'])

    # Extract and process the 'ans' row
    if 'รหัสนักศึกษา ' in df.columns:
        for index, row in df.iterrows():
            if row['รหัสนักศึกษา '] == "ans":
                for col in df.columns:
                    cell_split = str(row[col]).split(':')
                    if cell_split[0] == 'S':
                        cell_split[1] = str(cell_split[1]).replace(' ', '').lower()
                        answer_key[col] = [cell_split[0], cell_split[1]]
                    elif cell_split[0] == 'R':
                        range_vals = str(cell_split[1]).split('-')
                        range_vals = [float(val) for val in range_vals]
                        answer_key[col] = [cell_split[0], range_vals]
                    elif cell_split[0] == 'F':
                        answer_key[col] = [cell_split[0], float(cell_split[1])]
                    elif cell_split[0] == 'FA':
                        answer_key[col] = [cell_split[0], abs(float(cell_split[1]))]
                    elif cell_split[0] == 'Cal':
                        answer_key[col] = [cell_split[0]]
                    elif cell_split[0] == 'T':
                        answer_key[col] = [cell_split[0]]

    # Prepare to collect results for output
    output_rows = []

    for index, row in df.iterrows():
        if row['รหัสนักศึกษา '] != "ans":
            student_row = {}
            for col in answer_key.keys():
                student_row[col] = row.get(col, None)

            # Compare each key's value in student_row to answer_key, store results in new array
            correctness_list = []
            for col in answer_key.keys():
                ans_type = answer_key[col][0]
                ans_val = answer_key[col][1] if len(answer_key[col]) > 1 else None
                student_val = student_row[col]
                result = False
                # String type
                if ans_type == 'S':
                    if student_val is not None and str(student_val).replace(' ', '').lower() == ans_val:
                        result = True
                # Float type
                elif ans_type == 'F':
                    try:
                        if student_val is not None and float(student_val) - ans_val <= tolerance:
                            result = True
                    except Exception:
                        result = False
                # Float Absolute type
                elif ans_type == 'FA':
                    try:
                        if student_val is not None and abs(float(student_val) - ans_val) <= tolerance:
                            result = True
                    except Exception:
                        result = False
                # Range type
                elif ans_type == 'R':
                    try:
                        if student_val is not None:
                            student_val_float = float(student_val)
                            if ans_val[0] <= student_val_float <= ans_val[1]:
                                result = True
                    except Exception:
                        result = False
                # Cal type: leave as is
                elif ans_type == 'Cal':
                    result = None
                elif ans_type == 'T':
                    result = True
                correctness_list.append({"key": col, "correct": result})

        # Capture print output from shaft_cal
        log_stream = io.StringIO()
        with contextlib.redirect_stdout(log_stream):
            cal_program(answer_key, student_row, tolerance, correctness_list)
        calculation_log = log_stream.getvalue().strip()
        
        # Prepare output row
        output_row = {"รหัสนักศึกษา ": row['รหัสนักศึกษา ']}
        for item in correctness_list:
            key = item["key"]
            val = item["correct"]
            if val is True:
                output_row[key] = True
            else:
                input_data = student_row.get(key, None)
                calc_data = None
                # Try to get calculated value if available
                if key in student_row and student_row[key] is not None:
                    try:
                        calc_data = float(student_row[key])
                    except Exception:
                        calc_data = student_row[key]
                # If calculated value is different from input, show both
                if calc_data is not None and input_data != calc_data:
                    output_row[key] = f"{input_data} | {calc_data}"
                else:
                    output_row[key] = input_data

        # Add point column: count True values (excluding calculation_log and รหัสนักศึกษา )
        point = sum(1 for k, v in output_row.items() if k not in ["รหัสนักศึกษา ", "calculation_log"] and v is True)
        output_row["point"] = point
        output_row["calculation_log"] = calculation_log  # Add log to output
        output_rows.append(output_row)

    # Write output to Excel
    if output_rows:
        out_df = pd.DataFrame(output_rows)
        out_df.to_excel(output_excel_path, index=False)

check_excel('Homework 1 Shaft Design & Calculation (Responses) (6).xlsx', 0.1, 'result_sheet.xlsx')