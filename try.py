import pandas as pd
import os

# Get the directory of the .py file
file_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the .py file directory
os.chdir(file_dir)

df = pd.read_csv('test.csv', encoding='gbk')
# Get the variable names from the columns of the DataFrame
header = df.columns.tolist()

# Convert the DataFrame to a matrix
matrix = [header] + df.values.tolist()

name_mapping = {
    '张伟': 'John',
    '周亮': 'Simon',
    '邓红': 'Emily',
    '宋明': 'Mark',
    '范冰': 'Brian',
    '萧莉': 'Lily',
    '李娜': 'Natalie',
    '杨帆': 'Ethan',
    '董林': 'Dylan',
    '汪涛': 'Walter',
    '袁雪': 'Grace',
    '王芳': 'Alice',
    '崔琳': 'Linda',
    '谢燕': 'Oliver',
    '程菲': 'Emma',
    '任磊': 'Sophie',
    '刘洋': 'Nora',
    '郑华': 'Henry',
    '曹春': 'Edward',
    '吴秀英': 'Chris',
    '马宇': 'Michael',
    '许文': 'Amy',
    '孙健': 'Adam',
    '潘辉': 'Eric',
    '彭军': 'Mason',
    '赵雷': 'Liam',
    '陈晨': 'Charlie',
    '钟立': 'Benjamin',
    '冯雪': 'Olivia',
    '肖波': 'Matthew'
}

for x in matrix:
    for y in x:
        if y in name_mapping:
            x[x.index(y)] = name_mapping[y]

print(matrix)
df = pd.DataFrame(matrix)
df.to_csv('test_en.csv', encoding='gbk', index=False)
