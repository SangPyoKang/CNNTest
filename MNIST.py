import tensorflow as tf
import PyQt5 as py
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import random

learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1



mnist=input_data.read_data_sets("MNIST_data/", one_hot=True)

# tensorflow graph input
X = tf.placeholder('float', [None, 784]) # mnist data image of shape 28 * 28 = 784
Y = tf.placeholder('float', [None, 10]) # 0-9 digits recognition = > 10 classes

# set model weights
W0 = tf.Variable(tf.zeros([784, 10]))
b0 = tf.Variable(tf.zeros([10]))
# layer1 = tf.sigmoid(tf.add(tf.matmul(X,W0),b0))

# W1 = tf.Variable(tf.zeros([10, 10]))
# b1 = tf.Variable(tf.zeros([10]))
# layer2 = tf.sigmoid(tf.add(tf.matmul(layer1,W1),b1))
#
# W2 = tf.Variable(tf.zeros([10, 10]))
b2 = tf.Variable(tf.zeros([10]))
# layer3 = tf.sigmoid(tf.add(tf.matmul(layer2,W2),b2))
#
#
# W3 = tf.Variable(tf.zeros([10, 10]))
# b3 = tf.Variable(tf.zeros([10]))
# layer4 = tf.add(tf.matmul(layer3,W3),b3)
# Our hypothesis
activation = tf.sigmoid(tf.add(tf.matmul(X, W0),b0) ) # Softmax

# Cost function: cross entropy
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=activation, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)  # Gradient Descen

# Before starting, initialize the variables. We will `run` this first.
init = tf.initialize_all_variables()

# Launch the graph,
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)


        # Fit the line.
        for step in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Fit training using batch data

            sess.run(optimizer, feed_dict={X: batch_xs, Y: batch_ys})

            # Compute average loss
            avg_cost += sess.run(cost, feed_dict={X: batch_xs, Y: batch_ys})/total_batch
        # Display logs per epoch step
        # if epoch % display_step == 0:
            # print ("Epoch:", '%04d' %(epoch+1), "cost=", "{:.9f}".format(avg_cost))

    # print("Optimization Finished!")
    # print(total_batch)

    # Test model
    correct_prediction = tf.equal(tf.argmax(activation, 1), tf.argmax(Y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print ("Accuracy:", accuracy.eval({X: mnist.test.images, Y: mnist.test.labels}))

    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label:", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
    print("Prediction:", sess.run(tf.argmax(activation, 1),
                                  feed_dict={X: mnist.test.images[r:r + 1]}))

    plt.imshow(mnist.test.images[r:r + 1].
               reshape(28, 28), cmap='Greys', interpolation='nearest')
    plt.show()




