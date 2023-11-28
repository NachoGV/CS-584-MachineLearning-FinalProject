# RTMLCA: Real-Time Machine Learning model for large-scale cybersecurity attacks

RTMLCA (Real-Time Machine Learning model for large-scale cybersecurity attacks) is a machine-learning approach that performs classification task over pcap files to infer whether a TCP packet is a threat or not.

## Getting started

First, you have to install the project dependencies. We suggest to create a conda environment to avoid dependencies errors.

```
pip install -r requirements.txt
```

## Data preprocessing

To train our model, we have used the public dataset from the University of New Brunswick ([Link to access the dataset](https://www.mdpi.com/1424-8220/23/13/5941))

## Models

We have trained several ML models that performs classification task.

## Demo attack

For the shake of knowledge, we share the steps we performed to demonstrate our RTMLCA.

### Ubuntu

To record PCAP packets,

```
sudo -E python3.10 ./real_time_traffic.py
```

To send SYN flood attacks to the IP of the victim: <IP_VICTIM>

```
sudo hping3 -S --rand-source --flood <IP_VICTIM>
```

but in our tests, we ran it without --rand-source since we had to check the ground truth.

```
sudo hping3 -S --flood <IP_VICTIM>
```
