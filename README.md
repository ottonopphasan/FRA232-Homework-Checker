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
```

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
## Input  
| Student ID | Q1     | Q2       | Q3      | Q4     |
| ---------- | ------ | -------- | ------- | ------ |
| **ans**    | F:6000 | FA:-10.0 | R:1.5-2 | S\:Yes |
| 65001      | 5999.8 | -10.05   | 1.7     | yes    |
| 65002      | 6100   | 10.2     | 2.5     | YES    |
| 65003      | 5800   | -9.8     | 1.6     | no     |

## Output
| Student ID | Q1 | Q2 | Q3 | Q4 |
| ---------- | -- | -- | -- | -- |
| 65001      | ✅  | ✅  | ✅  | ✅  |
| 65002      | ❌  | ✅  | ❌  | ✅  |
| 65003      | ❌  | ✅  | ✅  | ❌  |

