from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text.",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, bd=0, activebackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0,  bd=0, activebackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)