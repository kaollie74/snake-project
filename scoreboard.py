from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score_from_file()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} || High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score_to_file()

        self.score = 0
        self.update_scoreboard()

    def set_high_score_to_file(self):
        with open("high_score.txt", mode="w") as file:
            file.write("High Score: " + str(self.high_score))

    def get_high_score_from_file(self):
        with open("high_score.txt", mode='r') as file:
            txt = file.read()
            score = txt[len(txt) - 1]
            return int(score)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
