import streamlit as st
from code.range_quiz import range_quiz_logic
from code.customer_quiz import customer_quiz_logic
from code.random_30_quiz import random_quiz_logic
from code.quiz_logic import load_questions
import os

# 設置頁面配置
st.set_page_config(page_title="AWS AIF-C01 Quiz",  # 頁面標題
                    page_icon="🚀",  
                    initial_sidebar_state="expanded" 
)

# 使用 CSS 自定義段落樣式（調整行間距）
st.markdown("""<style>
            .css-1d391kg p {
                width: 50%;  
                line-height: 1;  
                margin-left: 10px;  
            }

            .css-1d391kg h3 {
                font-size: 1.2rem;
                font-weight: bold;
                margin-bottom: 10px;
            }
            </style>
        """, unsafe_allow_html=True
)

# 顯示標題
st.title("🚀 AWS AIF-C01 Quiz 🌕")
# st.image("banner.png")  # 插入相關圖片或 logo
st.write("💡Practice for 勞動部 | AI數據應用人才養成班第01期")

# 在側邊欄顯示考試範圍
st.sidebar.title("📚 Quiz Scope - 筆試")
st.sidebar.markdown("""**AWS AIF-C01 參考題✒️**""")

st.sidebar.markdown(""" - Choose the quiz you want to practice.""")

# 顯示側邊欄的題目選擇和模式選擇
quiz_files = [f for f in os.listdir("data/json/") if f.endswith(".json")]
quiz_file = st.sidebar.selectbox("Quiz ", quiz_files)
quiz_mode = st.sidebar.selectbox("Mode", ["Range Mode", "Customer Mode", "Random Mode"])

# Function to reset session states
def reset_states():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# 根據選擇載入題目
questions = load_questions(f"data/json/{quiz_file}")

# 根據模式執行對應邏輯
if quiz_mode == "Range Mode":
    st.sidebar.write("📝 **挑戰自我** : 指定範圍學習")
    range_quiz_logic(questions)
elif quiz_mode == "Customer Mode":
    st.sidebar.write("🎯 **專注題型** : 鎖定錯誤，集中火力")
    customer_quiz_logic(questions)
elif quiz_mode == "Random Mode":
    st.sidebar.write("🎲 **骰子測驗** : 隨機挑選題目，全靠實力")
    random_quiz_logic(questions)

# Sidebar reset button
if st.sidebar.button("🔄 Reset", key="reset_button"):
    reset_states()

# 加入避嫌與聲明
st.sidebar.markdown("---")
st.sidebar.markdown("#### ⚠️ Disclaimer")
st.sidebar.markdown("""- 系統為 **個人專案**，僅學習且不涉任何商業用途。
                        - 參考 ** AIF-C01 題庫**。""")
st.sidebar.markdown("#### 📢 Notice")
st.sidebar.markdown("""- 若需使用相關資料，請遵守其知識產權法規。""")
