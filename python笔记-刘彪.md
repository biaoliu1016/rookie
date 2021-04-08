# day1内容

1.计算机的初步认识（`冯`（内存，硬盘等底层原理）**-----》**`系统`（windows，mac（装逼，开发方便），linux（centos需要运维，ubunt，redhat不用运维））**-----》**程序）

![image-20210407164615029](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407164615029.png)

2.解释器安装(了解环境变量：即路径，方便查找到exe等可执行程序的路径)

3.第一个脚本（文件）

4.编码(3类了解下，建议：文件编写时保存文件用utf-8格式，以什么编码保存就要用什么编码方式打开否则就会乱码）

- ascii8，英文，8位表示一个东西，2**8; 

-  unicode,万国码，32位表示一个东西，2**32；

- utf-8：一个字节占八位，一个英文字母占一个字节，占一个中文占两个字节，编码和解码要一致，python2默认解释器编码是ascii，python3默认解释器编码是utf-8。

  - py2：ascii，在文件头部加：

    ```
    # -*- coding:utf--8 -*-
    print('你好')
    ```

  - py3: utf-8

![image-20210407172036684](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407172036684.png)



![image-20210407171828418](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407171828418.png)

5.上午内容回顾

6.解释器

7.输出print（[python2：print '您好'；python3：print（'您好'）]()）

8.数据类型（**三种**：字符串（最多三引号），整数，true和false的布尔类型）

9.变量（**三个注意事项**：1.必须以数字、字母和下划线命名，2不能以数字开头，3.不能和关键字重合）（建议：1.见名知意：name='l刘彪' age=28；2用下划线连接：liubiao_dad='刘开秋'）

10.综上练习题

11.输入input

12.注释（项目写多了久了以后自己都不知道自己写的是什么）

13.条件判断（if）

14.今日总结

15.pycharm安装和使用

# day2基础&运算符

## 今日概要

1.循环

2.字符串格式化

3.运算符

4.编码

5.博客&git

## 内容回顾

- 计算机基础

- 安装解释器

  - py2
  - py3

- 语法

  - print/input
  - 整型int / 字符串 str / 布尔值 boolen
  - 条件语句
  - and运算符
  - 变量

- 练习：

  ```
  评分规则：
   A >=90
   B >=80
   c >=70
   D 其他
  用户输入成绩，根据成绩的不同显示不同的级别。
  
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
  ```

## 补充

1.if条件的嵌套

```
message = '''欢迎致电10086
1.话费查询；
2.流量服务；
3.业务办理；
4.人工服务'''

print(message)

index = input('请输入你要选择的服务：')
index = int(index)
if index == 1:
    print('话费查询')
elif index == 2:
    print('流量服务')
elif index == 3:
    content = '''业务办理
    1.修改密码；
    2.更改套餐；
    3.停机；'''
    print(content)
    value = input('请输入要办理的业务：')
    value = int(value)
    if value == 1:
        print('修改密码')
    elif value == 2:
        print('更改套餐')
    elif value == 3:
        print('停机')
    else:
        print('错误')
elif index == 4:
    print('人工服务')
else:
    print('输入错误')
```

2.pycharm可以变更解释器

![image-20210407202536057](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407202536057.png)

## 今日内容

### 1.循环语句

- while基本结构
- break
- continue
- while else

### 2.字符串格式化    

1.   %s

2. %d

3. %%

   ![image-20210407221942711](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407221942711.png)

### 3.运算符（运算，比较，赋值）（字符串和数字互相转换）

![image-20210407223307145](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407223307145.png)

![image-20210407223414859](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407223414859.png)

![image-20210407223443542](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407223443542.png)

### 4.编码补充

utf-8：网络传输或数据存储

- ascii
- unicode
  - ecs2
  - esc4（不够用产生的）

- utf-8，中文用3字节
- utf-16(电脑硬盘存储的格式)
- gbk（亚洲的公司用的）中文用2字节。
- qb2312，中文用2字节

![image-20210407224428445](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210407224428445.png)

### 5.博客

博客园:海燕 （路飞学城的一个师姐2）

### 6.git

# day03

## 今日概要

1.整型

2.布尔类型

3.字符串

## 内容回顾

作业：xmind写每周内容的思维导图

## 补充

1.运算符补充

- in
- not in



