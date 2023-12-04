from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#here to insert your key
from dotenv import load_dotenv

load_dotenv()

def generate_quiz(sub,num):
    llm = OpenAI(temperature=0.8)
    llm2 = OpenAI(temperature=1)

    #generat the answers
    prompt_template_Qustion = PromptTemplate(
        input_variables = ['sub','num'],
        template ="I want a multiple-choice quiz including {num} questions for {sub} subject with exactly 4 choices for each question."
    )
    Q = LLMChain(llm=llm, prompt=prompt_template_Qustion, output_key="Qize")
    responseQ = Q({'sub': sub, 'num': num})

    #generat the qustions
    prompt_template_Ans = PromptTemplate(
        input_variables = ['Qus'],
        template ="give me the correct answer just the correct one  for these qustion : {Qus} each one in a single line "
    )
    A = LLMChain(llm = llm2 , prompt=prompt_template_Ans, output_key="Answer")
    responseA = A({'Qus': responseQ["Qize"]})

    return [responseQ["Qize"],responseA["Answer"]]


if __name__ == "__main__":
    result = generate_quiz("computer scince" , "5")
    for x in result : 
        print (x)

