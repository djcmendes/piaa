import pandas as pd

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath('../src')) # Add the src directory to the Python path

from pisadatamap.pisadatamap import PISADataMap

data_map = PISADataMap('../databases/2018/teacher_data_structure_2018.csv')

# List of columns to keep
columns_to_keep = [
'PV1READ', 'PV2READ', 'PV3READ', 'PV4READ', 'PV5READ', 'PV6READ', 'PV7READ', 'PV8READ', 'PV9READ', 'PV10READ',
'PV1SCIE', 'PV2SCIE', 'PV3SCIE', 'PV4SCIE', 'PV5SCIE', 'PV6SCIE', 'PV7SCIE', 'PV8SCIE', 'PV9SCIE', 'PV10SCIE',
'PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV6MATH', 'PV7MATH', 'PV8MATH', 'PV9MATH', 'PV10MATH'
]

combined_columns = list(data_map.map_enum['map_enum'].keys()) + columns_to_keep

teacher_student = pd.read_csv('../databases/2018/teacher_student2018.csv')

filtered_teacher_student = teacher_student[combined_columns]
filtered_teacher_student.to_csv('../databases/2018/teacher2018.csv', index=False)

filtered_teacher_student.head(20)




