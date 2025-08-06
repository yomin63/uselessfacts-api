import requests
from datetime import datetime

API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_useless_fact():
    resp = requests.get(API_URL, timeout=10)
    if resp.status_code != 200:
        return "😅 오늘의 쓸모없는 지식을 가져오지 못했습니다."
    data = resp.json()
    return data.get("text", "데이터 없음")

def update_readme(fact):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 🪄 오늘의 쓸모없는 지식\n\n")
        f.write(f"💡 **{fact}**\n\n")
        f.write(f"---\n")
        f.write(f"⏳ 마지막 업데이트: {now}\n")
        f.write("\nPowered by [Useless Facts API](https://uselessfacts.jsph.pl/) · 자동화 봇")

if __name__ == "__main__":
    fact = get_useless_fact()
    update_readme(fact)
