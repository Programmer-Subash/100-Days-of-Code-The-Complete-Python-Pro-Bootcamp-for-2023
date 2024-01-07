from data import question_data
from question_model import Question
import random


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0

        self.list_of_questions = []
        for x in question_data:
            question = Question(x["text"], x["answer"])
            self.list_of_questions.append(question)

    def next_question(self):
        current_question = self.list_of_questions[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?: ").capitalize()
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number < len(self.list_of_questions):
            return True
        else:
            return False
