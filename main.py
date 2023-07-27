# THIS IS MAIN FILE FOR RUNNING THE 3D MESH
import matplotlib
matplotlib.use('TkAgg')  # Use the 'TkAgg' backend (or 'Qt5Agg', 'Qt4Agg', depending on your system)
import matplotlib.pyplot as plt
import sys
sys.path.append('scripts')
import data_reader
import mesh_utils

#ax1 = fig1.add_subplot()

for i in [
    data_reader.F,
    data_reader.B,
    data_reader.T
]:
    # ANNOTATION BLOCK:
    # Annotation properties
    x_position = 0.460895833333333
    y_position = 0.934735705808795
    width = 0.102343752284845
    height = 0.045846818463059
    text_color = [1, 0.411764705882353, 0.16078431372549]
    text_string = 'SQP304272-P12'
    line_style = 'none'
    font_size = 14

    # Create the textbox annotation
    plt.annotate(text_string,
                 xy=(x_position, y_position),
                 xytext=(x_position, y_position),
                 xycoords='figure fraction',
                 textcoords='figure fraction',
                 # bbox=dict(boxstyle=line_style, fc='w', ec='none'),
                 fontsize=font_size,
                 color='red')

        mesh_utils.refactor1(i)
        mesh_utils.meshplot(i)







