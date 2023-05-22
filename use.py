# 本程序用于处理孩子端匹配倾向数据的处理，匹配采用stable roommate matching
# 作者：范徐航, 2023.5.19
# 本程序使用了开源程序库来实现算法部分： https://github.com/charlierproctor/matching_algorithm
# 注意事项：
# 程序默认单个问卷文件中，孩子的名字是唯一确定的，不存在重名情况
# 本程序适用于两人小组配对，因此总人数为奇数时会提前随机排除一人，将该同学在生成结果中改名为"张三(out)"
# 默认的preference list是不完整的，程序会随机补足list

import matchmaker
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
    print('\n 处理文件: ', filename)
    if filename.endswith(".xlsx"):
        # 读取文件
        filepath = os.path.join(class_dir, filename)
        df = pd.read_excel(filepath)
        # 奇数时排除
        people_num = df.shape[0] - 1
        # if people_num % 2 == 1:
        #     # 随机选择一行，并将其对应的 'excluded' 特征设置为 1
        #     drop_index = random.choice(df.index[1:])
        #     drop_name = df.loc[[drop_index]]
        #     drop_name['peer'] = 'excluded'
        #     df.drop(drop_index, inplace=True)
        # 将 "name" 列的值转换为列表
        name_list = df.loc[:, 'name'].tolist()
        # 随机补全prefs list
        num_prefs = sum(col.startswith("pref") for col in df.columns) # 计算pref开头的vars (i.e. pref list length)
        for i in range(num_prefs+1, people_num+1): # 补全prefs list， 准备填充
            col_name = f"pref{i}"
            df[col_name] = 'none'
        for index, row in df.iterrows():
            # 将当前行转换为字典类型
            row_dict = dict(row)
            # 获取以"pref"开头的键并将它们添加到另一个字典中
            pref_dict = {k: v for k, v in row_dict.items() if k.startswith("pref") or k=="name"}
            pref_dict = dict(sorted(pref_dict.items(), key=lambda x: x[0])) # sort
            # 获取keys and values
            keys = pref_dict.keys()
            values = pref_dict.values() # 存在none的排序
            # 找出不是none的list
            part_name = [x for x in values if x != "none"]
            # 取出不包括list中名字的列表，并随机化
            temp = [x for x in name_list if x not in part_name]
            random.shuffle(temp)
            # 将字典pref_dict更新为新的值
            pref_dict.update(dict(zip(keys, part_name + temp)))
            # 更新
            df.loc[index, keys] = list(pref_dict[x] for x in keys)
        df = df.sort_index(axis=1)
        print("更新后的配对：\n", df.head())
        # 对列名按照索引进行排序
        df = df.reindex(sorted(df.columns), axis=1)
        # 导出
        # 对列名按照索引进行排序
        df = df.reindex(sorted(df.columns), axis=1)
        # 选取需要的列
        cols = ["name"] + [col for col in df.columns if col.startswith("pref")]
        # 数据表转为字典
        prefs = df[cols].set_index('name').T.to_dict('list')
        # Input: df of preferences df[name, pref-1 to pref-n]
        # Output: the matching outcome (stable roommate matching)
        # execute the match
        stable, outcome = matchmaker.execute(prefs)
        print("Matching outcome: \n")
        print("配对：", outcome)
        # 添加 Peer数据
        # 考虑人数为奇数下的空值问题
        no_peer = "none"
        for i in outcome:
            if outcome[i] == []:
                no_peer = i
        # print('no peer is', no_peer)
        # 遍历字典的键值对，拼接数据
        merged_data = []
        for name in outcome.keys():
            if name == no_peer:
                merged_df = df[df['name'] == no_peer]
                merged_data.append(merged_df)
                continue
            else:
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
        print("\n数据表\n", result)
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




