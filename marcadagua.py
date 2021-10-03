import os
import sys

from PIL import Image

EXTS = ('.jpg', '.png')

if len(sys.argv) < 3:
    print('Usage: marcadagua.py \'pasta das imagens\' \'localização do logo (logo.png caso esteja na mesma pasta)\' [topoesquerda, topodireita, esquerdabaixo, direitabaixo, centro]')
    sys.exit()
elif len(sys.argv) == 4:
    path = sys.argv[1]
    lgo = sys.argv[2]
    pos = sys.argv[3]
else:
    path = sys.argv[1]
    lgo = sys.argv[2]

logo = Image.open(lgo)
logoWidth = logo.width
logoHeight = logo.height


for filename in os.listdir(path):
    if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != lgo:
        image = Image.open(path + '/' + filename)
        imageWidth = image.width
        imageHeight = image.height

        try:
            if pos == 'topoesquerda':
                image.paste(logo, (0, 0), logo)
            elif pos == 'topodireita':
                image.paste(logo, (imageWidth - logoWidth, 0), logo)
            elif pos == 'esquerdabaixo':
                image.paste(logo, (0, imageHeight - logoHeight), logo)
            elif pos == 'direitabaixo':
                image.paste(logo, (imageWidth - logoWidth, imageHeight - logoHeight), logo)
            elif pos == 'centro':
                image.paste(logo, (int((imageWidth - logoWidth)/2), int((imageHeight - logoHeight)/2)), logo)
            else:
                print('Error: ' + pos + ' is not a valid position')
                print('Usage: marcadagua.py \'pasta das imagens\' \'localização do logo (logo.png caso esteja na mesma pasta)\' [topoesquerda, topodireita, esquerdabaixo, direitabaixo, centro]')

            image.save(path + '/' + filename)
            print('Marca dagua adicionada em ' + path + '/' + filename)

        except:
            image.paste(logo, (int((imageWidth - logoWidth)/2), int((imageHeight - logoHeight)/2)), logo)
            image.save(path + '/' + filename)
            print('Marca dagua padrao adicionada em ' + path + '/' + filename)
