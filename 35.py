#!/usr/bin/env python
import argparse
def plus(a,*kw): #一个必选参数 和可变参数    
    num =0
    
    for i in kw[0]:   #kw 是tuple 格式的 kw[0] 返回这个tuple 里第一个参数
        print(a+i)
        
        
    print(a+i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of the program')
    parser.add_argument('-f',type=str,help='please input num1')
    parser.add_argument('--sheet',type=str,nargs='+') #可变参数穿进去集合

    args= parser.parse_args()
    
    plus(args.f,args.sheet)  #传入必选参数和可变参数