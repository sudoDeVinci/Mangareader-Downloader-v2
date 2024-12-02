import os
from PIL import Image
import shutil
from typing import Tuple, List

mangas = os.listdir("temp")

if not os.path.exists("downloads"):
    os.mkdir("downloads")

for manga in mangas:

    if not os.path.isdir(f"temp/{manga}"):
        print(f"Skipping {manga} since its not a directory")
        continue
    
    images = []

    print("processing manga: " + manga)

    imagefiles = os.listdir(f"temp/{manga}")

    imagelen = len(imagefiles)

    print("Done! Beggining to append to pdf...")

    for i in range(1, imagelen + 1):
        print("Opening image " + str(i))
        try:
            images.append(Image.open(f"temp/{manga}/{i}.png"))
        except:
            # apples fucking retarded DS_Store file
            continue


    pdf_path = f"downloads/{manga}.pdf"

    print("Saving to pdf    ")
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )

    shutil.rmtree(f"temp/{manga}")


# Configuration
INPUT_DIR = "temp"
OUTPUT_DIR = "downloads"
IMAGE_EXT = ".png"
 
def get_manga_dirs() -> Tuple[str, ...]:
    """
    Get list of manga directories.

    Returns:
        Tuple[str]: A tuple of manga directory strings.
    """
    return tuple(d for d in os.listdir(INPUT_DIR) 
            if os.path.isdir(os.path.join(INPUT_DIR, d)))


def get_image_files(manga_dir: str) -> List[str]:
    """
    Get a sorted list of image files in a manga directory.

    Args:
        manga_dir (str): The manga directory.
    
    Returns:
        Tuple[str, ...]: A tuple of image files.
    """

    try:
        files = tuple(f for f in os.listdir(os.path.join(INPUT_DIR, manga_dir))
                if f.endswith(IMAGE_EXT))
        return tuple(sorted(files, key=lambda x: int(os.path.splitext(x)[0])))
    except ValueError:
        print(f"Invalid image filenames in {manga_dir}")
        return tuple([])


def process_manga(manga_dir: str) -> None:
    """
    Process a manga directory.

    Args:
        manga_dir (str): The manga directory.
    """

    pass