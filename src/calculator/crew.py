from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from pydantic import config # Veya tercih ettiğin model
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Calculator():
    """FirstProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def calculation_manager(self) -> Agent:
        return Agent(config=self.agents_config['calculation_manager'])

    @agent
    def addition_specialist(self) -> Agent:
        return Agent(config=self.agents_config['addition_specialist'])

    @agent
    def subtraction_specialist(self) -> Agent:
        return Agent(config=self.agents_config['subtraction_specialist'])

    @agent
    def multiplication_specialist(self) -> Agent:
        return Agent(config=self.agents_config['multiplication_specialist'])

    @task
    def solve_math_problem(self) -> Task:
        return Task(config=self.tasks_config['solve_math_problem'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.addition_specialist(), self.subtraction_specialist(), self.multiplication_specialist()],
            tasks=self.tasks,   # Tüm taskları otomatik alır
            process=Process.hierarchical, 
            manager_agent=self.calculation_manager(),
            verbose=True
        )
