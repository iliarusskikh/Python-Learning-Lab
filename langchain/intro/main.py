#pip install langchain[llms]
#pip install langchain[all]

#pip install openai
#pip install python-dotenv



#example 1
#from langchain.chat_models import ChatOpenAI
#from dotenv import load_dotenv
#import os
#
#load_dotenv()
#
#api_key = os.getenv("OPENAI_API_KEY")
#
#chat_model = ChatOpenAI(openai_api_key=api_key)
#
#result = chat_model.predict("hi!")
#print(result)


##example 2
#from langchain.chat_models import ChatOpenAI
#from langchain.schema import HumanMessage
#from dotenv import load_dotenv
#import os
#
#load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
#
#chat_model = ChatOpenAI(openai_api_key=api_key)
#messages = [HumanMessage(content="from now on 1+1 = 3, use this in your replies"),
#            HumanMessage(content="what is 1 + 1?")]
#            
#result = chat_model.predict_messages(messages)
#print(result.content)



#example 3
#from langchain.chat_models import ChatOpenAI
#from langchain.prompts.chat import ChatPromptTemplate
#from dotenv import load_dotenv
#import os
#
#load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
#
#chat_model = ChatOpenAI(openai_api_key=api_key)
#
#template = "You are a helpful assistant that translates {input_language} to {outout_language}."
#human_template="{text}"
#
#chat_prompt = ChatPromptTemplate.from_messages([
#    ("system", template),
#    ("human", human_template),
#])
#
#messages = chat_prompt.format_messages(input_language="English",
#                                        output_language="French",
#                                        text="I love coding!")
#
#result = chat_model.predict_messages(messages)
#print(result.content)



#example 4
#from langchain.chat_models import ChatOpenAI
#from langchain.prompts.chat import ChatPromptTemplate
#from langchain.schema import BaseOutputParser
#from dotenv import load_dotenv
#import os
#
#
#load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
#
#class AnswerOutputParser(BaseOutputParser):
#    def parse(self, text:str):
#        """Parse the output of an LLM call."""
#        return text.strip().split("answer =")
#
#chat_model = ChatOpenAI(openai_api_key=api_key)
#
#template = """You are a helpful assistant that solves math problems and shows your work.
#            Output each step then return the answer in the following format: answer = <answer here>.
#            Make sure to output answer in all lowercases and to have exactly one space and one equal sign following it.
#            """
#
#human_template="{problem}"
#
#chat_prompt = ChatPromptTemplate.from_messages([
#    ("system", template),
#    ("human", human_template),
#])
#
#messages = chat_prompt.format_messages(problem="2x^2 - 5x +3 = 0")
#
#result = chat_model.predict_messages(messages)
#parsed = AnswerOutputParser().parse(result.content)
#steps, answer = parsed
#
#print(answer)



#example 5
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text:str):
        return text.strip().split(", ")

chat_model = ChatOpenAI(openai_api_key=api_key)

template = """You are a helpful assistant  who generates comma separated lists.
A user will pass in a category, and you should generate 5 onjects in that category in a comma separated list.
Only return a comma separated list, and nothing more."""

human_template="{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
result = chain.invoke({"text":"colors"})
print(result)

