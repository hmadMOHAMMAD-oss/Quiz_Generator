import streamlit as st
from Question_Request import generate_quiz

#to format the ansers (qustion:qustion , option : [answer])
def split_quztion(arr):
    questions = arr.split('\n\n')
    qustion_list=[]

    for qb in questions:
        lines = qb.split('\n')

        question = lines[0]
        options = lines[1:]

        question_dict = {
        'question': question,
        'options': options
        }

        qustion_list.append(question_dict)
    
    return qustion_list


def main():
    st.title("Quiz Generator")

    subject = st.text_input("Enter the subject for the quiz:")
    option = [1,2,3,4,5]
    num_questions = st.selectbox("Enter the number of questions:", option)

    if subject  and num_questions :
        #Gitting the data
        result = generate_quiz(subject, str(num_questions))

        #Gitting the Answers
        for d, x in enumerate(result) : 
            if d == 0 :
                continue
            if 'Answers' not in st.session_state:
                st.session_state['Answers'] = x

            
        if 'result' not in st.session_state:
            st.session_state['result'] = generate_quiz(subject, str(num_questions))

        #getiing the qustion in format
        if 'qize_Q' not in st.session_state:
            st.session_state['qize_Q'] = split_quztion(result[0])

        #print the qustions
        for indx , val in  enumerate(st.session_state['qize_Q']) :
            st.write(st.session_state['qize_Q'][indx]["question"])
            for x in st.session_state['qize_Q'][indx]["options"] :
                st.write(x)

        #for to reseve the user answers and compar them to the correct answers
        with st.form("my_form"):
            length = len(st.session_state['qize_Q'])-1
            check_list = []
            check = True
            r = 1
            score = 0
            #to generate the forms 
            while length != 0:
                text = st.text_input(f"answer the {r} qustion")
                check_list.append(text)
                length -= 1  
                r += 1    
            #to Check if all the answer are submitted
            for x in check_list :
                if x is "":
                    check=False

            submitted = st.form_submit_button("Submit")
            if submitted and check:
                for x in check_list :
                    if x in st.session_state['Answers']:
                        score += 1
                st.success(f"your score is : {score}")
                st.write(f"the asnswer are :  { st.session_state['Answers'] }")

            else :
                st.warning("answer all the qustions")
    else :
        st.warning("Please input both subject and number of questions.")
    
if __name__ == "__main__":
    main()
    