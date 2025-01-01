import subprocess
from audio.audio_type import AudioType

def convert_audio(files_in, format_out=AudioType.WAV):
  if format_out not in [audio_type.value for audio_type in AudioType]:
    raise ValueError(f'Invalid target format: {format_out}')

  files_out = []
  for file_in in files_in:
    file_in_ext = file_in.split('.')[-1]
    if file_in.endswith(f'.{format}'):
      file_out = file_in.replace(f'.{file_in_ext}', f'.{format_out}')

      try:
        subprocess.run(['ffmpeg', '-i', file_in, file_out], check=True)
        files_out.append(file_out)
      except subprocess.CalledProcessError as e:
        print(f'Conversion failed {file_in} to {format_out}: {e}')

  return files_out
