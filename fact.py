import requests
import json
from datetime import datetime

# API URL
url = "https://uselessfacts.jsph.pl/random.json?language=en"

try:
    # API 호출
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    fact_data = response.json()

    # 저장 파일 이름 (고정)
    output_file = "useless_fact.json"

    # JSON 저장
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(fact_data, f, indent=4, ensure_ascii=False)

    print(f"[{datetime.now()}] Today's useless fact saved to {output_file}")

except requests.RequestException as e:
    print(f"Error fetching useless fact: {e}")
