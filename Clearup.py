import os
def remove_img(path, img_name):
    os.remove(path + '/' + img_name)

    if os.path.exists(path + '/' + img_name) is False:
        
        return True
