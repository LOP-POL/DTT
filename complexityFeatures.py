from View_data import sales
import pandas as pd
import matplotlib.pyplot as plt
from challenge_material.helper import *
import seaborn as sns


working_sales = sales
# Lists to add te row values in
bounding_box_list =  []
bounding_box_areas = []
bounding_box_heights = []
bounding_box_widths = []
cutting_lengths = []


for i in working_sales["file_name"]:
    bounding_box = get_dxf_bounds("challenge_material/10991360/" + i)
    c_length = get_cutting_length("challenge_material/10991360/" + i)
    

    box_height = bounding_box[0]
    box_width =  bounding_box[1]
    box_area =  box_height * box_width

    # Addign the lengths to the respective lists that will be the rows
    bounding_box_areas.append(box_area)
    bounding_box_widths.append(box_width)
    bounding_box_heights.append(box_height)
    bounding_box_list.append(bounding_box)
    cutting_lengths.append(c_length)

print(bounding_box_list)
print(len(working_sales))


new_columns = {
    "bounding_box_heights":bounding_box_heights,
    "bounding_box_widths":bounding_box_widths,
    "bounding_box_area":bounding_box_areas,
    "cutting_lengths":cutting_lengths
}

def insertIntoDf(df,new_col,rows):
    df.insert(len(df.columns),column=new_col,value=rows)


for key,value in new_columns.items():
    insertIntoDf(working_sales,key,value)

# creating new dataframe

complexity_df = pd.DataFrame(new_columns)
# added file name to use for future join

complexity_df["file_name"] = working_sales["file_name"]

# complexity_df.plot.scatter(x="file_name",y='bounding_box_area',alpha=0.5)

complexity_df[['bounding_box_heights','bounding_box_widths']].plot.box()

complexity_df['bounding_box_area'].plot.box()


plt.show()

# complexity_df.info()
# working_sales.info()




