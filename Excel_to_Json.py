import pandas
import json 

df: pandas.DataFrame = pandas.read_excel("IT Sales Ent.xlsx")

json_data = []

for idx, row in df.iterrows():
    data_dict = row.to_dict()
    json_data.append(data_dict)


with open("IT_sales_ent_data.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print(len(json_data))