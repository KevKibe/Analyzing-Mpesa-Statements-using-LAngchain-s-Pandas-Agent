import tabula
import pandas as pd
from tabulate import tabulate

class PDFProcessor:
    """
    A class for processing PDF data containing tables.

    Parameters:
    - pdf_file_path (str): The path to the PDF file.
    - start_page (int): The starting page for table extraction.
    - end_page (int): The ending page for table extraction.
    - output_csv_file (str): The path to save the processed data as a CSV file.
    """

    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path


    def extract_and_concatenate_tables(self):
        """
        Extract tables from the specified pages of the PDF and concatenate them into a DataFrame.
        """
        data = tabula.read_pdf(self.pdf_file_path, pages = "all")
        dataframes = []

        for i in range(2, len(data), 2):
            item = data[i]
            dataframes.append(item)

        self.merged_df = pd.concat(dataframes, ignore_index=True)
        return self.merged_df

    def display_dataframe(self):
        """
        Display the processed DataFrame as a table and print additional information.
        """
        print(tabulate(self.merged_df))
        print(self.merged_df.columns)
        print(self.merged_df.info())


    def process_pdf(self):
        """
        Execute the entire PDF data processing workflow.
        """
        self.extract_and_concatenate_tables()
        # self.display_dataframe()
        return self.merged_df



