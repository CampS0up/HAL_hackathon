from PIL import Image

def import_and_display_image(image_path):
    picture = Image.open(image_path)

    picture.show()

if __name__ == "__main__":
    picture_path = "HAL9000.png"
    
    import_and_display_image(picture_path)
