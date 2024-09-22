import os
from dotenv import load_dotenv
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings(model='text-embedding-3large')
print(embeddings)

text ='This is an tutorial on openAI Embedding'
query_result=embeddings.embed_query(text)
print(query_result)
