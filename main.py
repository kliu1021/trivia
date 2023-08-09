from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    questions_text = questions['text']
    questions_answer = questions['answer']
    new_questions = Question(questions_text, questions_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f'You\'ve completed the quiz.')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')
