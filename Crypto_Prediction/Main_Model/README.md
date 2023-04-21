# Main Model

### First Model: LSTM

The LSTM model is seen as an improved version of the RNN model. RNN cannot cope with two far apart attributes because of its single register, and this problem is called long-term dependence. LSTM, as its name suggests, has long and short term memory capacity and can solve this problem.

![image-20230410235659766](https://images.wu.engineer/images/2023/04/10/image-20230410235659766.png)



### Second Model: WGAN-GP

Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP) is an advanced variant of Generative Adversarial Networks (GANs), a class of machine learning models that consist of a generator and a discriminator, designed to generate realistic data samples. WGAN-GP specifically improves upon the original GAN framework by addressing some of its limitations, such as mode collapse and training instability.

For this algorithm, there are few [research papers] showed that it has higher accuracy than LSTM and basic GAN with all combined with the sentimental analysis data. However, this algorithm is a novel algorithm which is first stated at 2017. Hence, I can found less tutorial or model about this algorithm. I will try to implement a model if there is enough time.

1. Generator (G): The generator is a neural network that takes random noise as input and generates synthetic data samples. Its goal is to produce samples that are indistinguishable from real data.
2. Discriminator (D): The discriminator is another neural network that takes both real and generated data samples as input and tries to distinguish between them. Its goal is to correctly classify samples as real or generated.
3. Real Data: This represents the actual data samples from the dataset you are trying to model or mimic.
4. Generated Data: These are the data samples produced by the generator.
5. Gradient Penalty: This is the additional term in the loss function that enforces the Lipschitz continuity of the discriminator's gradients. It is calculated by taking the gradient of the discriminator's output with respect to its input and penalizing deviations from a specified norm.

- Generator receives random noise as input and produces generated data samples.
- Discriminator receives both real and generated data samples as input and attempts to classify them.
- Gradient penalty is computed based on the gradients of the discriminator with respect to its input.
- The loss function for the discriminator includes the Wasserstein distance and the gradient penalty term.
- The generator and discriminator are trained alternately, updating their weights to minimize their respective loss functions.

The generator tries to improve its ability to generate realistic samples, while the discriminator tries to improve its ability to distinguish between real and generated samples. The gradient penalty helps ensure the stability of the training process and improves the quality of the generated samples.

[research papers]: https://doi.org/10.3844/jcssp.2021.188.196	"Lin, H., Chen, C., Huang, G., &amp; Jafari, A. (2021). Stock price prediction using Generative Adversarial Networks. Journal of Computer Science, 17(3), 188–196"
