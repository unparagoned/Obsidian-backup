AE has deterministic latent space

VAE has a probabilistic latent space

AE has to change loss function to Adam and remove the regulariser

VAE had all sorts of issues since many functions aren't in the backend, then some are on tf and others are in keras ops, so had lots of issues with compatibilityy stuff. In the end the AI rewrote it in terms of a model object.

Cloud computing can provide resources for training deep neural network

Sparse penalizes activation of some neurons in hidden layers

Contractive, penalises gradient in hidden layers as well as reconstruction loss. Similar inputs should have similar encodings and similar latent space.

Denoising autoencoder. Compares ground truth to output, not noisy input. Loss is normally L1/L2.

Variational autoencoder. Latent attributes are expressed as probability distributions. Can generate new data.

Sparse has larger latent dimension than input dimension.

Can learn more features.

Undercomplete - dimensionality reduction

Sparse - Feature learning for vision.

Sparse has a penalisation term, which stops too many neurons firing at one.

Too many active neurons - penalty increases

There are two APIs in Keras, Sequential and functional

Sequential - Use add layers, but can't share layers or branch layers.

Functional - More flexible and powerful, can have branching and sharing of layers

Autoencoder Questions

1. What is the point of an autoencoder?

Get’s at the key features, in a feature space.

Explain how an autoencoder and  a decoder work together in general?

Encoder reduces dimensions, decoder recreates object from latent space

1. What is a latent space?

This is the middle hidden layer which has the features encoded.

1. Why is the auto-encoder said to be “self-supervised”?

The output is compared to the input.

1. In the “Monkeys” code, images are loaded via the following code.

Explain what is happening in each line.

import os

all_monkeys =[]

train_dir = '/content/drive/MyDrive/training/'

subdir=('n0','n1','n2','n3','n4','n5','n6','n7','n8','n9')

for sub in subdir:

  dir = train_dir + sub +'/'

  print("looking in " + dir)

  for image in os.listdir(dir):

    try:

      monkey = tf.keras.utils.load_img ((dir+ image),

                             target_size = (64,64))

      all_monkeys.append(monkey)

    except Exception as e:

      pass

print ('Recovered data format:', type(all_monkeys))

print('Number of monkey images:', len(all_monkeys))

1. When we first prepare the data  for processing, we use the following code

#Make the array

all_monkeys = np.asarray(all_monkeys)

np.asarray(all_monkeys)

print('Shape of array:', all_monkeys.shape)

#Normalise pixel values

all_monkeys = all_monkeys.astype('float32') / 255

#Flatten array

all_monkeys = all_monkeys.reshape((len(all_monkeys),

                                   np.prod(all_monkeys.shape[1:])))

print('Shape after flattened:', all_monkeys.shape)

What shape is the data when first read in and why?  What does each dimension mean?

What is the shape after flattening and why do we flatten the data?

1.  When building the model we use the following code:

#Input layer placeholder

input_layer = Input(shape=(input_dim,))

#Encoding layers funnel the images into lower dimensional representations

encoded = Dense(encoding_dim*4, activation='relu')(input_layer)

encoded = Dense(encoding_dim*2, activation='relu')(encoded)

#Latent space

encoded = Dense(encoding_dim, activation = 'relu')(encoded)

# 'decoded' is the lossy reconstruction of the input

decoded = Dense(encoding_dim*2, activation='relu')(encoded)

decoded = Dense(encoding_dim*4, activation='relu')(decoded)

decoded = Dense(input_dim, activation='sigmoid')(decoded)

#this model maps an input to its reconstruction

autoencoder = Model(input_layer, decoded)

autoencoder.summary()

The above shows use of the functional API for Keras.

What are the differences between the sequential and functional APIs?

Challenge

Overview answers only expected.

1. What is a GAN and how does it relate to autoencoders and decoders?

2. How are autoencoders and decoders used in natural language processing?

Create word embeddings, that capture meaning. Encoder to process input, decoder to create output text.

1. When were autoencoders first introduced.  Find a seminal paper.

Rumelhart, Hinton & Williams (1986) – “Learning representations by back-propagating errors.”

From <[https://d.docs.live.net/37cecb0168167465/Documents/Learning/L7%20AI/Machine%20Learning%20Using%20Cloud%20Computing/Workshops/Workshop%206/6.3%20Autoencoder%20Questions.docx](https://d.docs.live.net/37cecb0168167465/Documents/Learning/L7%20AI/Machine%20Learning%20Using%20Cloud%20Computing/Workshops/Workshop%206/6.3%20Autoencoder%20Questions.docx)>

14 October is when next term starts

22 September assignment