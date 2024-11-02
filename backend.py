# python -m uvicorn backend:app --reload
import os
import yt_dlp
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this as needed for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set the current directory
cur_dir = os.getcwd()

@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",  # Selects the best quality available
        "outtmpl": os.path.join(cur_dir, f"Video{link[-11:]}.mp4")  # Save video as VideoXXXXXX.mp4 in the current directory
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download started"}




