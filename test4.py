import random
dic = {"question1":"answer", "question2":"answer", "question3":"answer"}

print(list(dic.keys())[random.randrange(0, len(list(dic.keys())))])