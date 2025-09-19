# FRA232-Homework-Checker
_By 2025 TA_

This project is a program to **check student homework answers** submitted through **Google Forms** and stored in **Excel** format.

The main branch contains:
- A **default template** for checking answers in the standard format.
- Example code for handling **more advanced calculations**.

---

## 🔧 How It Works
1. Export student answers from Google Form into an Excel file.
2. Use the main checker function:

```python
check_excel('name.xlsx', tolerance, 'result_sheet.xlsx')

---

## 📑 Excel Format Rules

In the Excel file:
- The row with **`ans`** acts as the **answer key** (instead of a student ID).
- Each cell should contain a key specifying how the answer will be checked.

### Supported Answer Keys

| Key Type       | Format         | Description                                                                 | Example Input | Example Student Answer | Result |
|----------------|----------------|-----------------------------------------------------------------------------|---------------|-------------------------|--------|
| **Float**      | `F:value`      | Must be within ± tolerance of `value`.                                      | `F:0.01`      | `0.011` (tol=0.01)      | ✅ Correct |
| **Abs Float**  | `FA:value`     | Must match the **absolute value** within ± tolerance.                       | `FA:-10.0`    | `10.05` (tol=0.1)       | ✅ Correct |
| **Range**      | `R:min-max`    | Must fall within the specified range.                                       | `R:0-1`       | `0.85`                  | ✅ Correct |
| **String**     | `S:string`     | Case-insensitive, spaces ignored.                                           | `S:Hello`     | ` hello `               | ✅ Correct |
| **Manual**     | `Mannual`      | Skipped → requires manual checking.                                         | `Mannual`     | *(any value)*          | 🔍 Manual |
| **True**       | `T`            | Always correct, automatically marked True.                                  | `T`           | *(any value)*          | ✅ Correct |
| **Calc.**      | `Cal`          | Value will be calculated from the **Sub_calcuration** file.                 | `Cal`         | *(auto generated)*      | ⚙️ Calculated |

---

### Example  
In the Excel sheet:

- **`F:6000`** → Float check with tolerance  
- **`FA:-10.0`** → Absolute float check with tolerance  
- **`R:1.5-2`** → Range check  
- **`Cal`** → Auto-calculated based on `Sub_calcuration` file  
