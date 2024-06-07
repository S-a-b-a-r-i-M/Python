from typing import List
import openpyxl

# create a class model
class JDCVInfo:
    jd_id: int
    cids: List[int] = []

workbook = openpyxl.load_workbook(filename="Caypro_filter_details.xlsx", read_only=True, data_only=True)

sheet1 = workbook["OPPURTUNITY"]
sheet2 = workbook["CUSTOMERS"]

def get_related_rows_in_sheet2(s1_row_id):
    res = []
    flag = False
    for s2_row in sheet2.iter_rows(min_row=2, values_only=True):
        if s2_row[0] == s1_row_id:
            flag = True
            res.append(s2_row)
        elif(flag):
            break

    return res

def create_candidates(jd_id, s2_rows):
    pass

jd_id = 1
for s1_row in sheet1.iter_rows(min_row=2, values_only=True):#values_only=True is used to get only values inside the cell
    if not s1_row[0]:
        break
    print(s1_row[0])
    # jd_id=create record in t_jds

    related_rows2 = get_related_rows_in_sheet2(s1_row[0])
    create_candidates(jd_id, related_rows2)
    print(len(related_rows2))


        
    

