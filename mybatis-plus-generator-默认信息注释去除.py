#################################################################
#                                                               #
#   @Author ChenJingZhuo                                        #
#                                                               #
#   @Date 2020-12-20 21:52                                      #
#                                                               #
#   @Version 0.0.1                                              #
#                                                               #
#   @QQ 3279838729                                              #
#                                                               #
#   @功能 删除mybatis-plus-generator默认生成的信息注释          #
#                                                               #
#################################################################


import os
import re
import chardet   #需要导入这个模块，检测编码格式

encode_first = True
encode_type = None
count = 0

# 删除默认信息注释
def deleteCommit(path):
    if path == None or path == '':
        deleteCommit(os.getcwd())
    elif not os.path.exists(path):
        print('该路径不存在')
        isContinue = input('是否重新输入？（y/n）：')
        if isContinue == 'y':
            deleteCommit(input('请输入要删除注释的全路径（默认当前路径）：'))
        else:
            exit('退出成功')

    fileDir_list = [fileDir for fileDir in os.listdir(path)]

    for fileDir in fileDir_list:
        if os.path.isdir(os.path.join(path,fileDir)):
            deleteCommit(os.path.join(path,fileDir))
        elif fileDir.endswith('.java'):
            openFile(os.path.join(path,fileDir))

# 若存在默认信息注释，则删除默认信息注释，之后重新保存
def openFile(filePath):
    global encode_first,encode_type,count
    if not os.path.exists(filePath):
        exit('文件不存在 => %s'%filePath)
    if encode_first:
        encode_first = False
        # 判断文件编码
        f = open(filePath,'rb') # 要有"rb"，如果没有这个的话，默认使用gbk读文件。
        content = f.read()
        encode_type = chardet.detect(content)['encoding']
        f.close()
    
    # 解决识别utf-8编码为ascii编码的错误
    if encode_type == 'ascii':
        encode_type = 'utf-8'

    with open(filePath,'r',encoding=encode_type) as f:
        content = f.read()
        findContent = re.findall(r'\n/\*\*\s*\*\s*<p>.*?\*/',content,re.S)
    if len(findContent) > 0:
        contentS = re.sub(r'\n/\*\*\s*\*\s*<p>.*?\*/','',content,1,re.S)
        with open(filePath,'w',encoding=encode_type) as f:
            f.write(contentS)
            count = count + 1
            print("已删除mybatis-plus-generator的信息注释：%-10d => %s" % (count, filePath))

if __name__ == "__main__":
    print(
"""
#################################################################
#                                                               #
#   @Author ChenJingZhuo                                        #
#                                                               #
#   @Date 2020-12-20 21:52                                      #
#                                                               #
#   @Version 0.0.1                                              #
#                                                               #
#   @QQ 3279838729                                              #
#                                                               #
#   @功能 删除mybatis-plus-generator默认生成的信息注释          #
#                                                               #
#################################################################
""")
    deleteCommit(input('请输入要删除注释的全路径（默认当前路径）：'))