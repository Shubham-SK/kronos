# Kronos
A voice powered app
___
### Usage
Clone the repository, navigate to the server.py file. 

```
git clone https://github.com/Shubham-SK/TreeOverAte.git
cd TreeOverAte
```

Ensure [Flask](https://pypi.org/project/Flask/) is installed and run the server. It should be open [here](127.0.0.1/5000). 

```
python server.py
```

Upon opening the link, you should see a greeting with your name and an option to start recording the patient-doctor conversation! When you're ready to start the checkup click record and make sure the doctor is first to speak.

### Hardware Required
Raspberry Pi with a microphone (tuned Hz so Google speech API can extrapolate). We use a lightweight [MQTT](http://mqtt.org/) messaging protocol to transmit the recording file from the Pi to a webserver where the data will be parsed and distributed to the end user.

___
### Parts of Our Project
- Data Acquisition
- NLP speech to text
- Text analysis with a Bidirectinal RNN/LSTM with Attention
- UX/UI for doctor

#### Data Acquisition
We decided to use a RaspberryPi board to run an MQTT protocol, which can successfully transfer recording files. The recording is saved locally for the speech to text parser and for the ML model to summarize.

#### NLP speech to text
We decided to use [Google Cloud's](https://cloud.google.com/speech-to-text/) speech to text API to convert our recordings into textual data. From our experimentation, it outperformed our expectations and showed accuracy in even converting the most complex medicine names. We designed 2 different scripts for analysis since shortly after creating the first one, we realized we had to distinguish the voices of the patient and the doctor. Luckily, google had a service for this and we were easily able to accomodate changes.

#### Text analysis with Bidirectional RNN/LSTM with Attention
In order to make the Transcript easier to read and retain essential content, we decided to take advantage of the latest state-of-the-art models to summarize our text. After training it on hours of patient-doctor data, we were able to obtain a very reliable summarizer. We used pytorch to define the model, train and test it. We had it training on an EC2 instance running on AWS cloud for several hours before we received a low loss.

#### UX/UI for doctor
In progress lol.
