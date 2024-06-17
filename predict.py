from tensorflow import keras as tf

model = tf.models.load_model('/vgg_model.h5')
from load_image import image
img = image('/test/non_autistic/003.jpg')

res = model.predict(img).argmax()

if res == 1:
	print('Autistic')
elif res == 0:
	print('Negative')
