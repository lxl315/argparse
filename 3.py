
import re,argparse
import os
query=[]
def gci(filepath):
    dirs = os.listdir(filepath)
    for i in dirs:
        i_d = os.path.join(filepath, i)
        if os.path.isdir(i_d):
            gci(i_d)
        else:            
            if os.path.splitext(i_d)[1]=='.xls':
                query.append(i_d)
    return query        

def openfile(files):
    date=[]
    with open(files, "r", encoding='utf-8') as f:
        date=f.readlines()

    return ''.join(date)


def delsheet(str1,outfile,*kw): 
    
    for value in kw[0]:
        print('--->开始在'+outfile+'文件中查找  '+value+'sheet')
        i = re.search(r'<Worksheet ss:Name="' +
                          value+'">(.*?)</Worksheet>', str1, re.S)
        if i:           
                                   
            str1 = str1.replace(i.group(0),'')            
            
            print(outfile+'删除完毕！')
            with open(outfile, "w", encoding='utf-8') as f:
                f.write(str1)       

        else:
            print(outfile,'不存在'+value+'sheet')                               



if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='多余sheet 删除工具 By LXL')
    parser.add_argument('-f',type=str,help='请输入要删除的文件路径',default=False)
    parser.add_argument('--s1',type=str,nargs='+',help='请输入要删除的列名，支持多个列名，列名之前需要一个空格')
    args= parser.parse_args()
    print(args.f) 
    print(args.s1)
    lists=gci(args.f)
    print('找到 %s 个文件' % len(lists))   
    for k in lists:
        delsheet(openfile(k),k,args.s1)        
    
    
