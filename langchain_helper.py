from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)


def get_few_shot_db_chain():
    db_user = "root"
    db_password = "root1"
    db_host = "localhost"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)
    llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    return chain


if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    response = chain.run("how many tshirts available?")
    print(response)