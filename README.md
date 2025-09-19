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
