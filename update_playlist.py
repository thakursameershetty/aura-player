import os
import json

# CONFIGURATION
VIDEO_FOLDER = 'videos'
OUTPUT_FILE = 'playlist.json'

def generate_playlist():
    playlist = []
    
    # Check if folder exists
    if not os.path.exists(VIDEO_FOLDER):
        print(f"Error: Folder '{VIDEO_FOLDER}' not found.")
        return

    # Scan files
    files = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(('.mp4', '.webm', '.mov'))]
    files.sort() # Sort alphabetically

    print(f"Found {len(files)} videos...")

    for filename in files:
        # AUTOMATIC METADATA GUESSER
        # It tries to turn "end_of_beginning.mp4" into "END OF BEGINNING"
        
        # Remove extension
        clean_name = os.path.splitext(filename)[0]
        
        # Replace underscores/dashes with spaces
        readable_name = clean_name.replace('_', ' ').replace('-', ' ')
        
        # Guess Artist (Simple Logic)
        artist = "UNKNOWN ARTIST"
        title = readable_name.upper()

        # You can add custom logic here if you name files like "The Weeknd - Starboy.mp4"
        if " - " in readable_name:
            parts = readable_name.split(" - ")
            artist = parts[0].upper()
            title = parts[1].upper()
        
        # Manual Overrides (Optional)
        if "WEEKND" in title or "STARBOY" in title: artist = "THE WEEKND"
        if "TAYLOR" in title or "OPHELIA" in title: artist = "TAYLOR SWIFT"
        if "DJO" in title or "BEGINNING" in title: artist = "DJO"

        # Create Entry
        entry = {
            "title": title,
            "artist": artist,
            "filename": filename
        }
        playlist.append(entry)

    # Write JSON file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(playlist, f, indent=4)
    
    print(f"Success! {OUTPUT_FILE} updated with {len(playlist)} tracks.")

if __name__ == "__main__":
    generate_playlist()