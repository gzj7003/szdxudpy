import os
import requests

# 目标链接
SOURCE_URL = "https://gitee.com/lionzang/itv/raw/master/z.txt"

# 输出目录
OUTPUT_DIR = "txt_files"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "itv.m3u")

def fetch_source(url):
    """获取直播源内容"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def filter_sources(content):
    """过滤央视及卫视直播源"""
    filtered = []
    for line in content.splitlines():
        if "CCTV" in line or "卫视" in line:
            filtered.append(line)
    return "\n".join(filtered)

def save_playlist(content, output_file):
    """保存播放列表"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    # 获取并过滤直播源
    source_content = fetch_source(SOURCE_URL)
    filtered_content = filter_sources(source_content)

    # 保存播放列表
    save_playlist(filtered_content, OUTPUT_FILE)
    print(f"播放列表已保存到 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
