##File Name:  question.py
#Purpose:     Class to represent a trivia question with four
#             possible answers
#Author:      Austin Ramberg
#Date:        January 22, 2019

class Question:

    # initialization method 
    def __init__(self,
                prompt,
                ans1,
                ans2,
                ans3,
                ans4,
                correctAnswer):
        self.__prompt = prompt
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__correctAnswer = correctAnswer

    # getters
    def getPrompt(self):
        return self.__prompt

    def getAns1(self):
        return self.__ans1

    def getAns2(self):
        return self.__ans2

    def getAns3(self):
        return self.__ans3

    def getAns4(self):
        return self.__ans4

    def getCorrectAnswer(self):
        return self.__correctAnswer
        
    # setters
    def setPrompt(self, prompt):
        self.__prompt = prompt

    def setAns1(self, ans):
        self.__ans1 = ans

    def setAns2(self, ans):
        self.__ans2 = ans

    def setAns3(self, ans):
        self.__ans3 = ans

    def setAns4(self, ans):
        self.__ans4 = ans

    def setCorrectAnswer(self, num):
        self.__correctAnswer = num

    # other methods
    def __str__(self):
        return self.__prompt + '\n' + "1. " + self.getAns1() + '\n' + "2. " + self.getAns2() + '\n' + "3. " + self.getAns3() + '\n' + "4. " + self.getAns4() + '\n'