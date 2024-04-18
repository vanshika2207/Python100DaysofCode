THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score=Label(text="Score:",font=("Arial",10,"normal"),fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.canvas_text=self.canvas.create_text(150, 125,width=280, text="hello", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.right_img=PhotoImage(file="images/true.png")
        self.right_button=Button(image=self.right_img,highlightthickness=0,command=self.right)
        self.right_button.grid(row=2,column=0)

        self.left_img = PhotoImage(file="images/false.png")
        self.left_button = Button(image=self.left_img, highlightthickness=0, command=self.left)
        self.left_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def right(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def left(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():


            self.score.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="You have reached end of question")
            self.right.config(state="disable")
            self.left.config(state="disable")