# From Prehistoric Times to You

In the beginning, computers were these huge things, you needed a big room just to have one computer, and they did not have OS. No, you wrote the program and waited for the output in a paper receipt-like format. One program at a time, but then running more than one program at a time was needed. Here is when the first OSs were built, to run on servers because in the 70s personal computers or PCs weren't a thing. This is how UNIX and BSM were born. There were a whole lot more, but from these two, the operating systems from today were born. From the second one, Sun Microsystems and FreeBSD were created. Then Xerox Laboratory created a computer with something really strange called a mouse, and a GUI interface where you didn’t type commands to interact with the computer but it showed you everything in windows with graphic icons, and you used the mouse to select these icons.

Well, these guys decided to give a walk through their installations to some friendly folks—let’s call them the Steves. They had a company with the logo of an apple but had never sold fruit. These guys basically ripped off the ideas of Xerox Laboratory and made them popular in the future. But it was hard to implement these ideas; they were having some problems, so they asked for help from a friendly folk called Bill.

Bill used his mom’s contacts in IBM to convince them that they had a great OS to sell, then went and bought an operating system for PCs, not for servers, that was created by other guys named DOS. This is how IBM PCs started running Microsoft DOS. So Bill went to help his good friend Steve. Because Bill was a good programmer, he took a peek at their code and inspiration stroke him. Now we have Microsoft Windows and MacOS. The secret to succes is to be a friendly folk with great lawyers? well not necessarily.

Let us now pay attention to the most popular OS on the whole planet. That’s right—Linux.

Created by Linus Torvalds and supported on the GNU project ideas, and with the help of some other projects but mainly and more importantly with the framework of FREE software—but not FREE as in no cost, but FREE as in FREEDOM.
 Once yours, you can see the code and manipulate it.
A lot of enterprises used Linux to create and maintain open-source projects (once upon a time Bill hated open source and tried to destroy all of them). Now we have different flavors of Linux (Ubuntu, Arch, Fedora, Mint) running on all kinds of servers and personal computers, but especially we have a flavor of Linux called Android that runs on every pocket computer called a phone (and Windows now loves open source).

The world spins fast don't you think¡?

And here we are. You have just turned on your device (phone or PC) and want to share some files with some friends via the internet.

What happens now?

## The File System and Extensions

If you are too used to your phone, when you think of searching a file—aka a photo or a PDF—you think in terms of apps. But it has never been this way. The thing is that there is something called a file system that is a system of folders and files sorted in a particular way. The apps access this system, but the phone doesn’t show it to you. In PCs, it's starting to happen the same—in the address bar of your Windows File Explorer, you don’t see the **"file path"** but some names.

* In Windows, the root of your files is `C:` and is the same as the root of your drive (SSD or HDD)
* In Linux-based systems, it’s `/` and it is not the same as your disk. Your disk is on `/mnt/C`

Anyway, in both there are 3 types of folders:

* **Users or usr**: Here there is a common folder named `home`, where all the data of your user is saved. It could also happen that you encounter OS files or app files that are just for that user to use.

* **Apps or Program Files**: Files your apps or programs need to run and properly function

* **OS Files**: The central files for your kernel to properly work

The same is happening with extensions. They are never shown in phones or PCs by default. Extensions are 3 or 4 letters that follow a dot after the file name. They tell you and the OS what type of file it is. Depending on the extension, the OS and you can expect a structure and format of the data inside. Let’s review some common extensions:

* `.txt`: For plain text files
* `.jpg`: Joint Photographic Experts Group—an image file standard
* `.mp4`: A container for videos. Video files are a composition of a codec file, an audio file, and a subtitles file. The extensions of these files are H264, MP3, and SRT
* `.zip`: Compressed file that uses frequency and binary trees to build a compression algorithm. See the `compress.py` file in the repo for a little insight
* `.csv`: Comma-separated values—a very common format for tabulated data, but they are not database files

All files have something called a header—same as the formats of non-volatile memories (drives). Here the first 4 letters are the extension of the file. Then there is other information called metadata. This is information about the file. You can see all this if you use a hexadecimal text editor.

## Databases

They can be relational and non-relational. The non-relational can be graph-based or document-based. Or you also could have key-value databases like Redis. The relational databases are the most common, I think, because they are the oldest ones. The purpose of all databases is to avoid redundancy in the data structure but to be easily written and read and also to store humongous amounts of data. For this, the language SQL is used. The most common database engines used are SQLite, MySQL, Oracle, and Postgres. Why does this matter? Well, now you’ve found your file or photo and you attempt to save it on the internet in someone else’s database (a social network, an email service, a message service—you pick). Let us connect to the internet.
