import os
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

class Agent:
    def __init__(self, df, openai_api_key):
        self.df = df
        self.openai_api_key = openai_api_key

    def agent(self, query):
        openai_agent = create_pandas_dataframe_agent(OpenAI(temperature=0, api_key=self.openai_api_key), self.df, verbose=True)
        prompt = (
            """
        This dataset contains my mobile money transactions. Here's an overview of the columns:

        - **Completion Time:** Indicates the timestamp of each transaction.
        - **Paid In:** Represents funds added to the wallet. If it's an outgoing transaction, this field is NaN.
        - **Withdrawn:** Shows money taken out of the wallet. For transactions that credit the wallet, this field is NaN.
        - **Balance:** Reflects the wallet balance after each transaction.
        - **Transaction Type:** Describes the nature of the transaction. For example:
        - "buy bundles" is for purchasing internet data.
        - "customer transfer" is used when sending money to another person's wallet.
        - "mshwari withdraw" pertains to withdrawing money from a savings plan.
        - "funds received" indicates money credited to my wallet.
        - "perchant payment," "Pay Bill," and "Business Payment" signify transactions to a business wallet.
        - "mshwari deposit" is for moving money into the savings plan.
        - "deposit of" denotes crediting the wallet with cash.
        - "od loan" represents overdraft payment, while "Overdraft Of" signifies the transaction details.

        - **Participant:** Identifies the party involved in the transaction, either receiving funds into the wallet or sending them out.

        Please begin your response with "You have..." and provide a detailed explanation and if it is a question on spend specify whether it is sent or received.
       
        Please ensure your response is comprehensive.
        """
        + query
        )
        response = openai_agent.run(prompt)
        return response

