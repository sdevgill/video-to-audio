import os
import subprocess
import sys

# Constants
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
MAX_SIZE_MB = None
MB_TO_BYTES = 1_000_000  # 1 MB is 1,000,000 bytes

# Ensure the output directory exists
os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Check for max size argument
if len(sys.argv) > 1 and sys.argv[1].startswith("--max-"):
    try:
        MAX_SIZE_MB = int(sys.argv[1].split("--max-")[1])
    except ValueError:
        print(
            "Invalid max size argument, please use --max-N where N is the maximum size in MB"
        )
        sys.exit(1)

# Scan the input directory
for filename in os.listdir(INPUT_FOLDER):
    # Check if the file is a video file
    file_path = os.path.join(INPUT_FOLDER, filename)
    if os.path.isfile(file_path):
        output_file_path = os.path.join(
            OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}.mp3"
        )

        # Convert video to mp3
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                file_path,
                "-vn",
                "-acodec",
                "libmp3lame",
                "-q:a",
                "0",
                output_file_path,
            ]
        )

        # Check file size if max size is specified
        if MAX_SIZE_MB is not None:
            file_size = os.path.getsize(output_file_path)
            if file_size > MAX_SIZE_MB * MB_TO_BYTES:
                # Calculate new bitrate (assuming current file is at 192k bitrate)
                new_bitrate = int((MAX_SIZE_MB * MB_TO_BYTES * 192) / file_size)

                # Recompress file with lower bitrate
                temp_file_path = f"{output_file_path}.temp"
                os.rename(output_file_path, temp_file_path)
                subprocess.run(
                    [
                        "ffmpeg",
                        "-i",
                        temp_file_path,
                        "-vn",
                        "-acodec",
                        "libmp3lame",
                        "-b:a",
                        f"{new_bitrate}k",
                        output_file_path,
                    ]
                )
                os.remove(temp_file_path)
