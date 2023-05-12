# Video to Audio Converter

This is a Python script for converting video files to MP3 files. The application uses FFmpeg for conversion.

## Features

- Converts any number of video files from an 'input' folder into mp3 files.
- Outputs the mp3 files into an 'output' folder with .mp3 extension.
- Option to limit the size of the output mp3 files.
- If the file size limit is specified and the converted file exceeds this limit, the application will automatically reduce the bitrate to bring it under the limit.

## Requirements

- Python >=3.11
- FFmpeg

## Usage

1. Place your video files into the 'input' directory.
2. Run the script:

    ```bash
    python3 app.py
    ```

    This will convert the video files to mp3 files at the best possible quality.
    If you want to limit the size of the output mp3 files, you can specify the --max-N argument when running the script, where N is the maximum size in MB. For example:
3. The converted mp3 files will be available in the 'output' directory.

## Notes

- This application assumes that FFmpeg is installed and in your system's PATH.
- Compressing audio to a lower bitrate will result in loss of quality. Use the file size limit option judiciously.

## License

This project is open source and available under the MIT License.
