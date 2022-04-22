"""
安装及使用
"""
import streamlit as st


class Install:
    def __init__(self):
        pass

    def installInstruction(self):
        """安装说明"""
        st.write("安装说明")
        with st.expander("点此展开/关闭", expanded=True):
            st.write("Windows/Linux系统（建议使用Linux）")
            st.write("Python3.6")
            st.write("Pytorch1.7及以上")
            st.write("安装Streamlit")
            st.write("将该项目解压在本地路径，运行detect.py文件即可进行终端测试。也可运行main1.py文件进行浏览器可视化操作")
            pass
        pass

    def useDirect(self):
        """使用说明"""
        st.write("使用说明")
        with st.expander("点此展开/关闭", expanded=True):
            st.write("1、由于数据版权问题，该项目未将使用数据全部进行公布，只在dataset文件夹中存留两张测试数据")
            st.write("2、运行detect.py文件，将被检测的文件路径修改为自己本地存放路径")
            st.write("3、启动main1.py文件，命令如下(必须在所在文件夹路径下执行):streamlit run main1.py")
            pass
    pass
