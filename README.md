# Description
This is a streamlit app for analyzing Mpesa Statements using Langchain Pandas Agent.

## Installation
- Clone the repository `git clone https://github.com/KevKibe/Analyzing-Mpesa-Statements-using-Langchain-Pandas-Agent.git`
- Install requirements `pip install -r requirements.txt`
- Run the command `streamlit run app.py` to launch the app on localhost.

## Usage 
- Enter your OpenAI API Key in the sidebar.
- Upload your M-Pesa Statement.
- Enter a query in the provided text area and click the "generate" button.

## Screenshots
## The Agent getting an understanding of the Statement and the columns
![image](https://github.com/KevKibe/Analyzing-Mpesa-Statements-using-Langchain-Pandas-Agent/assets/86055894/dd49c787-9812-43f6-9990-b2db6fbdd9da)
## Finding out how much I have spent on buying Internet Bundles
![image](https://github.com/KevKibe/Analyzing-Mpesa-Statements-using-Langchain-Pandas-Agent/assets/86055894/f27da468-8258-4a63-94ca-8ddcae92c5de)
## Finding out how much money I have sent to a specific person in total. 
![WhatsApp Image 2023-10-18 at 13 20 10](https://github.com/KevKibe/Analyzing-Mpesa-Statements-using-Langchain-Pandas-Agent/assets/86055894/08cb8d1c-5293-434b-9c53-5a15074afbf1)
## Finding out how much money I have sent to a another specific person in total.
![WhatsApp Image 2023-10-18 at 13 22 31](https://github.com/KevKibe/Analyzing-Mpesa-Statements-using-Langchain-Pandas-Agent/assets/86055894/d1329bde-7a34-4225-a55c-f58c8a2e9420)

## Troubleshooting
- Solutions to common errors.
1. `jpype._jvmfinder.JVMNotFoundException: No JVM shared library file (libjvm.so) found. Try setting up the JAVA_HOME environment variable properly.` -
 means you do not have Java Virtual Machine installed in your environment, download it from this [site](https://www.oracle.com/ke/java/technologies/downloads/) and install.
2. `Retrying langchain.llms.openai.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for text-davinci-003 in organization org-X7JScsPiE6OYrh68GPSZOkVJ on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..` - means your agent has exceeded rate limit of 3 calls/min to the OpenAI API and you need to setup a payment method to increase rate limit.
