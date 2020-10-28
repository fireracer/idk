from question import question
question_prompts = [
    "What colors are apples?\n(a) red/green\n(b) purple\n(c)orange\n\n",
    "What is the language spoken in Columbia?\n(a) spanish\n(b) french\n(c) columbian\n(d) greek\n\n",
    "What is the speed of the NGRAM Rudra M-1\n(a) 3x10^8 m/s\n(b) Mach 2\n(c) 2.18x10^18\n(d) Mach 3\n\n",
    "What is the best color?\n(a) white\n(b) red\n(c) violet\n(d) black\n\n",
    "What is the offspring of a polar bear and a grizzly bear called?\n(a) golar bear\n(b) pizzily bear\n(c) grola bear\n(d) pizzy bear\n\n"
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "a"),
    question(question_prompts[2], "b"),
    question(question_prompts[3], "d"),
    question(question_prompts[4], "d")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
