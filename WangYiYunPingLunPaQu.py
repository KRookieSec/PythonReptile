#coding:utf-8
#爬取网易云音乐评论
'''
步骤                                    
1、找到未加密的参数                       #window.arsea()
2、想办法把参数进行加密（必须参考网易的逻辑），params => encText,encSecKey => encSecKey
3、请求到网易，拿到评论信息
'''
#AES加密模块
from Crypto.Cipher import AES
from base64 import b64decode, b64encode    #用于将加密后的结果转换为字符串
import requests
import json

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
#请求方式是post，找到真真实参数
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1840192925",
    'threadId': "R_SO_4_1840192925"
}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e"
g = "0CoJUm6Qyw8W8jud"
i = "qvlssn1vx78CoErY"        #固定i,从而固定encSecKey

def get_encSecKey():
    return "3e74106e3eb5f169c173fd89a57db2ae0de3e51dc402802dfb0bda80d54df715c49fd93233112c59e821345c8416c04f9c37c0c789710722c5376f6416f0154b789f204a183bf6e063b03af5892b2da3e"

#处理AES加密时字符串内容补齐
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad)*pad
    return data

#模拟函数d，得到params
def get_params(data):     #默认收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second    #返回的就是params


def enc_params(data, key):   #加密过程
    iv = "0102030405060708"  #加密函数中的偏移量
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'), mode=AES.MODE_CBC)    #创建加密器
    bs = aes.encrypt(data.encode('utf-8'))    
    '''
    加密，加密的内容的长度必须是16的倍数，如123456,16位差10个，则后面必须加上10个chr(10),
    如果数据刚好是16位，则后面必须加上16个chr(16)
    '''
    #使用b64模块将加密后的结果转化为字符串
    return str(b64encode(bs), 'utf-8')

#处理加密过
'''
function a(a) {                                 #2、a(16)，产生随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)              #循环16次
            e = Math.random() * b.length,       #随机数
            e = Math.floor(e),                  #取整
            c += b.charAt(e);                   #取字符串中的xxx位置
        return c
    }
    function b(a, b) {      #a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)     #b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)     #e是数据
          , f = CryptoJS.AES.encrypt(e, c, {   #c是加密们的密钥
            iv: d,   #偏移量
            mode: CryptoJS.mode.CBC     #模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {             #d: 数据，e：，010001，f:很长的一串,g:"0CoJUm6Qyw8W8jud"
        var h = {}                       #空对象
          , i = a(16);   #a(16)，        #1、查看a函数，i是一个16位的随机值
        return h.encText = b(d, g),      #g是密钥
        h.encText = b(h.encText, i),     #返回的就是params   i也是密钥
        h.encSecKey = c(i, e, f),        #得到的就是enSecKey，e和f是固定的，若把i固定，则得到的key一定是固定的
        h
    }
两次加密：
数据+g => b => 第一次加密+i => b => params
'''

resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),    #使用json模块将data转化为json字符串，不这么做将会报错
    "encSecKey": get_encSecKey()
})

print(resp.text)
print("over!")