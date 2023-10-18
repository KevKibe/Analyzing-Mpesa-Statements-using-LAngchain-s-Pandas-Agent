import pandas as pd
import string
import re

class DataframeProcessor:
    def __init__(self, df):
        """
        Initializes the DataProcessor object with a DataFrame.
        """
        self.df = df

    def convert_to_datetime(self):
        """
        Converts the 'Completion Time' column of the DataFrame to datetime format.
        """
        self.df["Completion Time"] = pd.to_datetime(self.df["Completion Time"])
        self.df["Withdrawn"] = self.df["Withdrawn"].str.replace('-', '')  
        self.df["Paid In"] = self.df["Paid In"].str.replace(',', '')  
        self.df["Withdrawn"] = self.df["Withdrawn"].str.replace(',', '')
        self.df["Balance"] = self.df["Balance"].str.replace(',', '')
        self.df["Withdrawn"] = self.df["Withdrawn"].astype(float)
        self.df["Paid In"] = self.df["Paid In"].astype(float)
        self.df["Balance"] = self.df["Balance"].astype(float)
        return self.df

    def preprocess_text(self):
        """
        Preprocesses the 'Details' column of the DataFrame by converting text to lowercase and removing non-alphabetic characters.
        """
        if 'Details' in self.df.columns:
            self.df['Details'] = self.df['Details'].astype(str).str.lower()
            self.df['Details'] = self.df['Details'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
        return self.df

    def replace_nan_with_zero(self):
        """
        Replaces any NaN values in the DataFrame with zero.
        """
        self.df = self.df.fillna(0)
        return self.df
    
    def drop_unwanted_col(self):
        """
        Drops unwanted columns from the DataFrame.
        """
        self.df = self.df.drop(['Unnamed: 0','Receipt No.','Transaction Status'], axis=1)
        return self.df

    def add_payment_column(self):
        """
        Adds a 'Transaction Type' column to the DataFrame. The values in this column are derived from the first four alphanumeric words in the 'Details' column.
        """
        def extract_first_four_words(description):
            words = description.split()
            alphanumeric_words = [word for word in words if word.isalnum()]
            return ' '.join(alphanumeric_words[:2])
        
        self.df['Transaction Type'] = self.df['Details'].apply(extract_first_four_words)
        return self.df

    def extract_words_after_keywords(self, column_name):
        """
        Adds a 'Participant' column to the DataFrame. The values in this column are derived from the text following certain keywords in the specified column.
        """
        extracted_words_list = []

        pattern = r'\b(?:from|to|of)\b(.*?)(?:\.|$)'

        for index, row in self.df.iterrows():
            text = row[column_name].lower()  
            matches = re.findall(pattern, text)

            if matches:
                extracted_words_list.append(matches[0].strip()) 
            else:
                extracted_words_list.append("carrier") 

        self.df['Participant'] = extracted_words_list

        return self.df
    
    def process_details_column(self):
        """
        Removes carriage return characters from all columns and then drops the 'Details' column from the DataFrame.
        """
        self.df = self.df.replace('\r', '', regex=True)  
        self.df = self.df.drop('Details', axis=1)
        return self.df
    
    def rearrange_columns(self):
        """
        Rearranging columns for easier reading and analysis
        """
        desired_order = ['Completion Time', 'Transaction Type', 'Participant', 'Paid In', 'Withdrawn', 'Balance']
        columns_to_add = [col for col in desired_order if col not in self.df.columns]
        self.df = self.df.reindex(columns=[*self.df.columns, *columns_to_add])
        self.df = self.df[desired_order]
        return self.df
    
    def main(self):
        """
        Main method that calls all other methods to perform data processing on the DataFrame.
        """
        self.convert_to_datetime()
        self.preprocess_text()
        self.replace_nan_with_zero()
        self.drop_unwanted_col()
        self.add_payment_column()
        self.extract_words_after_keywords('Details')
        self.process_details_column()
        self.rearrange_columns()
        return self.df



