class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        player_answer = input(
            f" Q.{self.question_number} - {current_question.text} (True/False): "
        )
        self.check_answer(player_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, player_answer, q_answer):
        if player_answer.lower() == q_answer.lower():
            print("you got the question right")
            self.score += 1
        else:
            print("wrong answer")
        print(f"The correct answer is: {q_answer}")
        print(f"your score is {self.score}/{self.question_number}")
