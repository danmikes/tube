import os
import subprocess
import tempfile

def burn_audio_cd(audio_data, device='/dev/scd0'):
  command = ['wodim', '-v', '-nofix', '-eject', 'dev={}'.format(device), '-audio', '-pad']

  try:
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.wav', delete=False) as temp_file:
      for audio in audio_data:
        temp_file.write(audio['data'])
        command.append(tempfile.name)
      result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
  except subprocess.CalledProcessError as e:
    print(f'Burning error: {e.stderr.decode()}')
  finally:
    tempfile.close()
    os.unlink(tempfile.name)
