import pandas as pd                      # 用于创建和读取 CSV 文件
import matplotlib.pyplot as plt          # 用于绘图
import matplotlib.font_manager as fm     # 用于设置中文字体
import matplotlib.cm as cm               # 用于配色方案

# === 步骤1：自动创建 CSV 文件 === #
data = {
    "时间": [1, 2, 3, 4, 5],
    "温度": [22, 24, 23, 25, 26],
    "湿度": [60, 63, 62, 65, 66],
    "压力": [101, 101, 100, 100, 100]
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)       # 保存为 UTF-8 格式的 data.csv 文件

# === 步骤2：自动设置支持中文的字体 === #
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
found_font = None
for font_path in font_list:
    font_name = fm.FontProperties(fname=font_path).get_name()
    if any(word in font_name for word in ['SimHei', 'Microsoft YaHei', '宋体', '黑体', '思源', '华文']):
        found_font = font_path
        break

if found_font:
    chinese_font = fm.FontProperties(fname=found_font).get_name()
    plt.rcParams['font.family'] = chinese_font
    print(f"使用的中文字体为：{chinese_font}")
else:
    print("未找到中文字体，图表中文字可能无法显示")

plt.rcParams['axes.unicode_minus'] = False   # 正确显示负号

# === 步骤3：读取 CSV 数据并绘制折线图 === #
data = pd.read_csv("data.csv")          # 读取 CSV 文件
x = data.iloc[:, 0]                     # 第一列作为 X 轴
y_data = data.iloc[:, 1:]               # 其余列作为多组 Y 数据

# 创建图形窗口
plt.figure(figsize=(10, 6))             # 设置图像大小为10x6英寸

# 设置颜色循环
colors = cm.get_cmap('tab10', len(y_data.columns))

# 绘制每一条折线
for i, column in enumerate(y_data.columns):
    plt.plot(x, y_data[column],
             label=column,
             color=colors(i),
             linestyle='-',
             linewidth=2,
             marker='o')

# 设置标题、标签
plt.title("多折线图示例", fontsize=14)
plt.xlabel("时间（天）", fontsize=12)
plt.ylabel("测量值", fontsize=12)

# 网格、图例、美化
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="图例", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 保存与显示图像
plt.savefig("multi_line_chart.png")     # 保存图像为 PNG 文件
plt.show()                              # 显示图形窗口