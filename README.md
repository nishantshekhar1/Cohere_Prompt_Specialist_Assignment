# Sales Support Agent

This project implements a Sales Support Agent using LangChain and Cohere. It includes an evaluation pipeline to measure performance against a golden dataset.

## Setup

### Prerequisites

- Python 3.10+ (I have tested on 3.13.5 and MacBook M3 Pro, Sequoia 15.6.1)
- A Cohere API Key

### Installation

1. **Create a Virtual Environment**

   It is recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv .venv 
   source .venv/bin/activate  
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**

   Create a `.env` file in the root directory of the project and add your Cohere API key:

   ```bash
   touch .env
   ```

   Add the following line to `.env`:

   ```
   COHERE_API_KEY=your_cohere_api_key_here
   ```

## Usage

1. **Run the Notebooks**

   Start the Jupyter Notebook server:

   ```bash
   jupyter notebook
   ```

   OR use vscode with ipykernel extension to run the notebooks.

   Navigate to the `notebooks/` directory and open the latest sales agent notebook (e.g., `sales_agent_ReAct_iteration_3.ipynb`).

   Note:  sales_agent_ReAct_iteration_3.ipynb is the final notebook that implements the sales agent using ReAct. sales_agent_ReAct_iteration_1.ipynb and sales_agent_ReAct_iteration_2.ipynb are the first and second iterations of the sales agent. I have use langchain create_agent which implements ReAct.

2. **Evaluation**

   The notebooks contain built-in evaluation loops that compare the agent's responses against a golden dataset (`data/evaluation_data.json`).

## Project Structure

- `notebooks/`: Contains Jupyter notebooks with the agent implementation and evaluation logic.
- `prompts/`: Python files containing system prompts and prompt engineering iterations.
- `data/`: CSV and JSON files for subscription data and evaluation benchmarks.
