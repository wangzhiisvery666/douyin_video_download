# Douyin Video URL Extractor

这是一个基于 FastAPI 的 Web 应用，用于从抖音短链接中提取视频的直接播放 URL。

## 功能

- 接受包含抖音短链接的文本输入
- 从短链接中提取视频 ID
- 获取视频的直接播放 URL

## 安装

1. 克隆此仓库：

   ```
   https://github.com/wangzhiisvery666/douyin_video_download.git
   cd douyin-video-extractor
   ```

2. 创建并激活虚拟环境（可选但推荐）：

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. 安装依赖：

   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 启动服务器：

   ```
   python webapp.py
   ```

   服务器将在 `http://0.0.0.0:8000` 上运行。

2. 发送 POST 请求到 `/get_video_url` 端点，请求体应包含 JSON 格式的 `text` 字段，其中包含抖音短链接。

   例如，使用 curl：

   ```
   curl -X POST "http://localhost:8000/get_video_url" -H "Content-Type: application/json" -d '{"text":"在这里粘贴包含抖音短链接的文本"}'
   ```

3. 服务器将返回一个 JSON 响应，包含视频的直接播放 URL。

## API 文档

启动服务器后，可以在 `http://localhost:8000/docs` 查看完整的 API 文档。

## 注意事项

- 本工具仅供学习和研究使用，请遵守抖音的使用条款和版权规定。
- 如遇到任何问题或有改进建议，欢迎提出 issue 或 pull request。