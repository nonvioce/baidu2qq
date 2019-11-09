# -*- coding: utf-8 -*-
"""
Spyder Editor

将百度输入法词库转为qq输入法词库
"""
souceFile = open("ch3.txt","r",encoding='UTF-16')#百度输入法词库
qFile = open("ch3_q.txt","a+")#转化的词库

def fun(s):
    fIndex=s.index("(")
    bIndex=s.index(")")
    qFile.write(s[fIndex+1:bIndex].replace("|","'"))
    qFile.write(" ")
    qFile.write(s[:fIndex])
    qFile.write(" ")
    qFile.write(s[bIndex+2:])

for line in souceFile:
    fun(line)
souceFile.close()
qFile.close()