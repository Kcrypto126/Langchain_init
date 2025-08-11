import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model

load_dotenv()

text = """
My name is John Doe and I am a software engineer.
I have 10 years of experience in software development.
I am a full stack developer.
"""

if __name__ == "__main__":
    print("Hello, Langchain!")
    # print(text)
    # print(os.environ["OPENAI_API_KEY"])

    summary_template = """
    You are a helpful assistant that summarizes the user's profile.
    Here is the user's profile:
    {text}
    Please summarize the user's profile in 2-3 sentences.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["text"],
        template=summary_template,
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Use the modern invoke method instead of deprecated run method
    response = llm.invoke(summary_prompt_template.format(text=text))
    print(response.content)