import base64
import requests
from pathlib import Path

def save_image_from_clipboard():
    try:
        from PIL import ImageGrab
        import io
        
        # Get image from clipboard
        img = ImageGrab.grabclipboard()
        
        if img:
            # Save the image
            img.save('profile.jpg', 'JPEG')
            print("✅ Image saved successfully as profile.jpg")
        else:
            print("❌ No image found in clipboard. Please copy an image first.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    save_image_from_clipboard()
