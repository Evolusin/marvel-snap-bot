import cv2

def show_images(images_list, titles_list):
    for image, title in zip(images_list, titles_list):
        cv2.imshow(title, image)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        exit(0)
    return True