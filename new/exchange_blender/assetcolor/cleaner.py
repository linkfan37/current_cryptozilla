import os, shutil
path = '/home/flo/projekt/new/exchange_blender/assetcolor/variation/'
colorlist= ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green"]
for color in  colorlist:
    folder = path + color
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))#cleans