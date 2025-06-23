# A sea of cables and protocols

A message from your friend: "Have you already uploaded the photo?" — a simple thing that enmascarates a complex and humongous network of cables and protocols that allows you two to communicate. Let's dive a little deeper into the internet.

First, you and your friend exchanged keys when you two added each other in (message app). Now, when she pressed send, the message she wrote was encrypted using the key you gave her — your public key. When the message arrives at your phone, before you even open it, it is decrypted using the key you did not share — your private key.

This protocol of having 2 keys, one private and one public — to share the public so others encrypt the messages they send you, and to decrypt with your private key — is called SSH. Now, this only accounts for the security part.

## Bits and Bytes

A bit is an interrupter that can be either on or off. In electronics, this normally relates with having a low voltage or current (represented by a 0) or a high voltage or current (represented by a 1). A bit is either a 0 or a 1.

If you group 8 bits, you have a byte. And with a byte, you can represent not 8 numbers but 256 numbers... how?

### Binary System

Imagine you have powers of 2 arranged from 2^0 to 2^7, and under this array, you have an interrupter that decides if the power of 2 over it is summed to the grand total or not. That is a binary system. All 8 bits on and you have 255.

Then you can add other codification systems on top of this one to use bytes to represent characters, like UTF-8 or ASCII.

So, your friend's message is converted to a series of bytes that are sent via waves to the Wi-Fi router at your friend's house, or to one of the cell phone antennas her cell phone is connected to (more than one at the same time). Then these devices convert it to an electrical signal that is sent via cable to an Internet Service Provider that is the company that conects you to the rest of the world. in colombia (Movistar,claro)

## IP Addressing and DNS

Just as your house has an address, your internet connection does too. All internet connections have an address. For this addressing, there are 2 protocols — IPv4 and IPv6. The first one uses 4 bytes to represent addresses. I'm sure you are used to seeing numbers like 127.0.0.1 (this is set as localhost).

Nowadays, IPv4 is used to represent some form of local network, and it's being used at the same time as IPv6, which has 8 bytes to represent addresses. IPv6 uses the hexadecimal system to represent them, so they look like AAAB\:FFF::1234, where :: represents a space where all numbers inside are 0.

Now, remembering all these numbers is hard. Imagine — wouldn't it be so much simpler to say to the Uber driver, "Take me to the house of Fulanito de Tal," and he immediately knew where to go? Well, the Uber driver is your browser, and there is an actual translator that allows this to happen. They are called Domain Name Servers. These servers translate the name of the place you want to go — e.g., minijuegos.com — to the IP address of the server in which minijuegos.com is hosted.

## Server-Client Model and HTTP Methods and Errors

## Domains and Programming Languages
