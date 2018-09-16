import subprocess

def convert2mp4(name_info):

    print("*************************************************************")
    print("*************************************************************")

    print("Final step: Convert processed pictures to video")

    print("*************************************************************")
    print("*************************************************************")

    picture_final_path = './' + name_info + '_final/pic_num_%d.jpg'
    video_final_name = './Video_for_' + name_info + '.mp4'

    ffmpeg_command = 'ffmpeg -framerate 0.25 -i ' + picture_final_path + ' ' + video_final_name
    subprocess.call(ffmpeg_command, shell=True)

    print(ffmpeg_command)