from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    ques_text = i['question']
    ques_answer = i['correct_answer']
    new_question = Question(ques_text, ques_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your Final score was : {quiz.score}/{quiz.question_number} ")



