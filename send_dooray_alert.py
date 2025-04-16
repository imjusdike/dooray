import requests

WEBHOOK_URL = "https://parkingcloud.dooray.com/services/2256444361245483660/4047412744015864813/Y8Oo9blQTZiMJPUEgl_0TQ"  # 여기에 네 Webhook URL 넣기

payload = {
    "botName": "확도 알림 봇",
    "text": "📢 확도 현장 보고"
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    print("✅ 메시지 전송 성공")
else:
    print(f"❌ 전송 실패: {response.status_code}, {response.text}")
