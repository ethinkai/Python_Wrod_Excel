from fileinput import close
import json
#v_File = open('D:\\vscode_PythonSource\\telecompwd.txt', 'r')
#print(v_File.read())
#v_File.close()

#with open('D:\\vscode_PythonSource\\telecompwd.txt', 'r') as v_Json_Res:
#    v_Json = json.load(v_Json_Res)
#    print(v_Json['v_Url']['v_UrlHuLianWang'])

#定义获取函数
def my_GetData(str1="",str2=""):
    #给参数设置默认值，才能使用字符串的韩式
    #对传入的参数不区分大小写
    str1 = str1.lower()
    str2 = str2.lower()
    with open('D:\\vscode_PythonSource\\telecompwd.txt', 'r') as v_Json_Res:
        v_Json = json.load(v_Json_Res)
        #市监局
        if str1 == 'h' and str2 == 'shijian':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ShiChangJianGuan']['v_Username'], 
                    v_Json['v_Data']['v_ShiChangJianGuan']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'shijian':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ShiChangJianGuan']['v_Username'], 
                    v_Json['v_Data']['v_ShiChangJianGuan']['v_Password']['v_PWD_ZhengWu']]
        #文旅厅
        elif str1 == 'h' and str2 == 'wenlv':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ah_wenlvting']['v_Username'], 
                    v_Json['v_Data']['v_ah_wenlvting']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'wenlv':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ah_wenlvting']['v_Username'], 
                    v_Json['v_Data']['v_ah_wenlvting']['v_Password']['v_PWD_ZhengWu']]
        #林业局
        elif str1 == 'h' and str2 == 'linye':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ah_linyeju']['v_Username'], 
                    v_Json['v_Data']['v_ah_linyeju']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'linye':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ah_linyeju']['v_Username'], 
                    v_Json['v_Data']['v_ah_linyeju']['v_Password']['v_PWD_ZhengWu']]
        #自然资源厅
        elif str1 == 'h' and str2 == 'ziran':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ah_ziranziyuanting']['v_Username'], 
                    v_Json['v_Data']['v_ah_ziranziyuanting']['v_Password']['v_PWD_ZhengWu']]
        elif str1 == 'z' and str2 == 'ziran':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ah_ziranziyuanting']['v_Username'], 
                    v_Json['v_Data']['v_ah_ziranziyuanting']['v_Password']['v_PWD_ZhengWu']]
        #人防办
        elif str1 == 'h' and str2 == 'renfang':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ah_renfangban']['v_Username'], 
                    v_Json['v_Data']['v_ah_renfangban']['v_Password']['v_PWD_ZhengWu']]
        elif str1 == 'z' and str2 == 'renfang':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ah_renfangban']['v_Username'], 
                    v_Json['v_Data']['v_ah_renfangban']['v_Password']['v_PWD_ZhengWu']]
        #药监局
        elif str1 == 'h' and str2 == 'yaojian':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ah_yaojianju']['v_Username'], 
                    v_Json['v_Data']['v_ah_yaojianju']['v_Password']['v_PWD_ZhengWu']]
        elif str1 == 'z' and str2 == 'yaojian':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ah_yaojianju']['v_Username'], 
                    v_Json['v_Data']['v_ah_yaojianju']['v_Password']['v_PWD_ZhengWu']]
        #乡村振兴局
        elif str1 == 'h' and str2 == 'xiangcun':
            return [v_Json['v_Url']['v_UrlHuLianWang'], 
                    v_Json['v_Data']['v_ah_xiangcunzhenxing[]ju']['v_Username'], 
                    v_Json['v_Data']['v_ah_xiangcunzhenxingju']['v_Password']['v_PWD_ZhengWu']]
        elif str1 == 'z' and str2 == 'xiangcun':
            return [v_Json['v_Url']['v_UrlZhengWuWang'], 
                    v_Json['v_Data']['v_ah_xiangcunzhenxingju']['v_Username'], 
                    v_Json['v_Data']['v_ah_xiangcunzhenxingju']['v_Password']['v_PWD_ZhengWu']]
        #2022-11-8新增安全资源池
        elif str1 == 'h' and str2 == 'sec':
            return [v_Json['v_Url']['v_Url_Sec_HuLian'],
                    v_Json['v_Data']['v_sec_wanglei']['v_Username'],
                    v_Json['v_Data']['v_sec_wanglei']['v_Password']]
        elif str1 == 'z' and str2 == 'sec':
            return [v_Json['v_Url']['v_Url_Sec_ZhengWu'],
                    v_Json['v_Data']['v_sec_wanglei']['v_Username'],
                    v_Json['v_Data']['v_sec_wanglei']['v_Password']]
        #2022-12-6新增国资委政务外网
        elif str1 == 'h' and str2 == 'guoziwei':
            return [v_Json['v_Url']['v_UrlHuLianWang'],
                    v_Json['v_Data']['v_ah_shengguoziwei']['v_Username'],
                    v_Json['v_Data']['v_ah_shengguoziwei']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'guoziwei':
            return [v_Json['v_Url']['v_UrlZhengWuWang'],
                    v_Json['v_Data']['v_ah_shengguoziwei']['v_Username'],
                    v_Json['v_Data']['v_ah_shengguoziwei']['v_Password']['v_PWD_ZhengWu']]
        #2022-12-22新增省检察院
        elif str1 == 'h' and str2 == 'jiancha':
            return [v_Json['v_Url']['v_UrlHuLianWang'],
                    v_Json['v_Data']['v_ah_shengjianchayuan']['v_Username'],
                    v_Json['v_Data']['v_ah_shengjianchayuan']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'jiancha':
            return [v_Json['v_Url']['v_UrlZhengWuWang'],
                    v_Json['v_Data']['v_ah_shengjianchayuan']['v_Username'],
                    v_Json['v_Data']['v_ah_shengjianchayuan']['v_Password']['v_PWD_ZhengWu']]
        #2022-12-22新增省委机要局
        elif str1 == 'h' and str2 == 'jiyao':
            return [v_Json['v_Url']['v_UrlHuLianWang'],
                    v_Json['v_Data']['v_ah_jiyaoju']['v_Username'],
                    v_Json['v_Data']['v_ah_jiyaoju']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'jiyao':
            return [v_Json['v_Url']['v_UrlZhengWuWang'],
                    v_Json['v_Data']['v_ah_jiyaoju']['v_Username'],
                    v_Json['v_Data']['v_ah_jiyaoju']['v_Password']['v_PWD_ZhengWu']]
        #信访局
        elif str1 == 'h' and str2 == 'xinfang':
            return [v_Json['v_Url']['v_UrlHuLianWang'],
                    v_Json['v_Data']['v_ah_xinfangju']['v_Username'],
                    v_Json['v_Data']['v_ah_xinfangju']['v_Password']['v_PWD_HuLian']]
        elif str1 == 'z' and str2 == 'xinfang':
            return [v_Json['v_Url']['v_UrlZhengWuWang'],
                    v_Json['v_Data']['v_ah_xinfangju']['v_Username'],
                    v_Json['v_Data']['v_ah_xinfangju']['v_Password']['v_PWD_ZhengWu']]
        else:
            return "1" 
    #print(my_GetData('h', 'shijian')[0] + "  "+ my_GetData('h', 'shijian')[1] + "  " + my_GetData('h', 'shijian')[2])
    #close(v_Json_Res)
