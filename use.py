# 本程序用于处理孩子端匹配倾向数据的处理，匹配采用stable roommate matching
# 作者：范徐航, 2023.5.19
# 本程序使用了开源程序库 https://github.com/charlierproctor/matching_algorithm、
# 注意事项：
# 程序默认单个问卷文件中，孩子的名字是唯一确定的，不存在重名情况

import matchmaker
import pandas as pd
import os
# 美化终端输出
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 设置打印宽度(**重要**)

# 获取当前脚本文件所在的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建"class"文件夹的绝对路径
class_dir = os.path.join(script_dir, "class")

# 遍历所有.xlsx文件，并读取数据
for filename in os.listdir(class_dir):
    print('filename is', filename)
    if filename.endswith(".xlsx"):
        # 读取文件
        filepath = os.path.join(class_dir, filename)
        print(filepath)
        df = pd.read_excel(filepath)
        # 在此处添加对数据的处理
        print(df.head())
        # 对列名按照索引进行排序
        df = df.reindex(sorted(df.columns), axis=1)
        # 选取需要的列
        cols = ["name"] + [col for col in df.columns if col.startswith("pref")]
        # 数据表转为字典
        prefs = df[cols].set_index('name').T.to_dict('list')
        print(prefs)
        # Input: df of preferences df[name, pref-1 to pref-n]
        # Output: the matching outcome (stable roommate matching)
        # execute the match
        stable, outcome = matchmaker.execute(prefs)
        print("Final outcome is: \n")
        print(outcome)
        # 添加 Peer数据
        # 遍历字典的键值对，拼接数据
        merged_data = []
        for name in outcome.keys():
            # 获取peer对应的行
            own_df = df[df['name'] == name]
            peer_df = df[df['name'] == outcome[name][0]].filter(regex='^(?!pref)')
            # 在变量名上加上 "peer_" 前缀
            peer_df = peer_df.add_prefix("peer_")
            # 将两个 DataFrame 横向合并
            own_df.reset_index(drop=True, inplace=True) # 删除原来的索引
            peer_df.reset_index(drop=True, inplace=True)
            merged_df = pd.concat([own_df, peer_df], axis = 1)
            # print(merged_df)
            merged_data.append(merged_df)
        # 合并所有新的数据框
        result = pd.concat(merged_data, axis=0)
        print(result)
        # 将 'name' 列移动到第一列
        new_order = ['name'] + [col for col in result.columns if col != 'name']
        result = result[new_order]
        # 导出
        # 构建"class"文件夹的绝对路径
        outcome_dir = os.path.join(script_dir, "outcomes")
        csv_name = filename[:-5]+"_匹配"+".csv"
        path = os.path.join(script_dir, csv_name)
        path.replace('\\', '/')
        result.to_csv(path, index=False)




