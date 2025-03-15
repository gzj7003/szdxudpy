import requests

# 原始直播源地址
SOURCE_URL = "https://raw.githubusercontent.com/gzj7003/kds/refs/heads/main/IPTV2.m3u"

# 自定义直播源
CUSTOM_SOURCES = """
#EXTINF:-1 tvg-id="16" tvg-name="苏州新闻综合" tvg-logo="http://www.csztv.cn/images/ds_off_01.png" group-title="苏州地方台",苏州新闻综合
https://live-auth.51kandianshi.com/szgd/csztv1.m3u8
rtmp://csztv.2500sz.com/live/c01
#EXTINF:-1 tvg-id="17" tvg-name="苏州社会经济" tvg-logo="http://www.csztv.cn/images/ds_off_02.png" group-title="苏州地方台",苏州社会经济
https://live-auth.51kandianshi.com/szgd/csztv2.m3u8
rtmp://csztv.2500sz.com/live/c02
#EXTINF:-1 tvg-id="18" tvg-name="苏州文化生活" tvg-logo="http://www.csztv.cn/images/ds_off_03.png" group-title="苏州地方台",苏州文化生活
https://live-auth.51kandianshi.com/szgd/csztv3.m3u8
rtmp://csztv.2500sz.com/live/c03
#EXTINF:-1 tvg-id="19" tvg-name="苏州生活资讯" tvg-logo="http://www.csztv.cn/images/ds_off_05.png" group-title="苏州地方台",苏州生活资讯
https://live-auth.51kandianshi.com/szgd/csztv5.m3u8
http://49.64.171.51:8887/rtp/239.49.8.116:8000
"""

def fetch_source(url):
    """获取远程直播源"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def filter_sources(content):
    """过滤央视1-15套及卫视直播源"""
    filtered = []
    for line in content.splitlines():
        if "#EXTINF" in line or "CCTV" in line or "卫视" in line:
            filtered.append(line)
    return "\n".join(filtered)

def save_playlist(content):
    """保存合并后的播放列表"""
    with open("mytvlist.m3u", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    # 获取并过滤原始直播源
    source_content = fetch_source(SOURCE_URL)
    filtered_content = filter_sources(source_content)

    # 合并自定义直播源
    final_content = filtered_content + "\n" + CUSTOM_SOURCES

    # 保存最终播放列表
    save_playlist(final_content)

if __name__ == "__main__":
    main()

try:
    with open("mytvlist.m3u", "w", encoding="utf-8") as f:
        f.write(content)
except IOError as e:
    print(f"保存文件失败: {e}")
