class Question:
        def __init__(self,prompt,answer):
                self.prompt=prompt
                self.answer=answer

#================================object======================
question_prompt=[
        "what's color of apples.? \n(a) Red\Green \n(b) Purple \n(c) Orange \n\n",
        "what's color of Bananas.? \n(a) Teal \n(b) Yellow \n(c) Magenta\n\n",
        "what's color of Strawberries.? \n(a) Yellow \n(b) Red \n(c) Blue\n\n"
]

questions=[

        Question(question_prompt[0],'a'),
        Question(question_prompt[1],'c'),
        Question(question_prompt[2],'b'),
]
def test_quiz(questions):
        score = 0
        for qns in questions:
                answer=input(qns.prompt)
                if answer == qns.answer:
                        score +=1
                        print('you got ' + str(score) + '/' + str(len(questions)) + ' correct')
test_quiz(questions)