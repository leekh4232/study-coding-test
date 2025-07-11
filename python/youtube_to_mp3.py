import subprocess

def download_mp3(url, output_dir='downloads'):
    command = [
        'yt-dlp',
        '-x',                         # extract audio
        '--audio-format', 'mp3',      # convert to mp3
        '--audio-quality', '0',       # best quality (0=best, 9=worst)
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]

    subprocess.run(command, check=True)
    print("다운로드 및 변환 완료!")

def download_webm(url, output_dir='downloads'):
    command = [
        'yt-dlp',
        '-f', 'bestaudio[ext=webm]',  # ✅ webm 확장자를 가진 최고 오디오 선택
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]

    subprocess.run(command, check=True)
    print("WebM 오디오 다운로드 완료!")

def download_flac(url, output_dir='downloads'):
    command = [
        'yt-dlp',
        '-x',                         # extract audio
        '--audio-format', 'flac',      # convert to mp3
        '--audio-quality', '0',       # best quality (0=best, 9=worst)
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]

    subprocess.run(command, check=True)
    print("다운로드 및 변환 완료!")

def download_opus(url, output_dir='downloads'):
    command = [
        'yt-dlp',
        '-x',                         # extract audio
        '--audio-format', 'opus',      # convert to opus
        '--audio-quality', '0',       # best quality (0=best, 9=worst)
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]

    subprocess.run(command, check=True)
    print("다운로드 및 변환 완료!")

def download_best_video(url, output_dir='downloads'):
    command = [
        'yt-dlp',
        '-f', 'bestvideo+bestaudio',     # ✅ 최고 화질 + 최고 음질
        '--merge-output-format', 'mp4',  # ✅ mp4로 자동 병합 (ffmpeg 필요)
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]
    subprocess.run(command, check=True)
    print("영상 다운로드 완료 (최고 화질 + 음질)!")

def download_best_audio(url, output_dir='downloads'):
    command = [
        'yt-dlp',
        '-f', 'bestaudio',  # ✅ opus 확장자를 가진 최고 오디오 선택
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]

    subprocess.run(command, check=True)
    print("✅ 오디오 다운로드 완료!")

# 예제 사용
if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=rboiHxBqdZk"
    download_opus(url)
    #download_best_video(url)