

ipt_username = input("Username (letters): ")
ipt_username_alpha = ipt_username.replace('_', '').replace('.', '')

ipt_username_alpha = ''.join([i for i in ipt_username_alpha if not i.isdigit()])

print(ipt_username_alpha)

#ipt_username = filter(lambda x: x.isalpha(), ipt_username)