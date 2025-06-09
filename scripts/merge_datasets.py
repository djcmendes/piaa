"""
import pandas as pd

columns_to_keep = [
'PV1READ', 'PV2READ', 'PV3READ', 'PV4READ', 'PV5READ', 'PV6READ', 'PV7READ', 'PV8READ', 'PV9READ', 'PV10READ',
'PV1SCIE', 'PV2SCIE', 'PV3SCIE', 'PV4SCIE', 'PV5SCIE', 'PV6SCIE', 'PV7SCIE', 'PV8SCIE', 'PV9SCIE', 'PV10SCIE',
'PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV6MATH', 'PV7MATH', 'PV8MATH', 'PV9MATH', 'PV10MATH',
'CNT', 'CNTSCHID', 'REPEAT', 'ST001D01T'
]

# Load the datasets
def get_dataset(columns_to_keep):
    merged_df1 = pd.read_csv('../databases/2018/student2018.csv')
    #merged_df1 = merged_df1[columns_to_keep]
    merged_df2 = pd.read_csv('../databases/2018/only_teacher2018.csv')
    #merged_df1.merge(merged_df2, on=['CNT', 'CNTSCHID'], how='outer')
    return pd.merge(merged_df1, merged_df2, on=['CNT', 'CNTSCHID'])

# Save the merged dataset to a CSV file
teacher_student = get_dataset(columns_to_keep)
teacher_student.to_csv('../databases/2018/teacher_student2018.csv', index=False)
"""


import pandas as pd

columns_to_keep = [
'PV1READ', 'PV2READ', 'PV3READ', 'PV4READ', 'PV5READ', 'PV6READ', 'PV7READ', 'PV8READ', 'PV9READ', 'PV10READ',
'PV1SCIE', 'PV2SCIE', 'PV3SCIE', 'PV4SCIE', 'PV5SCIE', 'PV6SCIE', 'PV7SCIE', 'PV8SCIE', 'PV9SCIE', 'PV10SCIE',
'PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV6MATH', 'PV7MATH', 'PV8MATH', 'PV9MATH', 'PV10MATH',
'CNT', 'CNTSCHID', 'REPEAT', 'ST001D01T', 'CNTSTUID'
]

# Function to load and merge datasets in chunks
def init_target_csv():
    with open("../databases/2018/teacher_student2018.csv", 'w') as file:
        pass # Do nothing, just open and close the file

    df1 = pd.read_csv('../databases/2018/student2018.csv', nrows=10)
    df2 = pd.read_csv('../databases/2018/only_teacher2018.csv', nrows=10)
    
    df1 = df1[columns_to_keep]
    
    df_result = pd.DataFrame(columns=(df1.columns.append(df2.columns)).unique())
    df_result.to_csv("../databases/2018/teacher_student2018.csv", index_label=False)

# Function to load and merge datasets in chunks
def get_dataset_in_chunks(chunk_size):
    chunks = []
    i=0
    for chunk in pd.read_csv('../databases/2018/student2018.csv', chunksize=chunk_size):
        i=i+1
        print("i=",i,flush=True)
        chunk = chunk[columns_to_keep]
        
        merged_chunk = pd.merge(chunk, pd.read_csv('../databases/2018/only_teacher2018.csv'), on=['CNT', 'CNTSCHID'])
        merged_chunk.to_csv("../databases/2018/teacher_student2018.csv", mode="a", header=False, index=False)
        #print(merged_chunk.head(), flush=True)
        #chunks.append(merged_chunk)
    #return pd.concat(chunks, ignore_index=True)

# Define the chunk size
chunk_size = 50000 # Adjust the chunk size based on your memory capacity

init_target_csv()
# Perform the merge in chunks
get_dataset_in_chunks(chunk_size)

print("Merge completed and saved to 'teacher_student2018.csv'.")

df = pd.read_csv('../databases/2018/teacher_student2018.csv')



