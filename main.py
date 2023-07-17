from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question_set in question_data:
    question_bank.append(Question(question_set["text"], question_set["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()