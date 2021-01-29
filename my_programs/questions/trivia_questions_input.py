# phil welsby - 28 jan 2021
# file to create a list containing elements to suite The Haunted Mansion Game

open_list = "['''"
quotes_open = "\'''"
quotes_close = "\''',"

question = input ('Enter question: ')
A = input('Enter answer A: ')
B = input('Enter answer B: ')
C = input('Enter answer C: ')
D = input('Enter answer D: ')
ans_letter = input('Enter the letter that matches the correct answer: ')
ans_correct = input('Enter a written response here for a correct answer: ')
ans_incorrect = input('Enter a written response here for an incorrect answer: ')

cls_list = "False],"


data = open('trivia_questions.py', 'a')
print(open_list, file = data)
print(question, file = data)
print('A', A, '               ', 'B', B, file = data)
print('C', C, '               ', 'D', D, quotes_close, file = data)
print(quotes_open, file = data)
print('Correct!', ans_correct, quotes_close, file = data)
print(quotes_open, file = data)
print('Incorrect!', ans_incorrect, quotes_close, file = data)
print("'", ans_letter, "',", cls_list, file = data)

