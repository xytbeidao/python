import hashlib

# 1. 模拟用户数据库
users = {}

# 2. 注册功能
def register(username, password):
    if username in users:
        print("用户名已存在，请换一个！")
        return False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print(f"用户 {username} 注册成功！")
    return True

# 3. 登录功能
def login(username, password):
    if username not in users:
        print("用户名不存在！")
        return False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if users[username] == hashed_password:
        print(f"用户 {username} 登录成功！")
        return True
    else:
        print("密码错误！")
        return False

# 测试流程
register("alice", "mypassword123")
register("bob", "securepass")
login("alice", "mypassword123")
login("bob", "wrongpass")
login("charlie", "test")
