from quiz_brain import QuizBrain

quiz_brain = QuizBrain()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
