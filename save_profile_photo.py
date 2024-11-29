from PIL import Image
import sys
import os

def save_profile_photo(input_path):
    try:
        # Open and resize the image
        img = Image.open(input_path)
        
        # Convert to RGB if needed
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
            
        # Calculate dimensions to maintain aspect ratio
        target_size = (400, 400)
        img.thumbnail(target_size, Image.Resampling.LANCZOS)
        
        # Save the image
        output_path = os.path.join(os.path.dirname(__file__), 'profile.jpg')
        img.save(output_path, 'JPEG', quality=95)
        print(f"✓ Profile photo saved successfully to: {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python save_profile_photo.py <path_to_your_photo>")
    else:
        save_profile_photo(sys.argv[1])
