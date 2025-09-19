import pandas as pd
import io
import contextlib
from sympy import symbols, sin, sqrt, sympify
import math
from utils import is_key_correct, update_correctness_with_calc

def cal_program(answer_key, student_row, tolerance, correctness_list):
    F1_col = 'F1 [N]'
    F2_col = 'F2 [N]'
    F_AT_col = 'F_AT [N]'
    F_AN_col = 'F_AN [N]'
    Dx_col = 'Dx [N]'
    Dy_col = 'Dy [N]'
    Ex_col = 'Ex [N]'
    Ey_col = 'Ey [N]'
    Ct_col = 'Ct ที่เลือกใช้'
    Cm_col = 'Cm ที่เลือกใช้'
    Ot_col = 'Operational Torque [Nm]'
    Sd_col = 'เส้นผ่านศูนย์กลางเพลาที่คำนวณได้ [mm.]'
    Sf_col = 'Strength factor'
    Mm_col = 'Maximum Moment [Nm]'

    # Calculate F1
    if is_key_correct(correctness_list, [F2_col], 'F1'):
        if F2_col in student_row and student_row[F2_col] is not None:
            F1_calc = student_row[F2_col] * 8
            update_correctness_with_calc(correctness_list, F1_col, student_row, F1_calc, tolerance)

    # Calculate Dx
    if is_key_correct(correctness_list, [F1_col, F2_col, F_AN_col], 'Dx'):
        if all(x in student_row and student_row[x] is not None for x in [F1_col, F2_col, F_AN_col]):
            F1_val = float(student_row[F1_col])
            F2_val = float(student_row[F2_col])
            F_AN_val = float(student_row[F_AN_col])
            Dx_calc = abs(((F1_val + F2_val) * math.cos((45 * math.pi) / 180) * 0.4 - F_AN_val * 0.125) / 0.6)
            update_correctness_with_calc(correctness_list, Dx_col, student_row, Dx_calc, tolerance)

    # Calculate Dy
    if is_key_correct(correctness_list, [F1_col, F2_col, F_AT_col], 'Dy'):
        if all(x in student_row and student_row[x] is not None for x in [F1_col, F2_col, F_AT_col]):
            F1_val = float(student_row[F1_col])
            F2_val = float(student_row[F2_col])
            F_AT_val = float(student_row[F_AT_col])
            Dy_calc = abs((-((F1_val + F2_val) * math.cos(45 * math.pi / 180) * 0.4) - (F_AT_val * 0.125) + 15) / 0.6)
            update_correctness_with_calc(correctness_list, Dy_col, student_row, Dy_calc, tolerance)

    # Calculate Ex
    if is_key_correct(correctness_list, [F1_col, F2_col, F_AN_col], 'Ex'):
        if all(x in student_row and student_row[x] is not None for x in [F1_col, F2_col, F_AN_col]):
            F1_val = float(student_row[F1_col])
            F2_val = float(student_row[F2_col])
            F_AN_val = float(student_row[F_AN_col])
            Ex_calc = abs((((F1_val + F2_val) * math.cos((45 * math.pi) / 180) * 0.2) - F_AN_val * 0.475) / 0.6)
            update_correctness_with_calc(correctness_list, Ex_col, student_row, Ex_calc, tolerance)

    # Calculate Ey
    if is_key_correct(correctness_list, [F1_col, F2_col, F_AT_col], 'Ey'):
        if all(x in student_row and student_row[x] is not None for x in [F1_col, F2_col, F_AT_col]):
            F1_val = float(student_row[F1_col])
            F2_val = float(student_row[F2_col])
            F_AT_val = float(student_row[F_AT_col])
            Ey_calc = abs((((F1_val + F2_val) * math.cos(45 * math.pi / 180) * 0.2) + (F_AT_val * 0.475)+3) / 0.6)
            update_correctness_with_calc(correctness_list, Ey_col, student_row, Ey_calc, tolerance)    
    
    # Calculate Sd (shaft diameter)
    if is_key_correct(correctness_list, [Sf_col, Ct_col, Ot_col, Cm_col, Mm_col], 'Sd'):
        if all(x in student_row and student_row[x] is not None for x in [F1_col, F2_col, F_AT_col]):
            Sf_val = float(student_row[Sf_col])
            Ct_val = float(student_row[Ct_col])
            Ot_val = float(student_row[Ot_col])
            Cm_val = float(student_row[Cm_col])
            Mm_val = float(student_row[Mm_col])
            sqrt_val = math.sqrt((Ct_val * Ot_val) ** 2 + (Cm_val * Mm_val) ** 2)
            Sd_calc = (((16 / (math.pi * Sf_val)) * sqrt_val) ** (1/3))*10
            update_correctness_with_calc(correctness_list, Sd_col, student_row, Sd_calc, tolerance)