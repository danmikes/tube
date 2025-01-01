import io
import yt_dlp
from conf import FORMAT_OUT

def fetch_videos(videos_url):
  ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': FORMAT_OUT.value,
    'noplaylist': True,
    'verbose': True,
  }

  audio_data = []

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      def custom_hook(d):
        if d['status'] == 'finished':
          audio_data.append({
            'filename': d['filename'],
            'data': d['data']
          })

      ydl.add_progress_hook(custom_hook)
      ydl.download(videos_url)

    return audio_data
  except Exception as e:
    print(f'Download failed: {e}')
    return []
