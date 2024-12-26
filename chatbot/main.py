from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following 

Here is the conversation history : {context}

Question : {question}

Answer :"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model 

def handleconv():
    context=""
    print("Welcome to the chat! I'll be happy to help you with any questions , exit to end chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result=chain.invoke({"context" : context, "question" : user_input })
        print("Model: ", result)

        context += f"\nYou : {user_input}\nAI : {result}"
if __name__ == "__main__":
    handleconv()