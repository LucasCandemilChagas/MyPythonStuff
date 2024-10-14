from PIL import Image
words = Image.open('word_matrix.png')
mask = Image.open('mask.png')
words.putalpha(128)
mask.putalpha(128)
new_mask = mask.resize((words.width, words.height))
words.paste(im=new_mask, box=(0,0), mask=new_mask)

words.show()