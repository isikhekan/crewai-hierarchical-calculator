# Calculator Crew

Welcome to the Calculator Crew project, powered by [crewAI](https://crewai.com).

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/calculator/config/agents.yaml` to define your agents
- Modify `src/calculator/config/tasks.yaml` to define your tasks
- Modify `src/calculator/crew.py` to add your own logic, tools and specific args
- Modify `src/calculator/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```


The crew consists of the following agents:

* ** Calculation Manager:** The brain of the operation. It analyzes the user's input (e.g., "I want to multiply 15 by 25"). It doesn't perform the math itself; instead, it plans the execution and delegates the task to the correct specialist.
* ** Addition Specialist:** Focuses solely on addition operations.
* ** Subtraction Specialist:** Focuses solely on subtraction operations.
* ** Multiplication Specialist:** Focuses solely on multiplication operations.

## How It Works

1. **Input:** The user provides a single natural language prompt.
2. **Analysis:** The `Calculation Manager` receives the prompt and determines which mathematical operation is required.
3. **Delegation:** The Manager uses built-in delegation tools to assign the specific calculation to the relevant specialist (e.g., sending a multiplication task strictly to the Multiplication Specialist).
4. **Execution & QA:** The assigned specialist performs the calculation and sends it back to the Manager. The Manager reviews the output against the expected criteria and presents the final, clean answer to the user.


Clone the repository:
    ```bash
   git clone [https://github.com/isikhekan/crewai-hierarchical-calculator.git](https://github.com/isikhekan/crewai-hierarchical-calculator.git)
   cd crewai-hierarchical-calculator
