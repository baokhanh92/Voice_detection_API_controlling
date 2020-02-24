## [ 1. OVERVIEW ]()
[ **1.1 About the data**: ]() 

**- Google speech command:** the data is 1s in length, and with only one words command. 

**- My own voice:** I recorded my own voices and add to the dataset


[ **1.2 What you can expect in this github**: ]() 
**1. Folder my model:**
1. .ipynb file to process data and the results of each models. 
2. .py connect the train models to control the volume in the computer.

**2. Google API:**
1. .py file to test out controling volume with Google API.
---
## [ 2. THE RESULT ](/9lRMLcbMR--joBvR84z5KA)

**1. Models: I tried out 4 type of models:**
- Melspectrogram + LSTM
- LSTM
- Shallow Neuron Network
- CNN

**2. The results:**

**1. CNN model**
![](https://i.imgur.com/GuTyxHm.png)

**2. Shallow neuron network**
![](https://i.imgur.com/tKuSKEu.png)

**3. Simple LSTM**
![](https://i.imgur.com/pJ4vRok.png)

![](https://i.imgur.com/C25vL7y.png)

**4. Melspectrogram + LSTM**
![](https://i.imgur.com/vWdkQ7t.png)

## [ 3. CONCLUSION ]()

**After trying everything, I come to a conclusion that.**

1. For my dataset, it’s just simple 1s, 1 word. No context or remember previous words needed to predict them.

2. For the LSTM models, it seemed like they were easily overfit when the train accuracy is up and the val accuracy not improving.

3. No need to say, when LSTM seemed to much, a melspectrogram with LSTM layers are even easier to get overfit, they remember so many features that is not important.

4. For shallow neuron network, it was proven that it can not learn important features to predict voice correctly.

5. CNN model works well because if you save the voice spectrogram as img and run CNN model to predict these image, the result is quite good as well.
 
---



