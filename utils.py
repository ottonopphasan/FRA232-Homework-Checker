def is_key_correct(correctness_list, required_keys, note):
    if isinstance(required_keys, list):
        for key in required_keys:
            found = False
            for item in correctness_list:
                if item["key"] == key:
                    if not bool(item["correct"]):
                        print(f"note : (wrong) {key}" if note is None else f"{note} : (wrong) {key}\n")
                        return False
                    found = True
                    break
        return True
    else:
        return False

def update_correctness_with_calc(correctness_list, key, student_row, calculated_value, tolerance):
    """
    Compare student_row[key] to calculated_value, print result, and update correctness_list for key.
    """
    if key in student_row and student_row[key] is not None:
        is_correct = abs(abs(float(student_row[key])) - abs(calculated_value)) <= tolerance
        if is_correct:
            print(f"{key} : (Correct) input {student_row[key]} match calculated value {calculated_value}\n")
        else:
            print(f"{key} : (incorrect) input {student_row[key]} does NOT match calculated value {calculated_value}\n")
        for item in correctness_list:
            if item["key"] == key:
                item["correct"] = is_correct
                break
        else:
            correctness_list.append({"key": key, "correct": is_correct})
