import streamlit as st
import json
import os

# 加載 JSON 問題檔案
def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def quiz_logic():
    all_questions = load_questions(file_path)

    # 全域變數初始化
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = []
    if "wrong_answers" not in st.session_state:
        st.session_state.wrong_answers = []
    if "correct_count" not in st.session_state:
        st.session_state.correct_count = 0
    if "range_selected" not in st.session_state:
        st.session_state.range_selected = False
    if "selected_questions" not in st.session_state:
        st.session_state.selected_questions = []
    if "quiz_ended" not in st.session_state:  
        st.session_state.quiz_ended = False    

    # 顯示題目範圍選擇介面
    if not st.session_state.range_selected:
        st.title("Select Question Range")
        total_questions = len(all_questions)

        # 使用者輸入範圍
        start_index = st.number_input("Enter start number (1-based):", min_value=1, max_value=total_questions, value=1)
        end_index = st.number_input("Enter end number (1-based):", min_value=1, max_value=total_questions, value=total_questions)

        if st.button("Start Quiz"):
            if start_index <= end_index:
                selected_range = all_questions[start_index - 1:end_index]
                st.session_state.selected_questions = [
                    {"question": q, "original_index": i + start_index} for i, q in enumerate(selected_range)
                ]
                st.session_state.user_answers = [None] * len(st.session_state.selected_questions)
                st.session_state.range_selected = True
            else:
                st.error("Start question number must be less than or equal to end question number.")
    elif st.session_state.quiz_ended:  
        show_quiz_summary()

        # 顯示題目
        def show_question(index):
            question = questions[index]["question"]
            st.subheader(f"Question {index + 1}: {question['question']}")
            
            # 顯示程式碼區塊（如果有）
            if "code" in question and question["code"]:
                st.code(question["code"], language="python")

            # 如果題目是簡答題
            if "input_field" in question and question["input_field"]:
                # 多行輸入框
                user_input = st.text_area("Enter your answer:", height=500, key=f"q_{index}")
                user_answer = user_input.strip()

            # 單選或多選
            elif "SELECT TWO" in question["question"].upper():
                user_answer = st.multiselect("Select your answers:", question["options"], key=f"q_{index}")
            else:
                user_answer = st.radio("Select your answer:", question["options"], key=f"q_{index}")

            # 確認或下一題按鈕
            if st.button("Submit/Next", key=f"submit_{index}"):
                check_answer(index, user_answer)
                if st.session_state.current_question_index < len(st.session_state.selected_questions) - 1:
                    st.session_state.current_question_index += 1
                else:
                    st.success("You have completed the quiz!")
                    st.session_state.quiz_ended = True

            # 顯示結束測驗按鈕
            if st.button("End Quiz", key="end_quiz"):
                st.session_state.quiz_ended = True
                show_quiz_summary()
                
        # 檢查答案
        def check_answer(index, user_answer):
            question = st.session_state.selected_questions[index]["question"]
            correct_answer = question["answer"]

            st.session_state.user_answers[index] = user_answer

            # 處理簡答題答案比對
            if "input_field" in question and question["input_field"]:
                if user_answer == correct_answer.strip():
                    st.session_state.correct_count += 1
                    st.success("Correct Answer!")
                else:
                    record_wrong_answer(index, user_answer)

            # 處理多選或單選題答案比對
            elif "options" in question and question["options"]:
                if isinstance(correct_answer, list):  
                    if set(user_answer) == set(correct_answer):
                        st.session_state.correct_count += 1
                        st.success("Correct Answer!")
                    else:
                        record_wrong_answer(index, user_answer)
                else:  
                    if user_answer == correct_answer:
                        st.session_state.correct_count += 1
                        st.success("Correct Answer!")
                    else:
                        record_wrong_answer(index, user_answer)

            # 提示
            st.write("### Hint:")
            st.write(f"- **Keywords:** {', '.join(question['keywords'])}")
            st.write(f"- **Explanation:** {question['explanation']}")
            st.markdown("---")

        # 記錄錯誤答案
        def record_wrong_answer(index, user_answer):
            question = st.session_state.selected_questions[index]["question"]
            original_index = st.session_state.selected_questions[index]["original_index"]
            st.session_state.wrong_answers.append({
                "original_index": original_index,
                "question": question["question"],
                "your_answer": user_answer,
                "correct_answer": question["answer"],
                "keywords": question["keywords"],
                "explanation": question["explanation"]
            })
            st.error("Incorrect Answer!")

        # 顯示當前問題
        show_question(st.session_state.current_question_index)

# 顯示測驗總結
def show_quiz_summary():
    total_questions = len(st.session_state.selected_questions)
    answered_questions = st.session_state.current_question_index + 1
    correct_answers = st.session_state.correct_count
    score = (correct_answers / total_questions) * 100

    st.write("## Quiz Summary")
    st.write(f"Total Questions: {total_questions}")
    st.write(f"Answered Questions: {answered_questions}")
    st.write(f"Correct Answers: {correct_answers}")
    st.write(f"Score: {score:.2f}%")

    if answered_questions < total_questions:
        st.warning("You ended the quiz early.")
    st.markdown("### Thank you for participating!")