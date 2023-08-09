class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0  # count question
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print(f'That\'s wrong. \n')
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}. \n')
