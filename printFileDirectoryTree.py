# 目录树
import os


def travelTree(currentPath, count):
    if not os.path.exists(currentPath):
        return
    if os.path.isfile(currentPath):
        fileName = os.path.basename(currentPath)
        print('\t' * count + '├── ' + fileName)
    elif os.path.isdir(currentPath):
        print('\t' * count + '├── ' + currentPath)
        pathList = os.listdir(currentPath)
        for eachPath in pathList:
            travelTree(currentPath + '/' + eachPath, count + 1)


travelTree('D:/projects/rasa3neo4j/', 1)

'''
├── QASystemOnMedicalKG
    ├── answer_search.py               # 问题查询及返回
    ├── build_medicalgraph.py          # 将结构化json数据导入neo4j
    ├── chatbot_graph.py               # 问答程序脚本
    ├── QASystemOnMedicalKG/data
        ├── hepatopathy.json           # 肝病知识数据
        ├── medical.json               # 全科知识数据
    ├── QASystemOnMedicalKG/dict
        ├── check.txt                  # 诊断检查项目实体库
        ├── deny.txt                   # 否定词库
        ├── department.txt             # 医疗科目实体库
        ├── disease.txt                # 疾病实体库
        ├── drug.txt                   # 药品实体库
        ├── food.txt                   # 食物实体库
        ├── producer.txt               # 在售药品库
        ├── symptom.txt                # 疾病症状实体库
    ├── QASystemOnMedicalKG/prepare_data
        ├── build_data.py              # 数据库操作脚本
        ├── data_spider.py             # 数据采集脚本
        ├── max_cut.py                 # 基于词典的最大前向/后向匹配
    ├── question_classifier.py         # 问句类型分类脚本
    ├── question_parser.py             # 问句解析脚本


├── actions.py
├── config.yml
├── credentials.yml
├── D:/projects/rasa3neo4j//data
    ├── D:/projects/rasa3neo4j//data/jieba_userdict
        ├── Departments_dic.txt
        ├── Diseases_dic.txt
        ├── Drugs_dic.txt
        ├── Foods_dic.txt
        ├── Symptoms_dic.txt
    ├── lookups.yml
    ├── D:/projects/rasa3neo4j//data/medical
        ├── D:/projects/rasa3neo4j//data/medical/lookup
            ├── Departments.txt
            ├── Departments.xlsx
            ├── Diseases.txt
            ├── Diseases.xlsx
            ├── Drugs.txt
            ├── Drugs.xlsx
            ├── Foods.txt
            ├── Foods.xlsx
            ├── Symptoms.txt
            ├── Symptoms.xlsx
            ├── txt2excel.py
    ├── nlu.yml
    ├── story.yml
    ├── synonyms.yml
├── domain.yml
├── endpoints.yml
├── D:/projects/rasa3neo4j//graph_database
├── D:/projects/rasa3neo4j//models
├── printFileDirectoryTree.py
├── D:/projects/rasa3neo4j//process_data
    ├── create_graph.py
    ├── drugs.csv
    ├── medical.json
    ├── producers.csv
    ├── rels_drug_producer.csv
    ├── __init__.py
├── readme.md
├── D:/projects/rasa3neo4j//tests
├── __init__.py
			
			'''
