import requests  # 用于发送 HTTP 请求
import os        # 用于文件目录操作
import re        # 正则表达式提取视频链接

# 你的 Cookie，请用引号括起来粘贴完整的 Cookie 字符串
cookie = "sid_tt=1385b319c171aa3fe5620654b4e66518; sid_ucp_v1=1.0.0-KDY0ODRmZTljOGFmNDkwZDU1NjA2NjRkNTZiYjU0ZTM0OTQ3YWZkZDkKIQi58IDewc2lARCisobCBhjvMSAMMMD5hrYGOAdA9AdIBBoCbHEiIDEzODViMzE5YzE3MWFhM2ZlNTYyMDY1NGI0ZTY2NTE4; ssid_ucp_v1=1.0.0-KDY0ODRmZTljOGFmNDkwZDU1NjA2NjRkNTZiYjU0ZTM0OTQ3YWZkZDkKIQi58IDewc2lARCisobCBhjvMSAMMMD5hrYGOAdA9AdIBBoCbHEiIDEzODViMzE5YzE3MWFhM2ZlNTYyMDY1NGI0ZTY2NTE4; strategyABtestKey=%221749129445.008%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1685%2C%5C%22screen_height%5C%22%3A948%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; ttwid=1%7CSaSwNfs4kafZWD4uCt-EbLV_704VX2VtlQ1c5N4j-nU%7C1749129442%7Ca83a2159f88f88a3978f0e3b4de736e81913c0366b9abe332470f170c808501c; uid_tt=5cef146a72998c8600488895597c5ba4; uid_tt_ss=5cef146a72998c8600488895597c5ba4; UIFID=3af258ad659545d9553f15cf32bb8a88df248991ebb865c20b5fa6f7dab6eb54e2e82e7822bd89e61cad006aeb4d52a2d8d65f685adfe7ada0b037c245f89d78d3fd92e37014810a2860fb4ee126bd64de6ef0e8376d69ee60e0cd305fea15a385b34f93b02d281c233651827430328d745bdfd074368fe212199d09c7895cc8f19f5356b46e76df0bdf6cfc7a41e62c7b6e697998441c4274"

# 请求头设置
headers = {
    'cookie': cookie,
    'user-agent': 'Mozilla/5.0'
}

# 点赞页面接口（假设为首页）
url = 'https://www.douyin.com/like'

# 保存视频的文件夹
save_dir = 'douyin_videos'
os.makedirs(save_dir, exist_ok=True)

# 发送请求
response = requests.get(url, headers=headers)

# 提取视频链接（简单示例）
video_urls = re.findall(r'playAddr":"(.*?)"', response.text)

# 清洗链接（转义字符替换）
video_urls = [url.replace('\\u002F', '/') for url in video_urls]

# 下载视频
for i, v_url in enumerate(video_urls):
    try:
        video = requests.get(v_url)
        file_path = os.path.join(save_dir, f'douyin_{i}.mp4')
        with open(file_path, 'wb') as f:
            f.write(video.content)
        print(f'下载成功：{file_path}')
    except:
        print(f'下载失败：{v_url}')