import re
import time
import requests
from bs4 import BeautifulSoup

from utils import jsonUtil

CHINA_MEMORY_PROJECT_PATH = "../china_memory_project"
BASE_URL = "http://memory.nlc.cn"
LIST_URL = BASE_URL + "/resource/index?type=video&sort=asc&sortType=none&page={}"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}


def get_video_list(page_num):
    url = LIST_URL.format(page_num)
    print(f"开始爬取第{page_num + 1}页")

    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"请求失败：{response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    pins = soup.select("div.pin")
    video_list = []
    for pin in pins:
        a_tag = pin.select_one("a.stretched-link")
        desc_tag = pin.select_one("p.description")
        if a_tag and desc_tag:
            href = BASE_URL + a_tag["href"]
            description = desc_tag.get_text(strip=True)
            video_list.append({"url": href, "description": description})
    return video_list


def print_video_subtitles(video_url):
    response = requests.get(video_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"请求失败：{response.status_code}")

    print(response.text)


def contains_english(text):
    return re.search(r'[a-zA-Z]', text) is not None


def get_video_subtitles_1(video_url):
    response = requests.get(video_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"请求失败：{response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    subtitle_elements = soup.find_all('p', class_='video-text-item')
    subtitles = []
    for subtitle_element in subtitle_elements:
        text = subtitle_element.get_text(strip=True)
        if not contains_english(text):  # 只保留没有英文的
            subtitles.append(text)

    return subtitles


def get_video_subtitles_2(video_url):
    # response = requests.get(video_url, headers=HEADERS)
    time.sleep(0.1)


if __name__ == '__main__':
    data = []

    for page in range(12):
        videos = get_video_list(page)
        time.sleep(1)  # 加个延时，避免频繁请求被封
        for video in videos:
            # print(f"{video['description']} - {video['url']}")
            context = get_video_subtitles_1(video["url"])
            if len(context) == 0:
                get_video_subtitles_2(video["url"])
                continue

            json_object = {"name": video["description"], "context": context}
            jsonUtil.write_json_file(f"{CHINA_MEMORY_PROJECT_PATH}/{video['description']}.json", json_object)
            data.append(json_object)
            print(f"视频{video['description']}录入完毕")
            time.sleep(1)
    jsonUtil.write_json_file(f"{CHINA_MEMORY_PROJECT_PATH}/data.json", data)

    # 测试
    # print_video_subtitles("http://memory.nlc.cn/video/167")
    # print(get_video_subtitles_1("http://memory.nlc.cn/video/167"))
