import os
import asyncio
import pandas as pd
from dotenv import load_dotenv

from prompts import new_prompt, instruction_str, context

# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# from llama_index.core.query_engine import PandasQueryEngine
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core import Settings
from llama_index.llms.groq import Groq  # <-- Import LlamaIndex's Groq wrapper


# from groq import Groq

from note_engine import notes_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.agent.workflow import FunctionAgent



load_dotenv()
# Configure LlamaIndex to use Groq by default
Settings.llm = Groq(
    model="openai/gpt-oss-120b",  # Or your preferred active Groq model
    api_key=os.getenv('GROQ_API_KEY')
)


def load_data():
    population_path = os.path.join("data", "WorldPopulation2023.csv")
    population_df =pd.read_csv(population_path)

    # print(population_df.head())

    return population_df


async def agent():

    #load the data in pandas
    population_df = load_data()

    population_query_engine = PandasQueryEngine(df=population_df,
                                                verbose=True,
                                                instruction_str=instruction_str,
                                                new_prompt=new_prompt
                                                )


    # query_engine.update_prompts({"pandas_prompt": new_prompt})

    tools = [
        notes_engine,
        QueryEngineTool(query_engine=population_query_engine,
                        metadata=ToolMetadata(
                            name="population_data",
                            description="That gives information at the world population and demographics"
                        ),
                        )
    ]



    llm = Groq(
        model="openai/gpt-oss-120b",  # Or your preferred active Groq model
        # model="llama-3.3-70b-versatile",  # Or your preferred active Groq model
        api_key=os.getenv('GROQ_API_KEY')
    )
    agent = FunctionAgent(
        tools=tools,
        llm=llm,
        verbose=False,
        streaming=False,
        context=context
    )



    # context = Context(agent)

    while (prompt := input("Enter a prompt (q to quit): ")) != "q":
        result = await agent.run(prompt,
                                 max_iterations=5
                                 )
        print(result)

    return population_query_engine



def use_groq(content):
    # Retrieve the API key from the environment
    api_key = os.getenv("GROQ_API_KEY")
    print("API Key loaded:", bool(api_key))

    load_data()

    try:
        client = Groq()
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": "Ping"}]
        )
        print("Connection Successful:", completion.choices[0].message.content)
    except Exception as e:
        print("Detailed Error:", type(e).__name__, e)



    print('\n>', content)
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
       messages=[
           {
               "role": "user",
               "content": content,
           }
       ],
       model="openai/gpt-oss-120b",
    )
    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    asyncio.run(agent())


