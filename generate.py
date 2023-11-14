from pypinyin import pinyin, lazy_pinyin, Style
import xml.etree.ElementTree as ET
import jieba
import opencc

def filter_tag(sentence):
    tag = ""
    has_tag = False
    index = 0

    juzi = ""
    pinyin_arr = []

    for char in sentence:
        if char=="<" and not has_tag:
            tag += char
            has_tag = True
            continue

        if has_tag:
            if char==">":
                index += 1
                tag += char
                if index==2:
                    has_tag = False
                    index = 0
                    root = ET.fromstring(tag)

                    juzi += root.text
                    pinyin_arr.append(root.attrib["py"])

                    tag = ""
                continue
            else:
                tag += char
                continue
        
        juzi += char
        pinyin_arr.append("")

    return (juzi, pinyin_arr)

# 繁体转简体
converter = opencc.OpenCC('t2s.json')

name = "松源崇岳禅师语录"
path = f'{name}.txt'

body = ""
with open(path) as f:
    for line in f.readlines():
        tag = ""
        has_tag = False
        index = 0
        try:
            root = ET.fromstring(line)
            tag = ""
            try:
                level = root.attrib["level"]
                tag = f"h{level}"
            except Exception as e:
                # print(e)
                tag ="h2"
            
            body += f"<{tag}>"
            for char in root.text:
                if char=="。":
                    body += char
                else:
                    ppyy = pinyin(char, heteronym=True)
                    if len(ppyy[0])>1:
                        body += "<ruby>"+ "<font color=\"black\">"+char+"</font><rt>"+pinyin(char)[0][0]+"</rt></ruby>"
                    else:
                        body += "<ruby>"+ char+"<rt>"+pinyin(char)[0][0]+"</rt></ruby>"
            
            body += f"</{tag}>"
            continue
        except Exception as e:
            # print(e)
            pass

        if len(line.strip()) == 0:
            continue

        body +="<p>"
        juzi = ""
        for char in line:
            # print(pinyin(char))
            if char == "。":
                juzi, pinyin_arr = filter_tag(juzi)
                juzi_s = converter.convert(juzi)
                seg_list = jieba.cut(juzi_s, cut_all=False)
                # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
                my_list = list(seg_list)
                juzi_index = 0
                for cizu in my_list:
                    ppyy = pinyin(cizu, heteronym=True)
                    i = 0
                    while i<len(cizu):
                        c_pinyin = pinyin_arr[juzi_index]
                        zi = juzi[juzi_index]
                        
                        if len(c_pinyin)==0:
                            if "盡"==zi and len(cizu)==1:
                                # "盡"字在单独情况下拼音都显示为jǐn，数量有大，特作处理。
                                body += f"<ruby>{zi}<rt>jìn</rt></ruby>"
                            elif zi in ["(", ")", "[", "]", "．"]:
                                # 特殊符号不标注拼音
                                body += f"<ruby>{zi}<rt></rt></ruby>"
                            else:
                                # print("Default Mode: " + "/ ".join(my_list))  # 精确模式
                                body += f"<ruby>{zi}<rt>{ppyy[i][0]}</rt></ruby>"
                        else:
                            # 处理没有拼音的标记
                            if c_pinyin=="-":
                                body += f"<ruby>{zi}<rt></rt></ruby>"
                            else:
                                body += f"<ruby>{zi}<rt>{c_pinyin}</rt></ruby>"
                        i += 1
                        juzi_index +=1
                body += "。"
                juzi=""
            else:
                juzi += char

        if len(juzi)>0:
            juzi_s = converter.convert(juzi)
            seg_list = jieba.cut(juzi_s, cut_all=False)
            # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
            my_list = list(seg_list)
            # print(my_list)
            for cizu in my_list:
                ppyy = pinyin(cizu, heteronym=True)
                # print(f"ppyy: {ppyy}")
                i = 0
                while i<len(cizu):
                    body += f"<ruby>{cizu[i]}<rt>{ppyy[i][0]}</rt></ruby>"
                    i += 1
            juzi=""
        body +="</p>"

body += ""
# print(body)

from jinja2 import Template

f2 = open("./templates/template.html","r")
mystr = ""
for i in f2.readlines():
    mystr += i

template = Template(mystr)
content = template.render(title=name, content=body)

with open(f"{name}.html","w") as f:
    f.write(content)
