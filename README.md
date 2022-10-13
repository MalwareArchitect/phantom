[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<p align="center">
    <img src="https://i.postimg.cc/c4j7YGQv/Phantom.png" width=300>
</p>
<h3 align="center">PHANTOM</h3>
<p align="center">
   Why buy a burner phone, when Phantom allows you to text anyone... anonymously!
</p>

[![version-badge](https://camo.githubusercontent.com/8341cfbe224718e1c2334bc81363673efd2565f8b6878314a96d03e4ce42213b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6369636972656c6c6f2f6d6f6469666965642d6c616d2d6578706572696d656e74733f6c6f676f3d476974487562)](https://github.com/SkippyTheTracer/phantom)

# 📖 Description
**PHANTOM** is a simple Python script that enables a user to text a victim from an anonymous number. The program uses the 'textbelt' API to communicate with a victim using a random generated phone number. Not only can you spoof messages, you can now also receive messages between you and the victim using the integrated webhook option. With an incredibly simple UI, sms spoofing has never been easier!

# 🎥 Demo
![Phantom Demo](https://j.gifs.com/79kGMj.gif)

# ⚖️ Legal Disclaimer:
**FOR EDUCATIONAL PURPOSES ONLY!** <br />
Misuse of **PHANTOM** is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. The developer assumes no liability and is not responsible for any misuse or damage caused by this program. Use Responsibly!
<br />


# ⚙️ Installation
```console
skippy@kali:~$ git clone https://github.com/AlgorithmNerd/phantom/
skippy@kali:~$ cd phantom
skippy@kali:~$ pip3 install -r requirements.txt
```
# ▶ Run
```console
skippy@kali:~$ python3 phantom.py 
```
# 🧰 Requirements
### TEXTBELT
In order to use **PHANTOM** at it's full capacity, you must first purchase an API key from https://textbelt.com/purchase/

<img src="https://i.postimg.cc/zGGn9X82/api-checkout.png" width=700>

You are also able to use the API key **textbelt** for one **FREE** message!

### WEBHOOK
It's not necessary to obtain a webhook url, unless you would like to receive messages. You can find a unique webhook url at https://webhook.site/

<img src="https://i.postimg.cc/MppFdS4q/webhook-site.png" width=700>

# 💻 Usage
## Sending a Text
Once the program is running, you will be asked to enter the victim's phone number.
```shell script
Phone Number:
```
You will then be prompted to enter a message. This will be the message sent to the victim.
```shell script
Message:
```
Now it is time to add your API key. Input the key provided by https://textbelt.com
```shell script
Key:
```
Now that you are ready to send the message, you will be asked if you would like to receive responses from the victim. If yes, type 'yes'. You will then be given the option to input your webhook url (as shown in the above example). If not, type "no".
```shell script
Would you like to receive reply messages? yes/no
```
Now that all of the steps have been completed, your message will be sent to the victim. You will be asked if you would like to send more messages. If your answer is no, the program will stop running.
## Receiving a Text
During the above process, you will be able to view the responses through your 'webhook.site' url. Be sure to look out for the **POST** requests, as they will contain the victim's responses.


### Now that you have learnt to use **PHANTOM**, be sure to have fun!
