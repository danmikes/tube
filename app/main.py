import os
from audio.burn import burn_audio_cd
from audio.convert import convert_audio
from audio.fetch import fetch_videos
from video.list import videos_id
from conf import BASE_URL

def main():
  videos_url = [BASE_URL + video_id for video_id in videos_id]
  audio_data = fetch_videos(videos_url)
  if audio_data:
    burn_audio_cd(audio_data)
  else:
    print('No audio data to burn')

if __name__ == '__main__':
  main()
