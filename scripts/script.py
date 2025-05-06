import pandas as pd

#student = pd.read_sas(
#    "./CY08MSP_STU_QQQ.SAS7BDAT", format="sas7bdat"
#)

#student.to_csv("student2022.csv", index=False)

data = pd.read_sas(
    "./cy07_msu_stu_qqq.sas7bdat", format="sas7bdat"
)

print("stu 2018 read :", flush=True)

data.to_csv("student2018.csv", index=False)

print("stu 2018 write :", flush=True)

data = pd.read_sas(
    "./cy07_msu_tch_qqq.sas7bdat", format="sas7bdat"
)
print("teacher2018 read :", flush=True)
data.to_csv("only_teacher2018.csv", index=False)
print("teacher2018 write :", flush=True)

data = pd.read_sas(
    "./cy6_ms_cmb_stu_qqq.sas7bdat", format="sas7bdat"
)

print("student2015 read :", flush=True)
data.to_csv("student2015.csv", index=False)
print("student2015 write :", flush=True)




#  PISA2012_SAS_student2012.sas      SAS_STU_QQQ2018.zip
#  PUF_SAS_COMBINED_CMB_STU_QQQ2015  SAS_TCH_QQQ2018
#  SAS_STU_QQQ2018