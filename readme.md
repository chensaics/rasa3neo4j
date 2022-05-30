
**基于rasa 3.x + neo4j的医疗知识图谱问答对话机器人。**

首先安装neo4j图数据库，

将process_data/create_graph.py中的username 和 password修改为自己的，运行文件写入数据。

安装必要的包：例如spacy 和 预训练模型 zh_core_web_md

rasa train命令及相关参数训练模型

rasa run actions -vv ：启动rasa sdk action server

rasa shell运行测试

声明：

数据来源根据刘焕勇老师提供的开源医疗数据，请勿商用。


