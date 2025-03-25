import pandas as pd

student = pd.read_sas(
    "./CY08MSP_STU_QQQ.SAS7BDAT", format="sas7bdat"
)

student.to_csv("student2022.csv", index=False)