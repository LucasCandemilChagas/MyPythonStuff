from PIL import Image

logo = Image.open('a.png')

anita = Image.open('AnitaanitaB.jpg')

print(type(logo))

logo.show()

print(f'Tamanho da imagem: {logo.size}')

w = logo.width/3
h = logo.height/3

logo.crop((0,0,w,h)).show()

logo.putalpha(128)

anita.putalpha(128)

logo.show()

logo.paste(im=anita, box=(0,0),mask=anita)

logo.show()
