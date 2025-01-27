#don't forget to install pillow library by using ✔🐱‍🐉🐱‍🐉 "pip install pillow"🐱‍🐉🐱‍🐉 in terminal
#just replace Manish singh with your username
import os
import glob
from PIL import Image
def bing_spot_light_wp(outpath=r"C:\Users\Manish singh\OneDrive\Pictures\Wallpapers", size_in_kb=100):
#or you can use this path:outpath=r"Pictures" if you conflict username issue without any headache or just replace Manish singh with your username
    """
    Convert all files in the Assets directory to PNG format and save them in the specified output folder.
    
    :param outpath: Folder to write the output images to.
    :param size_in_kb: Minimum size of files to process (in KB).
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    
    # Path to the Assets folder
    assets_path = r"C:\Users\Manish singh\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    
    # Iterate over all files in the Assets directory
    for x in glob.glob(os.path.join(assets_path, "*")):
        # Check if the file is valid and meets the size requirement
        if os.path.isfile(x) and os.path.getsize(x) > size_in_kb * 1024:
            try:
                # Open the image file
                im = Image.open(x)
                # Prepare output filename with .png extension
                filename = os.path.splitext(os.path.basename(x))[0] + ".png"
                # Save the image as PNG in the output path
                im.save(os.path.join(outpath, filename), format="PNG")
                print(f"Converted and saved: {filename}")
            except Exception as e:
                print(f"Error processing {x}: {e}")

# Example usage
bing_spot_light_wp()
