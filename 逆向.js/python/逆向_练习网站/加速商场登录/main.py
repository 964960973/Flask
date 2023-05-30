#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @author: A.L.Kun
# @file : test.py
# @time : 2022/4/25 6:22
from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read  # 生成随机偏移量
# print(random_generator)
rsa = RSA.generate(2048, random_generator)  # 生成一个私钥
# print(rsa)
# 生成私钥
private_key = rsa.exportKey()  # 导出私钥
# print(private_key.decode())
# 生成公钥
public_key = rsa.publickey().exportKey()  # 生成私钥所对应的公钥
# print(public_key.decode())

with open('rsa_private_key.pem', 'wb')as f:
    f.write(private_key)  # 将私钥内容写入文件中

with open('rsa_public_key.pem', 'wb')as f:
    f.write(public_key)  # 将公钥内容写入文件中
