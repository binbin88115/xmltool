xmltool
=======

a tool for cocos2dx that used to generate xml file and assosiated c++ code

=======

游戏客户端本地数据的存储是一个很重要的问题，一般情况下也是一个工作量挺大的模块。该工具提供一键生成xml文件及对应可读取该xml文件的c++代码。该c++代码部分使用c++11标准。因此编译器要支持C++11。

NOTE: 1）C++代码对xml的解析是使用第三方tinyxml库，因此需要将tinyxml导入到项目中，同时需要的情况下需要将tinyxml文件夹添加到项目的可搜索目录。即#include "tinyxml.h"就可以定位到tinyxml。

2）使用该C++代码，需要#include "XMLManager.h"头文件，并且XML_LOAD_DATA()方法提供对本地数据的加载，本地xml文件默认是放置于Resource目录下，可根据需要在XMLManager.cpp文件更改路径。访问某个数据对象可通过XML_DATASET宏来实现，对数据的读取C++代码提供了两个方法，分别为queryById和queryByCallback。前者根据id编号查找一条数据，后者通过传入一个回调函数来查找一条或多条数据。具体可参见XMLLoader。

3）该工具提供一个template.xlsx文件，用户的数据需要基于指定的格式填写。该工具并不支持用户自己定义的excel文件。（TIP：用户可以复制一份template.xlsx副本，并自定义文件名称。）

要成功运行该python文件，首先需要确保系统已安装python（版本是2.7），同时python方面对excel文件的解析是使用第三方的xlrd库。因此没有安装的话需要安装。
命令格式：python main.py excel.xlsx
          python main.py ../directory/excel.xls
          python main.py directory/excel.xls
如果没发生任何错误，运行完命令后，会在excel文件所在目录下生成xml和cpp两文件夹，分别存放导出的xml文件及对应的读取该xml文件的c++代码。
