# import datetime.datetime
import os, sys, datetime
import cv2
import ktb

from enum import Enum
class ImageType(Enum):
    depth = 1
    ir = 2
    rgb = 3

def main():
    
    today = datetime.date.today().isoformat()
    BASE_PATH = "/home/ewertonsjp/Documents/doutorado/coleta_ricardo/{}".format(today)
    
    if len(sys.argv) == 1:
        print("ERRO: Um parâmetro com o código do Animal deve ser Infomado!")

    else:
        animal = sys.argv[1]

        os.makedirs('{}/{}/imagens_depth'.format(BASE_PATH, animal))
        os.makedirs('{}/{}/imagens_ir'.format(BASE_PATH, animal))
        os.makedirs('{}/{}/imagens_rgb'.format(BASE_PATH, animal))

        k = ktb.Kinect()
        i = 0

        while True:

            # counter
            i += 1
            
            # Specify as many types as you want here
            color_frame = k.get_frame(ktb.RAW_COLOR)
            depth_frame = k.get_frame(ktb.RAW_DEPTH)
            ir_frame = k.get_frame(ktb.IR)

            # k.record('temp.avi', ktb.COLOR)    
            cv2.imshow('c_frame', color_frame)
            cv2.imshow('d_frame', depth_frame)
            cv2.imshow('i_frame', ir_frame)

            cv2.imwrite('{}/{}/imagens_depth/{}.png'.format(BASE_PATH, animal, str(i)), depth_frame)
            cv2.imwrite('{}/{}/imagens_ir/{}.png'.format(BASE_PATH, animal, str(i)), ir_frame)
            cv2.imwrite('{}/{}/imagens_rgb/{}.png'.format(BASE_PATH, animal, str(i)), color_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def make_dirs(base_path, animal):
    for image_type in list(ImageType):
        mkdir(base_path, animal, image_type.name)

def mkdir(base_path, animal, name):
    os.makedirs('{}/{}/{}'.format(base_path, animal, name))


if __name__ == "__main__":
    main()