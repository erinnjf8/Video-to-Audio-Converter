import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()
    video.close()

def main():
    print("MP4 to MP3 Converter")
    
    # Input video (MP4)
    input_file = input("Enter the path to the input MP4 file: ")
    
    if not os.path.exists(input_file):
        print("Error: Input file does not exist.")
        return
    
    if not input_file.lower().endswith('.mp4'):
        print("Error: Input file is not an MP4 file.")
        return
    
    # Check if conversion is needed
    output_file = os.path.splitext(input_file)[0] + '.mp3'
    if os.path.exists(output_file):
        overwrite = input("Output MP3 file already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Conversion cancelled.")
            return
    
    # Convert MP4 to MP3
    try:
        convert_mp4_to_mp3(input_file, output_file)
        print(f"Conversion successful. Output saved as: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    main()
