n=4

while n:
    s=input("请输入考试成绩：")
    if s.isdecimal():
        s = int(s)
        if s<60 and s>=0:
            print("你没及格，要挨揍了")
        elif s>=60 and s<80:
            print("你及格了，但还是要挨揍")
        elif s>=80 and s<90:
            print("小伙子还不错，你已经超过了好多人")
        elif s>=90 and s<100:
            print("优秀，继续保持")
    else:
        print("请输入正整数")
    n = n-1