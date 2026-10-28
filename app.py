from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# APIキー
load_dotenv()  # Load environment variables from .env file

# LLM実行
def llm_execute(selected_item, input_message):
        if selected_item == "公立学校教師":   
            system_message = "あなたは公立学校教師です。塾とは異なり生徒一人ひとりの個性を大事に、優しく寄り添った指導が得意です。"
        else:
            system_message = "あなたはスパルタ進学塾の講師です。生徒の成績向上を最優先に考え効率的な学習法を提供するのが得意です。厳しい口調で指導してください。"
               
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=input_message)
        ]

        return llm.invoke(messages).content


st.title("先生に質問できるアプリ")

st.write("##### 勉強方法について質問できます。")
st.write("回答者は、公立学校教師かスパルタ塾の講師、どちらかを選べます。")
st.write("###########################################################################")
st.write("■公立学校教師：生徒一人ひとりに寄り添い、優しく丁寧な指導が得意")
st.write("■スパルタ塾講師：成績向上を最優先に考え、効率的な学習法を厳しく指導。")
st.write("###########################################################################")
st.write("入力フォームに質問を入力し、「実行」ボタンを押してください。")

selected_item = st.radio(
    "回答を希望する先生を選択してください。",
    ["公立学校教師", "スパルタ塾講師"]
)
input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    
    st.divider()

    if input_message:

        if selected_item == "公立学校教師":        
            st.write("公立学校教師の田中が回答します。") 
            st.write("考案中・・・") 
        else:
            st.write("スパルタ塾講師の松本が回答します。")
            st.write("考案中・・・") 

        st.write(llm_execute(selected_item, input_message))

    # 質問が空だったら
    else:
        st.error("質問を入力してください。")