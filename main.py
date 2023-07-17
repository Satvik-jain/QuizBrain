from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

question_bank=[]
for question_set in question_data:
    question_bank.append(Question(question_set["question"], question_set["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.question_left():
    quiz.next_question()

print("You have completed the Quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")