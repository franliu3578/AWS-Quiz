import streamlit as st
import json
import random

# Load JSON question file
def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def random_quiz_logic(questions):
    # Ensure `questions` is a list of questions
    if isinstance(questions, list):
        all_questions = questions
    else:
        all_questions = load_questions(questions)

    # Initialize session state variables
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

    # Random selection of questions
    if not st.session_state.range_selected:
        st.title("Random 30 Questions Quiz")
        total_questions = len(all_questions)

        st.write(f"📋 This quiz contains {total_questions} questions.")

        if st.button("Start Quiz"):
            st.session_state.selected_questions = random.sample(all_questions, min(30, total_questions))
            st.session_state.user_answers = [None] * len(st.session_state.selected_questions)
            st.session_state.current_question_index = 0
            st.session_state.range_selected = True
    elif st.session_state.quiz_ended:  
        show_quiz_summary()
    else:
        # Active quiz logic
        questions = st.session_state.selected_questions
        current_index = st.session_state.current_question_index
        question = questions[current_index]

        st.subheader(f"Question {current_index + 1}: {question['question']}")

        # Display code block (if any)
        if "code" in question and question["code"]:
            st.code(question["code"], language="python")


        # Handle short answer questions
        if "input_field" in question and question["input_field"]:
            # Multi-line input field
            user_input = st.text_area("Enter your answer:", height=100, key=f"q_{current_index}")
            user_answer = user_input.strip()
        else:
            # Handle single or multiple choice
            if "SELECT TWO" in question["question"].upper() or isinstance(question["answer"], list):
                user_answer = st.multiselect("Choose your answers:", question["options"], key=f"q{current_index}")
            else:
                user_answer = st.radio("Choose your answer:", question["options"], key=f"q{current_index}")

        # Submit button for the current question
        if st.button("Submit/Next", key=f"submit_{current_index}"):
            correct_answer = question["answer"]

            # Check if the answer is correct
            if isinstance(correct_answer, list):  
                if set(user_answer) == set(correct_answer):
                    st.session_state.correct_count += 1
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect! ❌")
                    record_wrong_answer(current_index, user_answer, question)
            else:  # Single-choice
                if user_answer == correct_answer:
                    st.session_state.correct_count += 1
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect! ❌")
                    record_wrong_answer(current_index, user_answer, question)

            # Show hint
            st.write("### Hint:")
            st.write(f"- **Keywords:** {', '.join(question.get('keywords', []))}")
            st.write(f"- **Explanation:** {question.get('explanation', 'No explanation provided.')}")

            # Update question index
            if st.session_state.current_question_index < len(questions) - 1:
                st.session_state.current_question_index += 1
            else:
                st.success("You have completed the quiz! 🎉")

        # Add "End Quiz" button
        if st.button("End Quiz"):
            st.session_state.quiz_ended = True

# Record incorrect answers
def record_wrong_answer(index, user_answer, question):
    st.session_state.wrong_answers.append({
        "question": question["question"],
        "your_answer": user_answer,
        "correct_answer": question["answer"],
        "keywords": question.get("keywords", []),
        "explanation": question.get("explanation", "No explanation provided."),
    })

# Display quiz summary
def show_quiz_summary():
    total_questions = len(st.session_state.selected_questions)
    correct_answers = st.session_state.correct_count
    score = (correct_answers / total_questions) * 100

    st.write("## Quiz Summary")
    st.write(f"Total Questions: {total_questions}")
    st.write(f"Correct Answers: {correct_answers}")
    st.write(f"Score: {score:.2f}%")

    if st.session_state.wrong_answers:
        st.warning("Here are your incorrect answers:")
        for i, item in enumerate(st.session_state.wrong_answers, 1):
            st.write(f"### Incorrect Question {i}")
            st.markdown(f"- **Question:** {item['question']}")
            st.write(f"- **Your Answer:** {item['your_answer']}")
            st.write(f"- **Correct Answer:** {item['correct_answer']}")
            st.write(f"- **Keywords:** {', '.join(item['keywords'])}")
            st.write(f"- **Explanation:** {item['explanation']}")
            st.markdown("---")
