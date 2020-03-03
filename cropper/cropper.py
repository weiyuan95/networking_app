from PIL import Image
import os

def crop():
    # change the sub picture sizes here
    # measurement in pixels
    SUBPIC_HEIGHT = 50
    SUBPIC_WIDTH = 50
    image_to_crop = "img_2.jpg"

    image = Image.open("img_2.jpg")

    if image_to_crop == "img_2.jpg":
        image = image.crop((0, 0, 3600, 3600))

    image_width, image_height = image.size
    print(image_width, image_height, "\n")
    pic_no = 1

    for height_coord in range(0, image_height, SUBPIC_HEIGHT):
        for width_coord in range(0, image_width, SUBPIC_WIDTH):
            # the first 100 x 100 box starts from (0, 0, 100, 100)
            subpic_coordinates = height_coord, width_coord, height_coord+SUBPIC_HEIGHT, width_coord+SUBPIC_WIDTH
            subpic = image.crop(subpic_coordinates)

            # pic_1 will be top left 100px box, pic_2 will be the next 100px box below, etc
            # every 15 picture "boxes" is a new column
            file_name = f"../static/cropped_images/subpic_{pic_no}.png"

            subpic.save(file_name)
            pic_no += 1

if __name__ == "__main__":
    crop()