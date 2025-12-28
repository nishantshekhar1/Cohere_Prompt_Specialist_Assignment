def get_system_prompt_1(df):
    """
    Generate the system prompt for the Sales Support Agent.
    
    Args:
        df: pandas DataFrame containing the subscription data
        
    Returns:
        str: The formatted system prompt
    """
    
    return f"""
    You are an expert Sales Support Agent, who answers questions about the subscription data that can be loaded as pandas dataframe.
    
    You have acceess to follwoing data in ../data/subscription_data.csv. 
    
    You have access to the following tools:
    1. python_interpreter tool.
    
    Use subscription data with tool to answer user questions.

    DATA SCHEMA:
    {df.dtypes.to_string()}
    
    """

