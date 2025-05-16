"""
 This file contains the PISADataMap class.

 :py:class:`piaa.pisadatamap.pisadatamap.PISADataMap` instance.
"""
from enum import Enum
import pandas as pd


class PISADataMap:
    map_enum = None

    def __init__(self, file_path='../../../databases/2018/student_data_structure_2018.csv'):
        """
        Constructor

        :param file_path: data file path
        :type file_path: string
        """
        # load data
        map_df = pd.read_csv(file_path, na_values=['NA', 'n/a', ''], delimiter=';')

        columns_to_drop = map_df.columns[2:] # Drop all columns except the first two
        map_df = map_df.drop(columns=columns_to_drop) # Drop the columns
        map_df = map_df.iloc[2:] # Drop the first two rows, we only need the values
        map_df = map_df.dropna(subset=[map_df.columns[0]]) # Drop rows with missing values in the first column

        self.map_enum = Enum('MapEnum', {row.iloc[0]: row.iloc[1] for index, row in map_df.iterrows()})  # Setup enum with key, values of the codebook

    def rename_keys(self, df):
        """
        Rename keys of a dataframe with map_enum

        :param df: dataframe to be renamed
        :type df: pandas.DataFrame

        :rtype: df
        """
        return df[list(map(lambda c: c.name, self.map_enum))].rename(columns={e.name: e.value for e in self.map_enum})


# how to use
#data_map = PISADataMap('../../databases/2018/student_data_structure_2018.csv')
#student = pd.read_csv('../../databases/2018/student2018.csv', nrows=1000)
#print(list(map(lambda c: c.name, data_map.map_enum)))

#student = data_map.rename_keys(student)
#print(student.iloc[20])