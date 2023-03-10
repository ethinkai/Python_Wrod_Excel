import easygui
from load_on_telecom_web_function import my_OpenUrl
#v_str1 = 'h'
#v_str2 = 'shijian'
#v_str1 = 'z'
#v_str2 = 'wenlv'
#交互输入
#v_str1 = input('互联网输入h， 政务外网输入z:')
#v_str2 = input('单位拼音前两位，如市监局shijian:')
#交互界面输入
v_str1 = easygui.enterbox('互联网输入h， 政务外网输入z :')
v_str2 = easygui.enterbox('单位拼音前两位，如市监局shijian:')
my_OpenUrl(v_str1, v_str2)