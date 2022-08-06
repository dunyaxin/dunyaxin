from tkinter import *
import math
import time
import numpy as np
LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("新井踏勘及老井定位辅助软件V1.0")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1100x800+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label2 = Label(self.init_window_name, text="待处理数据，格式：井1 36000000 3900000")
        self.init_data_label2.grid(row=0, column=0)
        self.init_data_label = Label(self.init_window_name,justify=LEFT, text="使用说明:\n1、井号及坐标可直接从excel里复制后粘贴进来\n2、软件生的gpx文件在D盘根目录下\n3、如有疑问联系0934-8386014或者dunyx_cq@petrochina.com.cn\n4、Copyright@长庆油田采油十二厂地质研究所")
        self.init_data_label.grid(row=21, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12, rowspan=10, columnspan=10)
        self.log_label = Label(self.init_window_name, text="日志-转换记录")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=62, height=35)  #原始数据录入框
        self.scroll1 = Scrollbar(self.init_window_name)
        # 放到窗口的右侧, 填充Y竖直方向
        self.scroll1.grid(row=1, column=0,rowspan=10, columnspan=19,sticky=N+S)
        self.scroll1.config(command=self.init_data_Text.yview)

        self.init_data_Text.config(yscrollcommand=self.scroll1.set)

        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.scroll2 = Scrollbar(self.init_window_name)
        # 放到窗口的右侧, 填充Y竖直方向
        self.scroll2.place(x=1040, y=25,height=650)#指定 上下展开
        self.scroll2.config(command=self.result_data_Text.yview)

        self.result_data_Text.config(yscrollcommand=self.scroll2.set)

        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="3度带转换", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="6度带转换", bg="lightblue", width=10,command=self.str_trans_to_md6)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=11)
        # self.can = Canvas(self.init_window_name ,width=150, height=150)  # 图标
        # self.filename = PhotoImage(file="12.gif")
        # self.image =self.can.create_image(0, 0, anchor="nw", image=self.filename)
        # self.can.place(x=5, y=760)#指定 上下展开

    def GetLatLon2(self,B, C, IsSix):
        # 带号
        pi = math.pi
        D = math.trunc(C / 1000000)
        # 中央经线（单位：弧度）
        K = 0
        if IsSix == 6:
            K = D * 6 - 3  # 6度带计算
        else:
            K = D * 3  # 3度带计算
        L = B / (6378245 * (1 - 0.006693421623) * 1.0050517739)
        M = L + (0.00506237764 * math.sin(2 * L) / 2 - 0.00001062451 * math.sin(4 * L) / 4 + 0.0000002081 * math.sin(
            6 * L) / 6) / 1.0050517739
        N = L + (0.00506237764 * math.sin(2 * M) / 2 - 0.00001062451 * math.sin(4 * M) / 4 + 0.0000002081 * math.sin(
            6 * M) / 6) / 1.0050517739
        O = L + (0.00506237764 * math.sin(2 * N) / 2 - 0.00001062451 * math.sin(4 * N) / 4 + 0.0000002081 * math.sin(
            6 * N) / 6) / 1.0050517739
        P = L + (0.00506237764 * math.sin(2 * O) / 2 - 0.00001062451 * math.sin(4 * O) / 4 + 0.0000002081 * math.sin(
            6 * O) / 6) / 1.0050517739
        Q = L + (0.00506237764 * math.sin(2 * P) / 2 - 0.00001062451 * math.sin(4 * P) / 4 + 0.0000002081 * math.sin(
            6 * P) / 6) / 1.0050517739
        R = L + (0.00506237764 * math.sin(2 * Q) / 2 - 0.00001062451 * math.sin(4 * Q) / 4 + 0.0000002081 * math.sin(
            6 * Q) / 6) / 1.0050517739
        S = math.tan(R)
        T = 0.006738525415 * (math.cos(R)) ** 2
        U = 6378245 / math.sqrt(1 - 0.006693421623 * (math.sin(R)) ** 2)
        V = 6378245 * (1 - 0.006693421623) / (math.sqrt((1 - 0.006693421623 * (math.sin(R)) ** 2))) ** 3
        W = 5 + 3 * S ** 2 + T - 9 * T * S ** 2
        X = 61 + 90 * S ** 2 + 45 * S ** 4
        Y = 1 + 2 * S ** 2 + T ** 2
        Z = 5 + 28 * S ** 2 + 24 * S ** 4 + 6 * T + 8 * T * S ** 2
        Lat = (180 / pi) * (
                    R - (C - D * 1000000 - 500000) ** 2 * S / (2 * V * U) + (C - D * 1000000 - 500000) ** 4 * W / (
                        24 * U ** 3 * V) - (C - D * 1000000 - 500000) ** 6 * X / (7200 * U ** 5 * V))
        Lon = (180 / pi) * (C - D * 1000000 - 500000) * (
                    1 - (C - D * 1000000 - 500000) ** 2 * Y / (6 * U ** 2) + (C - D * 1000000 - 500000) ** 4 * Z / (
                        120 * U ** 4)) / (U * math.cos(P))
        Lat = Lat
        Lon = K + Lon
        return (Lon, Lat)
    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END)
        try:
            #print("src =",src)
            myjw = src.split( )
            count=len(myjw)
            wellname=[]
            wx=np.zeros(count)
            wy=np.zeros(count)
            rest = []
            j=0
            self.result_data_Text.delete(1.0, END)
            for i in range(0,count,3):
                wellname.append(myjw[i])
                wx[j] = myjw[i+1]
                wy[j] = myjw[i+2]
                rest.append(self.GetLatLon2(wy[j], wx[j], 3))

                # self.result_data_Text.insert(1.0,"\n")
                j = j + 1
            #print(myMd5_Digest)
            #输出到界面
            npjw = np.array(rest)
            for x in rest:
                self.result_data_Text.insert("insert", x)
                self.result_data_Text.insert("insert", "\n")
                j += 1
            self.write_log_to_Text("INFO:坐标转换成功并在D盘生成了gpx文件")
            # self.result_data_Text.insert("insert", npjw)
            maxjd=np.max(npjw[:,0])
            minjd = np.min(npjw[:,0])
            maxwd=np.max(npjw[:,1])
            minwd = np.min(npjw[:,1])
            count=len(npjw)

            fo = open("D:/转换完成的坐标可在谷歌地球和奥维地图上打开.gpx", "w", encoding='utf-8')
            # 写入头文件
            fo.write(
                '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" creator="MapSource 6.15.6" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">  <metadata>    <link href="http://www.garmin.com">      <text>Garmin International</text>    </link>    <time>2016-03-17T09:28:21Z</time>    ')
            # 写入井号和坐标
            fo.write(
                '<bounds maxlat="'+str(maxjd)+'" maxlon="'+str(maxwd)+'" minlat="'+str(minjd)+'" minlon="'+str(minwd)+'"/>  </metadata>  ')
            for i in range(0,count,1):
                fo.write(
                    '<wpt lat="'+str(npjw[i,1])+'" lon="'+str(npjw[i,0])+'">    <time>2016-03-17T09:26:28Z</time>    <name>'+str(wellname[i])+'</name>    <sym>Flag, Blue</sym>    <extensions>      <gpxx:WaypointExtension xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3">        <gpxx:DisplayMode>SymbolAndName</gpxx:DisplayMode>      </gpxx:WaypointExtension>    </extensions>  </wpt>')
                # 写入结尾
            fo.write('</gpx>')
        except:
            self.write_log_to_Text("INFO:请输入正确的井号及坐标格式，井号，坐标之间均用空格隔开")

    def str_trans_to_md6(self):
        src = self.init_data_Text.get(1.0,END)
        try:
            #print("src =",src)
            myjw = src.split( )
            count=len(myjw)
            wellname=[]
            wx=np.zeros(count)
            wy=np.zeros(count)
            rest = []
            j=0
            self.result_data_Text.delete(1.0, END)
            for i in range(0,count,3):
                wellname.append(myjw[i])
                wx[j] = myjw[i+1]
                wy[j] = myjw[i+2]
                rest.append(self.GetLatLon2(wy[j], wx[j], 6))

                # self.result_data_Text.insert(1.0,"\n")
                j = j + 1
            #print(myMd5_Digest)
            #输出到界面
            npjw = np.array(rest)
            for x in rest:
                self.result_data_Text.insert("insert", x)
                self.result_data_Text.insert("insert", "\n")
                j += 1
            self.write_log_to_Text("INFO:坐标转换成功并在D盘生成了gpx文件")
            # self.result_data_Text.insert("insert", npjw)
            maxjd=np.max(npjw[:,0])
            minjd = np.min(npjw[:,0])
            maxwd=np.max(npjw[:,1])
            minwd = np.min(npjw[:,1])
            count=len(npjw)

            fo = open("D:/井位踏勘定位软件导出的文件可在谷歌地球和奥维地图上打开.gpx", "w", encoding='utf-8')
            # 写入头文件
            fo.write(
                '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" creator="MapSource 6.15.6" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">  <metadata>    <link href="http://www.garmin.com">      <text>Garmin International</text>    </link>    <time>2016-03-17T09:28:21Z</time>    ')
            # 写入井号和坐标
            fo.write(
                '<bounds maxlat="'+str(maxjd)+'" maxlon="'+str(maxwd)+'" minlat="'+str(minjd)+'" minlon="'+str(minwd)+'"/>  </metadata>  ')
            for i in range(0,count,1):
                fo.write(
                    '<wpt lat="'+str(npjw[i,1])+'" lon="'+str(npjw[i,0])+'">    <time>2016-03-17T09:26:28Z</time>    <name>'+str(wellname[i])+'</name>    <sym>Flag, Blue</sym>    <extensions>      <gpxx:WaypointExtension xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3">        <gpxx:DisplayMode>SymbolAndName</gpxx:DisplayMode>      </gpxx:WaypointExtension>    </extensions>  </wpt>')
                # 写入结尾
            fo.write('</gpx>')
        except:
            self.write_log_to_Text("INFO:请输入正确的井号及坐标格式")



    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()