#! /usr/bin/env python2.7
#coding=utf-8
from simple import match_aiml
responses= match_aiml('你好')
for response in responses:
    print response
