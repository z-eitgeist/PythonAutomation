import os
import shutil
from datetime import datetime, timedelta

downloads = os.path.join(os.path.expanduser("~\Downloads"))

old_downloads = os.path.join(os.path.expanduser("~\Downloads"), "old_downloads")

# If there is no folder called old_files, make one
if not os.path.exists(old_downloads):
    os.makedirs(old_downloads)

# get the list od all files in the Downloads folder
files = os.listdir(downloads)

# Get the today's date
today = datetime.now()

# Loop throught the files to see which ones are older then 30 days
for file in files: 
    file_path = os.path.join(downloads, file)
    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    time_difference = today - modified_time
    # Move all files older then 30 days to old_downloads folder
    if time_difference > timedelta(days=30):
        shutil.move(file_path, old_downloads)
