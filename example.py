from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Initialize a language model. Requires OPENAI_API_KEY env variable.
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

researcher = Agent(
    role="Researcher",
    goal="Find the top AI trends",
    backstory="Expert analyst who knows the latest in AI",
    llm=llm,
)

writer = Agent(
    role="Writer",
    goal="Write a short article about an AI trend",
    backstory="Technology journalist",
    llm=llm,
)

trend_task = Task(
    description="Identify the most important AI trend for 2025.",
    expected_output="Name of one top trend",
    agent=researcher,
)

write_task = Task(
    description="Write a short paragraph summarizing {trend_task}.",
    expected_output="Paragraph summarizing the trend",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[trend_task, write_task],
    process=Process.sequential,
)

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
