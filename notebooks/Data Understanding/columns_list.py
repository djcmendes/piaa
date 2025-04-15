math_columns = [f"PV{i}MATH" for i in range(1, 11)]


math_subscales = [
    f"PV{i}{suffix}"
    for i in range(1, 11)
    for suffix in ["MCCR", "MCQN", "MCSS", "MCUD", "MPEM", "MPFS", "MPIN", "MPRE"]
]

reading_columns = [f"PV{i}READ" for i in range(1, 11)]

science_columns = [f"PV{i}SCIE" for i in range(1, 11)]


def get_math_results(dataframe, math_columns):
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
    reading_results["Avg Reading Result"] = reading_results[reading_columns].mean(
        axis=1
    )
    reading_results = reading_results.drop(columns=reading_columns)

    return reading_results
