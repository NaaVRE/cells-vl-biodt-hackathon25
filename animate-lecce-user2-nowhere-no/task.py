from PIL import Image
import shutil
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output_gif_path', action='store', type=str, required=True, dest='output_gif_path')


args = arg_parser.parse_args()
print(args)

id = args.id

output_gif_path = args.output_gif_path.replace('"','')


conf_data_path = conf_data_path = '/tmp/data/'

img = Image.open(output_gif_path)

frames = []
try:
    while True:
        frames.append(img.copy())
        img.seek(img.tell() + 1)
except EOFError:
    pass

frames[0].save('animated.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
output_gif = 'animated.gif'
output_animated_path = os.path.join(conf_data_path, output_gif)
shutil.copy('animated.gif', output_animated_path)

file_output_gif = open("/tmp/output_gif_" + id + ".json", "w")
file_output_gif.write(json.dumps(output_gif))
file_output_gif.close()
