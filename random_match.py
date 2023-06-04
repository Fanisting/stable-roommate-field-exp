# 本程序用于处理孩子端匹配倾向数据的处理，匹配采用Random Match
# 作者：范徐航, 2023.6.4
# 注意事项：
# 程序默认单个问卷文件中，孩子的名字是唯一确定的，不存在重名情况
# 默认的preference list是不完整的，程序会随机补足list

import pandas as pd
import os, random
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
    if filename.endswith(".xlsx"):
        print('\n 处理文件: ', filename)
        # 读取文件
        filepath = os.path.join(class_dir, filename)
        df = pd.read_excel(filepath)

        # Random Match
        # 将 "name" 列的值转换为列表
        names = df.loc[:, 'name'].tolist()
        name_temp = names.copy()
        pairs = {}
        while name_temp:
            name = random.choice(name_temp)
            name_temp.remove(name)
            if name_temp:
                peer = random.choice(name_temp)
                name_temp.remove(peer)
            else: # 考虑奇数的情况
                peer = '实验员'
            
            pairs[name] = peer
            pairs[peer] = name
        # Create 'peer_name' based on the dict "pairs"
        df['peer_name'] = df['name'].map(pairs)

        # 添加 Peer数据
        # 遍历字典的键值对，拼接数据
        merged_data = []
        for name in names:
            # 获取peer对应的行
            own_df = df[df['name'] == name]
            peer_df = df[df['name'] == pairs[name]].filter(regex='^(?!pref)')
            # Drop the 'name' and 'peer_name' variables
            peer_df = peer_df.drop(['name', 'peer_name'], axis=1)
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
        print("\n数据表\n", result)
        # 将 'name' 列移动到第一列
        new_order = ['name'] + [col for col in result.columns if col != 'name']
        result = result[new_order]
        # 导出
        # 构建"class"文件夹的绝对路径
        outcome_dir = os.path.join(script_dir, "outcomes")
        csv_name = filename[:-5]+"_random"+".csv"
        path = os.path.join(script_dir, csv_name)
        path.replace('\\', '/')
        result.to_csv(path, index=False)




