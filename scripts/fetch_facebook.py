import json
import os
import urllib.request
import urllib.parse
from pathlib import Path

PAGE_ID = os.environ["FACEBOOK_PAGE_ID"]
TOKEN = os.environ["FACEBOOK_PAGE_ACCESS_TOKEN"]

API_VERSION = "v27.0"

url = (
    f"https://graph.facebook.com/{API_VERSION}/{PAGE_ID}/published_posts?"
    + urllib.parse.urlencode({
        "fields": "id,message,created_time,full_picture,permalink_url",
        "limit": 30,
        "access_token": TOKEN
    })
)

req = urllib.request.Request(
    url,
    headers={"User-Agent": "AnarMedia-News/1.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    result = json.loads(response.read().decode("utf-8"))

if "error" in result:
    raise RuntimeError(result["error"])

posts = []

for post in result.get("data", []):
    message = post.get("message", "").strip()

    if not message:
        continue

    lines = [x.strip() for x in message.splitlines() if x.strip()]

    posts.append({
        "id": post.get("id"),
        "title": lines[0][:120] if lines else "AnarMedia мэдээ",
        "description": message,
        "image": post.get("full_picture", ""),
        "date": post.get("created_time", ""),
        "url": post.get("permalink_url", "")
    })

output = Path("data/facebook-posts.json")
output.parent.mkdir(parents=True, exist_ok=True)

output.write_text(
    json.dumps(posts, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Successfully synced {len(posts)} Facebook posts.")
