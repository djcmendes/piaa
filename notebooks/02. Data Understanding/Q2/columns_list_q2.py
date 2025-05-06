import numpy as np

math_columns = [f"PV{i}MATH" for i in range(1, 11)]

math_subscales = [
    f"PV{i}{suffix}"
    for i in range(1, 11)
    for suffix in ["MCCR", "MCQN", "MCSS", "MCUD", "MPEM", "MPFS", "MPIN", "MPRE"]
]

science_columns = [f"PV{i}SCIE" for i in range(1, 11)]

global_columns = [f"PV{i}GLCM" for i in range(1, 11)]

reading_columns = [f"PV{i}READ" for i in range(1, 11)]

reading_subscales = [
    f"PV{i}{suffix}"
    for i in range(1, 11)
    for suffix in ["RCLI", "RCUN", "RCER", "RTSN", "RTML"]
]

def get_math_results(dataframe, math_columns, round = None):
    math_results = dataframe.copy()
    math_results["Avg Math Result"] = math_results[math_columns].mean(axis=1)
    math_results = math_results.drop(columns=math_columns)

    return math_results

def get_science_results(dataframe, science_columns):
    scie_results = dataframe.copy()
    scie_results["Avg Science Result"] = scie_results[science_columns].mean(axis=1)
    scie_results = scie_results.drop(columns=science_columns)

    return scie_results

def get_reading_results(dataframe, reading_columns):
    reading_results = dataframe.copy()
    reading_results["Avg Reading Result"] = reading_results[reading_columns].mean(axis=1)
    reading_results = reading_results.drop(columns=reading_columns)

    return reading_results

def get_avg_results(dataframe, columns, type="", round=None):
    avg_results = dataframe.copy()

    avg_results[f"Avg {type} Result"] = avg_results[columns].mean(axis=1)

    match round:
        case "Rounded":
            avg_results[f"Avg {type} Result Rounded"] = avg_results[f"Avg {type} Result"].round()  # Standard rounding
        case "Floor":
            avg_results[f"Avg {type} Result Floor"] = np.floor(avg_results[f"Avg {type} Result"])  # Floor rounding
        case "Ceil":
            avg_results[f"Avg {type} Result Ceil"] = np.ceil(avg_results[f"Avg {type} Result"])  # Ceiling rounding

    return avg_results

def drop_columns(dataframe):
    """
    dataframe = dataframe.drop(columns=math_subscales)
    2018 database does not have the math scales
    """
    dataframe = dataframe.drop(columns=math_columns)
    dataframe = dataframe.drop(columns=reading_columns)
    dataframe = dataframe.drop(columns=global_columns)
    dataframe = dataframe.drop(columns=science_columns)
    dataframe = dataframe.drop(columns=reading_subscales)

    return dataframe