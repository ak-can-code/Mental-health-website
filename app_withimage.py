import streamlit as st
import textwrap
import requests

st.set_page_config(page_title="Changing our views on Mental Illness", layout="wide")
# - - - - HEADER Section - - - -
st.title("Mental Illness")
st.write("By Akshiithi Prithiviraj")
st.subheader("What is Mental Illness?")
st.write("The National Institute of Mental Health defines mental illness as a mental, behavioral, or emotional disorder. Mental illnesses can vary in impact. Impairment because of the illness can range from no impairment, mild, moderate, and severe impairment. When a person has severe impairment they are described as having serious mental illness.")
with st.container():
    st.write("- - -")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("What is Mental Illness?")
        st.write("##")
        st.write("""The National Institute of Mental Health defines mental illness as a mental, behavioral, or emotional disorder. Mental illnesses can vary in impact. Impairment because of the illness can range from, no impairment, mild, moderate, and severe. When a person has severe impairment they are described as having serious mental illness. Mental illness is not the same as poor mental health, often people confuse the two. Mental health is the physical, mental/emotional, and social well being of a person. """)
        st.subheader("Brief History of Mental Illness")
        st.write("In early history, in some cultures, mental illness was categorized as a religious or personal problem, but in many others, it was a form of religious punishment or demonic possession. During the middle ages, the mentally ill were still believed to be possessed or in need of religion. These negative interpretations of mental illness were present in the 18th century in the United States. This led to the unhygienic confinement of mentally ill individuals in prisons alongside actual criminals. After viewing these living conditions Dorothea Dix, a female activist, started advocating for better living conditions for the mentally ill. The U.S government built 32 state psychiatric hospitals after a 40 year period of pressure from Dorothea Dix. Despite having these state hospitals, proper care was not being given to those who needed it. After several reports of human rights violations and poor living conditions reported about these facilities, deinstitutionalization( idea of improving treatment and quality of life for the mentally ill) became a popular Idea. Deinstitutionalization efforts mirrored an almost international movement to reform the “asylum-based” mental health care system and move toward community-oriented care.")
        st.write("##")
        st.subheader ("The Stigma Around Mental Illness")
        st.write("Stigma regarding mental health is when society views a person in a negative way because of their mental illness. Mental health stigma comes from harmful stereotypes that originated with early beliefs about mental illness. Pressures of mental health stigma can come from anyone; family, friends, coworkers, and society. In a survey done by the HealthAffairs a majority of people in the U.S believe in supporting those with mental illness so they can recover but almost half said they wouldn’t welcome a mental health facility into their neighborhood and 2⁄3 of the respondents said there was still a lot of stigma attached to mental illness.  In data found by the SAMHSA in 2020, 21% of all U.S. adults had any mental illness. Of that 21%, 42.2% adults received mental health services in the past year. Additionaly, the suicide rate increased 25% over the past 20 years for the most part because of not enough access to mental health care, and poor financing of mental health care yet societal and cultural stigma around mental illness has been mostly unchanged (American Psychiatric Association).  The main reason people don’t seek help from professionals is fear of being labeled “crazy” or “psycho”. These characterizations are not truthful, cause pain, and prevent people from getting the help they need. ")
        st.subheader ("How to overcome mental health stigma")
        st.write ("The reason stigma exists is because of misinformation, lack of understanding, and fear .  To overcome mental health stigma as a society we have to increase education about mental illness and support those who are experiencing stigma. Please remember people with mental illnesses are not defined by their illness, rather it is a part of them and they are much more than just their illness. Don’t be a part of the problem, try to solve it.")
        

