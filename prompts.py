from llama_index.core import PromptTemplate

instruction_str = """\
    1. Convert the query to executable Pyhton code usinng Pandas
    2. The final line of the code should be a Python expression that can be called with the 'eval()' funnctionn
    3. The code should represent a solution to the query
    4. Print onnly th expression
    5. Do not quote the expression
"""

new_prompt = PromptTemplate(
    """\
        You are working with pandas dataframe in Python.
        The name of the dataframe is 'df'.
        This is the result of 'print(df.head())':
        {df_str}
        
        Follow these instructions:
        {instruction_str}
        
        Query: {query_str}
        
        Expression: 
    """
)


context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about world population statistics and details about a country. """