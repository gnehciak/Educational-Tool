# reading the CSV file
text = open("user_data.csv", "r")

with open('test.csv', 'r+') as f:
    text = f
    text = ''.join(text.readlines())
    # search and replace the contents

    text = text.split('\n')
    print(text)
    for i in text:
        if i.split(',')[0] == 'Kevin':
            new = i.split(',')
            new[1] = str(int(new[1]) + 1)
            new = ','.join(new)
            text[text.index(i)] = new
            print(int(i.split(',')[1]) + 1)

    print(text)
    text = '\n'.join(text)

# output.csv is the output file opened in write mode 
x = open("test.csv", "w")
x.writelines(text)
# all the replaced text is written in the output.csv file
#x.writelines(text)
x.close()

"""
for record in reader:
                if record[0] == activeUser:
                    if int(record[1]) <= 5:
                        print("Congratulations! You've unlocked the next level:")
                        print("Level", int(record[1]) + 1, 'unlocked.')
"""