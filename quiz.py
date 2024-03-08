




class Quiz():
    def __init__(self):
        self.questions = []
        self.answers = []

    def user_populate(self):
        print("Type \"q\" to quit.")
        while True:
            q_input = input("Please type a question: ")
            a_input = input("Please type the answer to that question: ")

            if a_input == "q" or q_input == "q":
                print("Exiting...")
            else:
                self.questions.append(q_input)
                self.answers.append(a_input)

    def auto_populate(self, questions, answers):
        self.questions = questions
        self.answers = answers


def auto_run_quiz(quiz, answers):
    acc_key = {"Total":0, "Correct": 0, "Incorrect": 0}
    for i in range(len(answers)):
        if answers[i] == quiz.answers[i]:
            acc_key["Correct"] += 1
        else:
            acc_key["Incorrect"] += 1
        acc_key["Total"] += 1
    
    print(f"Total Correct: " + str(acc_key["Correct"]))
    print(f"Total Incorrect: " + str(acc_key["Incorrect"]))
    print("Score: " + str(round(acc_key["Correct"] / acc_key["Total"], 2) * 100) + "%")
        

def run_quiz(quiz):
    cur_ans = ""
    acc_key = {"Total": 0, "Correct": 0, "Incorrect": 0}
    for i,q in enumerate(quiz.questions):
        print(q)
        cur_ans = input()

        if cur_ans == quiz.answers[i]:
            acc_key["Correct"] += 1
        else:
            acc_key["Incorrect"] += 1
        acc_key["Total"] += 1
    
    print(f"Total Correct: " + str(acc_key["Correct"]))
    print(f"Total Incorrect: " + str(acc_key["Incorrect"]))
    print("Score: " + str(round(acc_key["Correct"] / acc_key["Total"], 2) * 100) + "%")


seasons_q = ["January?", "February?", "March?", "April?", "May?", "June?", "July?", "August?", "September?", "October?", "November?", "December?"]
seasons_a = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall", "Fall", "Fall", "Winter"]
user_a = ["Summer", "Summer", "Spring"]
seasons = Quiz()

seasons.auto_populate(seasons_q, seasons_a)

auto_run_quiz(seasons, seasons_a)

        