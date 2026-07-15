from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent
import json

# Nama Akun
client = TikTokLiveClient(unique_id="@anomali.384")

# Kata yang harus ditebak
target_kata = "kimia" 

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print("Berhasil terhubung ke Live!")

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    user = event.user.unique_id
    komentar = event.comment.strip().lower()
    
    # 1. Update tampilan dengan komentar terbaru
    with open('game_state.json', 'w') as f:
        json.dump({"latest_comment": komentar, "status": "playing"}, f)
    
    print(f"{user} berkata: {komentar}")
    
    # 2. Cek jawaban
    if komentar == target_kata:
        print(f"--- {user} MENJAWAB DENGAN BENAR! ---")
        with open('game_state.json', 'w') as f:
            json.dump({"status": "correct", "user": user, "word": target_kata}, f)

if __name__ == '__main__':
    client.run()
