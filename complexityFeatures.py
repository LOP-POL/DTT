from dataCleanUpFinal import df
import pandas as pd
import matplotlib.pyplot as plt
from challenge_material.helper import *
import seaborn as sns


working_sales = df
# Lists to add te row values in
bounding_box_list =  []
bounding_box_areas = []
bounding_box_heights = []
bounding_box_widths = []
cutting_lengths = []
number_of_holes = []
number_of_edges = []
number_of_vertices = []
complexity_measure = []

path = "challenge_material/10991360/"

new_columns = {
    "bounding_box_heights":bounding_box_heights,
    "bounding_box_widths":bounding_box_widths,
    "bounding_box_area":bounding_box_areas,
    "cutting_lengths":cutting_lengths,
    "number_of_holes":number_of_holes,
    "number_of_edges":number_of_edges,
    "number_of_vertices":number_of_vertices,
    "complexity_measure":complexity_measure
}

def insertIntoDf(df,new_col,rows):
    df.insert(len(df.columns),column=new_col,value=rows)

# creating new dataframe

weight = {
    "edges":0.03,
    "vertices":0.05,
    "holes":0.1
}

def complexityMeasure(cutting_lengths,number_of_edges,number_of_vertices,number_of_holes,bounding_box_heights,bounding_box_widths,area):
    rcl = cutting_lengths * (
        1+
        weight["edges"]*number_of_edges
        +
        weight["vertices"]*number_of_vertices
        +
        weight["holes"]*number_of_holes
        )
    areaPenalty = 1
    if bounding_box_widths >160 and bounding_box_heights > 160:
        areaPenalty += 0.02

    score = round(math.log(rcl + area*areaPenalty),2)
    return score


def complexityMeasureSeries():
    result = []
    for i in complexity_df.itertuples():
        
        rcl = i.cutting_lengths * (
            1+
            weight["edges"]*i.number_of_edges
            +
            weight["vertices"]*i.number_of_vertices
            +
            weight["holes"]*i.number_of_holes
            )
        areaPenalty = 1
        if i.bounding_box_widths >160 and i.bounding_box_heights > 160:
            areaPenalty += 0.02
        score = math.log(rcl + i.bounding_box_area*areaPenalty)

        result.append(round(score,2))
    return result


for i in working_sales["file_name"]:
    bounding_box = get_dxf_bounds(path + i)
    c_length = get_cutting_length(path + i)
    n_holes = get_number_of_holes(path + i)
    n_egdes_and_vertices = count_edges_and_vertices(path + i)
    n_edges = n_egdes_and_vertices[0]
    n_vertices = n_egdes_and_vertices[0]

    box_height = bounding_box[0]
    box_width =  bounding_box[1]
    box_area =  box_height * box_width

    complexity_m = complexityMeasure(c_length,n_edges,n_vertices,n_holes,box_height,box_width,box_area)

    # Addign the lengths to the respective lists that will be the rows
    bounding_box_areas.append(box_area)
    bounding_box_widths.append(box_width)
    bounding_box_heights.append(box_height)
    bounding_box_list.append(bounding_box)
    cutting_lengths.append(c_length)
    number_of_holes.append(n_holes)
    number_of_vertices.append(n_vertices)
    number_of_edges.append(n_edges)
    complexity_measure.append(complexity_m)

for key,value in new_columns.items():
    insertIntoDf(working_sales,key,value)

complexity_df = pd.DataFrame(new_columns)
# added file name to use for future join

complexity_df["file_name"] = working_sales["file_name"]


# complexity_df[['bounding_box_heights','bounding_box_widths']].plot.box()

# complexity_df['bounding_box_area'].plot.box()
print(complexity_df)

print(complexity_df.describe())

print(complexity_df.info())


# # Plot bounding box area
# plt.figure(figsize=(10, 6))
# plt.plot(complexity_df["file_name"], complexity_df['bounding_box_area'], marker='o', linestyle='-', color='b')
# plt.xlabel('file_name')
# plt.ylabel('Bounding Box Area')
# plt.title('Bounding Box Area per File')
# plt.xticks(rotation=90)  # Rotate file names for better readability
# plt.tight_layout()  # Adjust layout to make sure everything fits
# plt.show()
# # plt.show()








