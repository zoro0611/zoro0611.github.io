from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))

# print(f"{question_bank[0].text}: {question_bank[0].answer}")
quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizBrain.score}/{quizBrain.question_number}")