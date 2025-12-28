# Sales Support Agent

This project implements a Sales Support Agent using LangChain and Cohere. It includes an evaluation pipeline to measure performance against a golden dataset.

## Setup

### Prerequisites

- Python 3.10+ (I have tested on 3.13.5 and MacBook M3 Pro, Sequoia 15.6.1)
- A Cohere API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nishantshekhar1/Cohere_Prompt_Specialist_Assignment.git
   cd Cohere_Prompt_Specialist_Assignment
   ```
2. Open the project in your preferred IDE (e.g., VSCode).
3. Open the terminal in your IDE.
4. Create a virtual environment:
   ```bash
   python3 -m venv .venv 
   source .venv/bin/activate  
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. create .env file in the root directory of the project and add your Cohere API key (You will need a Cohere API key to run the code):
   ```bash
   touch .env
   ```
   Add the following line to `.env`:
   ```bash
   COHERE_API_KEY=your_cohere_api_key_here
   ```
7. Open sales_agent_ReAct_iteration_2.ipynb in your IDE.
8. Select Kernel in your IDE to use the virtual environment.
9. Click Run All(at the top of the notebook) in sales_agent_ReAct_iteration_2.ipynb notebook. If you are asked to install ipykernel, please install it and the click Run All again.

### Project Structure

- `notebooks/`: Contains Jupyter notebooks with the agent implementation and evaluation logic.
- `prompts/`: Python files containing system prompts and prompt engineering iterations.
- `data/`: CSV and JSON files for subscription data and evaluation benchmarks.


## Prompt engineering approach:
- PERSONA(Sales Support Agent), 
- GOAL(Answer question about subscrition data)
- TOOLS the agent has access to (python interpreter tool to execute dataframe code.) 
- FEW SHOT PROMPTING to help agent understand the kind of response expected from it. 
- EXPLAIN DATA to mitigate HALLICUNATION. - Agent was hallucinating while filtering on columns. E.g. Agent used "Active" instead of "active" for Active Subscriptions(status). This moved ACCURACY from 60% to 80%.
- IMPORTANT RULES(CRITICAL INSTRUCTIONS) section to guide agent on how to answer questions.
- Always use the 'python_interpreter' tool data analysis. - To limit hallucination.
- Prompt to not return only number. List the names/entities behind the number. - This is make response coherent with golden answers.
- Added instructions to deal with VAGUE questions. Prompted agent to mention question is ambiguous and what assimptions it made to answer the question. - This is to better align the agent's response with the evaluation criteria. FOR PRODUCTION: Going forward we can add a human-in-the-loop for questions that are vague.
- Added instrcutions for how python code should be verbose and explain each step. Print each step of the code execution. This to help agent understand the code and provide better explanation for its answer (as the golden answers do not only provide the exact answer but provide more context to the answer).
- SECURITY GUARDRAILS to prevent PII disclosure - Explicit mention of not disclosing PII in the prompt.
- Use a ReAct Agent Strategy for the agent to Reason, Act and Observe to provide a complete response as the golden answers are not only providing a concise answer but supporting context as well. - I have used Langchain create_agent which implements ReAct.

### Evaluation Design:
- Main focus is Accuracy.
- Given golden answers are not concise answers or one word answers it makes sense to LLM-as-a-Judge to evaluate the agent's responses.
- Judge marks the AGENT's response as PASS or FAIL based on the following criteria:
    - if Agent's response satisfies the evaluation criteria in evaluation_data.json
    - if Agent's response conveys the same meaning as golden_answer in evaluation_data.json
    - if Agent's response has disclosed PII or not
    - if Agent's response has handled ambiguous questions or not
    - the agent's reponse does not need to match the golden answer word-for-word
- Given most of questions can have one word answers as they are mathematical calculations. We can consider concise answers for evaluation for future. This can help us quickly evaluate how well the agent is able to use its tools.

### Evaluation Insights:
- For data analysis agent's like this, it's important to provide explanation of the data in prompt to prevent hallucination. e.g. Agent was hallucinating while filtering on columns. E.g. Agent used "Active" instead of "active" for Active Subscriptions(status). I provided all the unique values of the important columns in the prompt. This helped agent to avoid hallucination and increased ACCURACY from 60% to 80%. - Here, I could have provided the whole table as a reference to the agent but I do not think this will scale in production as the tables can be very large in actual world.
- Prompted the agent to provide explanation for the answer helped improve accuracy. - explanation helped with evaluation criteria provided in the evaluation data.
- Provided explicit mention not to disclose PII and how to handle ambiguous questions helped improve accuracy.
- My agent struggled with questions that were not clear. e.g. question: "Show me companies that are not using their subscriptions effectively.". Answers were not statisfying the evaluation criteria.
- My agent also hallucinated while generating python code. Agent made up column values like "Active" instead of "active" for Active Subscriptions(status). As talked in first point. Providing all the unique values of the important columns in the prompt helped agent to avoid hallucination.

## Iterations you made:
- Started with simple prompt with PERSONA, GOAL and TOOLS the agent can use to move fast and have something working first. This gave accuracy of 50%.
- Then I added IMPORTANT RULES to guide agent on how to answer questions, SECURITY GUARDRAILS to prevent PII disclosure, and how to handle ambiguous questions. This is better to match the evaluation criteria in evaluation_data.json and requirements of this assessment. This improved accuracy of 60%.
- Then I added FEW SHOT PROMPTING to better match the results in golden_answer as few shot prompting can help steer the agent towards the expected output.
- Then I added essential column(unique) values in the prompt to help agent avoid hallucination and provide better context for generation of correct for data analysis. This helped reduce hallucination. This improved accuracy of 80%.
- This did make the prompt bigger and more complex.

## Next improvements:
- Given more time: I would improve the prompt for vague questions. Maybe add more examples or provide step-by-step instructions how to approach vague questions.
- Move from pre-built langchain agent to langgraph based agent to better control the flow and context of the agent. This can help me steer the agent response to better align with the golden answers and evaluation criteria.


### Important Notes:
1. iteration_1_accuracy_metric.txt and iteration_2_accuracy_metric.txt are the accuracy metrics for iteration 1 and iteration 2 respectively. They are under notebooks folder.
2. evaution run with agent response is for iteration 1 and 2 is in evaluation_results_report_iteration_1.csv and evaluation_results_report_iteration_2.csv respectively. They are under notebooks folder. Going forward we can run add golden answer as well seperate column for agent response explanation in the evaluation data.
3. Currently the evalution is only done for accuracy. Going forward we can calculate other metrics like Completeness of answer and if the agents grows complex we can evaluate tool call trajectory evaluation. We can have metrics for PII Saftety too.






