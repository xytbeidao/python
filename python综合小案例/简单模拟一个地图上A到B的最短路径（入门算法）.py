from collections import deque  # 导入队列结构，用于BFS广度搜索

# 定义地图
grid = [
    ["S", "0", "1", "0", "E"],  # 0 表示能走，1 表示障碍，S是起点，E是终点
    ["1", "0", "1", "0", "1"],
    ["0", "0", "0", "0", "0"]
]

rows = len(grid)         # 地图有几行
cols = len(grid[0])      # 地图每行有几列

# 定义四个方向：上、下、左、右（坐标变化量）
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 找起点和终点坐标
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            start = (i, j)  # 起点坐标
        if grid[i][j] == "E":
            end = (i, j)    # 终点坐标

# BFS 搜索最短路径
def bfs(start, end):
    queue = deque()
    queue.append((start, [start]))  # 队列元素是 (当前坐标, 到这里的路径)

    visited = set()  # 记录访问过的节点，避免走回头路

    while queue:
        (x, y), path = queue.popleft()  # 取出当前点和到这里的路径

        if (x, y) == end:  # 如果到达终点
            return path  # 返回路径

        visited.add((x, y))  # 标记为已访问

        for dx, dy in directions:  # 尝试四个方向
            nx, ny = x + dx, y + dy  # 计算新坐标
            # 检查新坐标是否在地图范围内、能走、没访问过
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "1" and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))  # 加入队列，并把路径更新

    return None  # 如果走不到终点

# 调用函数并打印结果
result = bfs(start, end)

if result:
    print("找到最短路径：")
    for step in result:
        print(step)  # 打印每一步坐标
else:
    print("无法到达终点")
