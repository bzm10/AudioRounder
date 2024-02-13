import os
import subprocess
from pydub import AudioSegment

# Define constants
AUDIO_EXTENSIONS = ['.mp3', '.wav']
MODIFIED_FOLDER = 'modified'
ORIGINAL_FOLDER = 'original'

# Define file paths
current_directory = os.getcwd()
temp_directory = os.path.join(current_directory, 'temp')
modified_directory = os.path.join(current_directory, MODIFIED_FOLDER)
original_directory = os.path.join(current_directory, ORIGINAL_FOLDER)

# List all the files in the current directory
try:
    # List all the files in the current directory
    files = os.listdir(current_directory)
except OSError as e:
    # Print error message
    print(f'Error occurred while listing files: {e}')
    exit(1)

# Create the modified and original folders if they don't exist
try:
    # Create the modified and original folders if they don't exist
    if not os.path.exists(modified_directory):
        os.makedirs(modified_directory)
    if not os.path.exists(original_directory):
        os.makedirs(original_directory)
except OSError as e:
    # Print error message
    print(f'Error occurred while creating folders: {e}')
    exit(1)

# Process each file in the current directory
for file_name in files:
    # Define file paths
    file_path = os.path.join(current_directory, file_name)
    modified_file_path = os.path.join(modified_directory, file_name)
    original_file_path = os.path.join(original_directory, file_name)

    # Check if the file is an audio file 
    if any(file_name.endswith(ext) for ext in AUDIO_EXTENSIONS):
        # Check if the file has already been modified
        if not os.path.exists(modified_file_path):
            # try to process the file and round it to the nearest minute
            try:
                # Load the audio file to get the duration of the audio to calculate the speed factor
                audio = AudioSegment.from_file(file_path)

                # Calculate the speed factor
                duration = len(audio) / 1000
                rounded_duration = round(duration / 60) * 60
                speed_factor = duration / rounded_duration

                # Print logs
                print(f'Original audio duration: {duration} seconds')
                print(f'Rounded audio duration: {rounded_duration} seconds')
                print(f'Speed factor: {speed_factor}')
                print(f'Rounding {file_name} to the nearest minute...\n')

                # Run the ffmpeg command to round the audio to the nearest minute using the speed factor and save the modified file to the modified folder
                subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'panic', '-i', file_path, '-filter:a', f'atempo={speed_factor}', '-vn', modified_file_path])

                # Print success message
                print('Audio successfully rounded to the nearest minute!')

                # Move the original file to the original folder
                os.rename(file_path, original_file_path)
            except Exception as e:
                # Print error message
                print(f'Error occurred while processing file {file_name}: {e}')
        else:
            # Print message if the file has already been modified
            print(f'Skipping file {file_name} as a modified version already exists.\n')
