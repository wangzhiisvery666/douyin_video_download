from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import re
import json
import uvicorn

app = FastAPI()


class InputText(BaseModel):
    text: str


def get_video_id(short_url):
    response = requests.get(short_url, allow_redirects=True)
    final_url = response.url
    match = re.search(r'video/(\d+)', final_url)
    return match.group(1) if match else None


def get_video_info(video_id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'referer': 'https://www.douyin.com/?is_from_mobile_home=1&recommend=1'
    }
    url = f'https://www.iesdouyin.com/share/video/{video_id}/'
    res = requests.get(url, headers=headers).text
    try:
        data = re.findall(r'_ROUTER_DATA\s*=\s*(\{.*?\});', res)[0]
        json_data = json.loads(data)
        item_list = json_data['loaderData']['video_(id)/page']['videoInfoRes']['item_list'][0]
        video = item_list['video']['play_addr']['uri']
        video_url = f'https://www.douyin.com/aweme/v1/play/?video_id={video}' if 'mp3' not in video else video
        return video_url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取视频信息失败: {str(e)}")


@app.post("/get_video_url")
async def get_video_url(input_data: InputText):
    match = re.search(r'https://v.douyin.com/(\S+)', input_data.text)
    if not match:
        raise HTTPException(status_code=400, detail="未找到有效的抖音短链接")

    short_url = match.group(0)
    video_id = get_video_id(short_url)
    if not video_id:
        raise HTTPException(status_code=400, detail="无法提取视频ID")

    video_url = get_video_info(video_id)
    return {"video_url": video_url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
