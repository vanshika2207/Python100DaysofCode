class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        ans= input(f"Q{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(ans,current_question.answer)
    def still_has_question(self):
        while self.question_number<len(self.question_list):
            return True
        else:
            return False
    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower()==correct_ans.lower():
            print("You got it right")
            self.score+=1

        else:
            print("That is wrong")
        print(f"The correct answer is :{correct_ans}")
        print(f"The current score is :{self.score}/{self.question_number}")
        print('\n')


