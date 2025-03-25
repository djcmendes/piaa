math_columns = [f"PV{i}MATH" for i in range(1, 11)]


math_subscales = [
    f"PV{i}{suffix}"
    for i in range(1, 11)
    for suffix in ["MCCR", "MCQN", "MCSS", "MCUD", "MPEM", "MPFS", "MPIN", "MPRE"]
]

reading_columns = [f"PV{i}READ" for i in range(1, 11)]

science_columns = [f"PV{i}SCIE" for i in range(1, 11)]
