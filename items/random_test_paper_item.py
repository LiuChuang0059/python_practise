# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:48:09 2018

@author: 刘闯


生成随机的测试文件：省份 和省会城市

1.创建 30 份试卷 
2.每份试卷 20 个选择题 顺序随机
3.每个问题 一个正确答案 3个随机错误答案
4.测验试卷 写入 30个文本文件
5.答案 写入30个文本文件

"""

import random   ## 随机安排问题和答案 导入 random 

###1 测验数据保存在一个字典中

#### keys: 省份 ； values： 省会；
Capitals={"Hei Longjiang": "Ha'erbin",
           "Jilin" :"Changchun",
           "Liaoning":"Shenyang",
           "Hebei":"Shijiazhuang",
           "Henan":"Zhengzhou",
           "Anhui":"Hefei",
           "Hubei":"Wuhan",
           "Hunan":"Changsha",
           "Shanxi_1":"Xi'an",     ###如何解决字典里 储存相同字符问题
           "Shanxi_3":"Datong",
           "Gansu":"Lanzhou",
           "Ningxia":"Yinchuan",
           "Hainan":"Haikou",
           "Fujian":"Fuzhou",
           "Jiangxi":"Taiyuan",
           "jiangsu":"Nanjing",
           "Zhejiang":"Hanzhou",
           "Sichuan":"Chengdu",
           "Shandong":"Jinan",
           "Guangdong":"Guangzzhou"
        } 

###2 创建30份问卷  并随机给出候选答案

### 创建 quiz 和 answer  文件
for quiz_num in range(30):
    quizFile=open('Capitals_quiz%s.txt'%(quiz_num+1),'w')
    answerFile=open('Capital_quiz_answer%s.txt'%(quiz_num+1),'w')
    
###创建测验标题
    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((' '* 20)+ 'State Captial Quiz (Form %s)'%(quiz_num+1))
    quizFile.write('\n\n')
    answerFile.write('Quiz answer')
    answerFile.write('\n\n')


###创建省份的随机列表
    states=list(Capitals.keys())
    random.shuffle(states)
    
### 3 创建答案选
    for question_num  in range(20):
        correct_answer=  Capitals[states[question_num]]
        wrong_answer=list(Capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer=random.sample(wrong_answer,3)###选择的列表 ，随机选择的
        answer_options=wrong_answer+[correct_answer]
        random.shuffle(answer_options)
        
###4 将内容写进测试试卷 和答案文件
        #### 写入问题 和答案选项
        quizFile.write('%s.What is the capital of %s?\n' %(question_num+1,states[question_num]))
        for i in range(4):
            quizFile.write('  %s.%s\n'%('ABCD'[i],answer_options[i]))
        quizFile.write('\n')
        
        #### 写入答案  list.index!!!
        
        answerFile.write('%s.%s\n'%(question_num+1,'ABCD'[answer_options.index(correct_answer)]))
    quizFile.close()
    answerFile.close()
        


