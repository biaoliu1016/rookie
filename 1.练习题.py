score = input('''请输入成绩:''')
score_int = int(score)
if score_int>=90:
    print('A')
elif score_int>=80:
    print('B')
elif score_int>=70:
    print('C')
else:
    print('D')