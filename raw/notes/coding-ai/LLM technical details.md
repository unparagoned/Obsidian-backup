
# Attention

A word will have a query vector which asks stuff like what adjectives are before me
Words will have key vectors which say what they are like I'm an adjective

You take the dot product between the keys and query vectors. Giving you an attention pattern, so what words relate to others. 

Then you times the value matrix against previous word embeddings, so you then add the value vectors to the original vectors.

Use multi head, so you can do it in parallel, with lots of different ways and vectors. Having one massive matrix wouldn't be efficient, and you can't do it in parallel.

There are various layers, so in the first player hoodie just attends to red, but in layer 2 the updated hoodie attends to the updated red.

Position uses lots of sin waves, so it know if it's every two tokens or every token, etc.


# Reinforcement learning
Reinforcement learning, still uses back propagation but the signal is from trying different answers(from output distribution) and rewarding ones that's good.