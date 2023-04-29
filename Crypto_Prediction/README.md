# Cryptocurrency Prediction
Tong Wu

## TODO

#### Main Model

- [x] Determine the main model to predict the price (Before 2023.04.13)

- [ ] Second (Supplementary) model (pending)

#### Implementation

*Awaiting for the data structure of sentimental analysis*

- [x] Fetch BTC data

- [ ] Fetch tweet data (pending)

- [x] Data cleaning

- [x] Model implementing

- [ ] Fine tuning

#### Fusion

Discover fusion between different machine learning algorithms
Fusion is completed, by adding dropout layers and GRU layers into LSTM model, in order to avoid overfitting and improve the accuracy.

#### Combine

Predict the price using ML model combined with the sentimental analysis data of tweet
Combine is almost completed. The function adding sentimental analysis data into the model has been writtem but not test yet.

#### Optimization

Optimism the running time and accuracy
Optimisation is ongoing, the parameters are tuned.

## Main model

### First Model: LSTM

The LSTM model is seen as an improved version of the RNN model. RNN cannot cope with two far apart attributes because of its single register, and this problem is called long-term dependence. LSTM, as its name suggests, has long and short term memory capacity and can solve this problem.

![image-20230410235659766](https://images.wu.engineer/images/2023/04/10/image-20230410235659766.png)



### Second Model: WGAN-GP

Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP) is an advanced variant of Generative Adversarial Networks (GANs), a class of machine learning models that consist of a generator and a discriminator, designed to generate realistic data samples. WGAN-GP specifically improves upon the original GAN framework by addressing some of its limitations, such as mode collapse and training instability.

For this algorithm, there are few [research papers] showed that it has higher accuracy than LSTM and basic GAN with all combined with the sentimental analysis data. However, this algorithm is a novel algorithm which is first stated at 2017. Hence, I can found less tutorial or model about this algorithm. I will try to implement a model if there is enough time.

[research papers]: https://doi.org/10.3844/jcssp.2021.188.196	"Lin, H., Chen, C., Huang, G., &amp; Jafari, A. (2021). Stock price prediction using Generative Adversarial Networks. Journal of Computer Science, 17(3), 188–196"

## Implementation

Completed (pending)

## Fusion of ML algorithms

TBD, may discard due to lack of time.

## Combine With Sentimental Analysis Data

TBD, implemented with sample data, awaiting the sentimental analysis

## Optimization

TBD

## Interfacing with front-end

TBD
Output format: images for tomorrow, 3 days after, 5 days after prediction. Predicted price array for each day.
