"""
 This file contains the PISADataMap class.

 :py:class:`piaa.pisadatamap.pisadatamap.PISADataMap` instance.
"""
from enum import Enum
import pandas as pd

class PISADataMap:
    map_enum = None

    def __init__(self, file_path=['../../../databases/2018/student_data_structure_2018.csv']):
        """
        Constructor

        :param file_path: data file path(s)
        :type file_path: string|list
        """

        if isinstance(file_path, str):
            file_paths = [file_path]
        else:
            file_paths = file_path

        map_entries = []

        for path in file_paths:
            try:
                df = pd.read_csv(path, na_values=['NA', 'n/a', ''], delimiter=';')
                df = df.drop(df.columns[2:], axis=1)  # Keep only first two columns
                df = df.iloc[2:]  # Drop first two rows
                df = df.dropna(subset=[df.columns[0]])  # Drop rows with missing keys
                map_entries.extend([(row.iloc[0], row.iloc[1]) for _, row in df.iterrows()])
            except Exception as e:
                print(f"Failed to load {path}: {e}")

        if not map_entries:
            raise ValueError("None of the provided file paths could be loaded.")

        self.map_enum = Enum('MapEnum', dict(map_entries))

    def get(self, col):
        mapped_value = self.map_enum.__members__.get(col, None)
        return mapped_value.value if mapped_value else col

    def rename_keys(self, df):
        """
        Rename keys of a dataframe with map_enum

        :param df: dataframe to be renamed
        :type df: pandas.DataFrame

        :rtype: df
        """
        return df[list(map(lambda c: c.name, self.map_enum))].rename(columns={e.name: e.value for e in self.map_enum})

    def as_dict(self) -> dict:
        """
        Converts enum_map to dict

        Args:
            enum_map (Enum): The Enum class or instance to be converted.

        Returns:
            dict: A dictionary mapping member names to member values.
        """
        # This dictionary comprehension is the most efficient and Pythonic way to do it.
        return {member.name: member.value for member in self.map_enum}


# how to use
#data_map = PISADataMap('../../databases/2018/student_data_structure_2018.csv')
#student = pd.read_csv('../../databases/2018/student2018.csv', nrows=1000)
#print(list(map(lambda c: c.name, data_map.map_enum)))

#student = data_map.rename_keys(student)
#print(student.iloc[20])