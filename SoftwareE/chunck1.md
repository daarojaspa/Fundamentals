# Fundamentals for Technology and Computers

We will explain the path from where you turn on your computer or cellphone until you start a conversation with another person on another computer, and through this path, explain the different concepts you must know.

## BIOS, UEFI, or Bootloader

Electricity comes through via your power network (220-110 volts in the socket, but then lowered to your device's needed voltage). You push "on" on your device, and the first part that wakes up sends something called a POST — **Power On Self Test**. This process recognizes the other parts on your computer:

* Keyboard: which can be in different distributions like QWERTY
* Screen: made from pixels that are 3 little light bulbs — green, red, and blue
* Hard disk: a long-term data storage device that can be SSD or HDD
* RAM: Rapid Access Memory in which your files are transported from the hard disk to use them in "real time"
* CPU: a bunch of transistors that are the core of your processing power, doing one task at a time in multitasking mode

### Architectures and the Bit and Byte System

Your CPU is made through a process called lithography. The company that does this best in 2025 is LSM, printing 3D cities of transistors with streets 12 atoms wide. There are different architectures of CPUs based on common tasks they normally have to do, taking into account the use they are put to.

* **ARM**: Are built with energy consumption and compatibility in account, very popular for mobile devices
* **X86**: Optimized for the common operations in Windows operating systems
* **RISC**: Very simple, mainly used in datacenters and servers, they are multipurpose

### Memory Assignment and Management

Well, we have 2 types of memories: persistent and volatile. The first one is on devices like the BIOS, the mechanical drive, or the SSD. The second type of memory is on devices like cache in CPUs and RAM.

Volatile memories are the fastest, with cache being the fastest of all, then RAM. After this, we can talk about SSD, and finally, mechanical drives.

The RAM gets filled with the files you are working on. When they are open but not used, they are sent to the SWAP memory — a piece of the SSD or HDD used as RAM, but which is much slower. A bunch of programming languages now use something called a garbage collector to clean the RAM from stuff that is no longer useful. If they are not implemented, the PC will start to get slower.

Now your operating system will encrypt your files using your password and username. This encryption will happen in different formats.

#### Formats of Persistent Memory

* **APFS**: Apple File System
* **FAT32**: The original format used by Windows. Files could not be larger than 4 GB. Did not have much security or a robust permissions system.
* **NTFS**: Faster, safer, and newer — the modern format for Windows systems
* **EXT3 or EXT4**: Linux distributions' default formats — high security and fast

What these formats provide is a header of the file map — an index like a table of contents. What happens when you delete a file is not that the file is really deleted, but the pointer to that piece of memory in the table of contents (in a book it would be like "page 4: Humanity’s kinkiest secrets") is deleted.

Now, when you need to save something else, the OS will think that space in memory is available and overwrite whatever is there.

## OS

Then your operating system enters the scene, working as a bridge between the hardware of your device and the other software that you will run. It uses APIs to communicate with high-level software, like a word app or a browser, and drivers to communicate with hardware like your screen. Think of these two terms — drivers and APIs — like a set of rules and protocols that define the communication between the kernel, the hardware, and third-party software.

### Kernel and Virtual Machines

The kernel is the heart of your operating system, where the really important and unpredictable stuff is programmed in a low-level language like C. Your OS has to manage a lot of security processes where it has to manage the communications between many things on different levels of security. For example, your bank website can be accessed without your word application knowing your bank password or bank data. For this, they use a scheme of 4 rings of security.

Inside the first ring, the kernel runs. Then inside ring 1 and 2, you have your drivers and APIs. Inside ring 3, you have your third-party apps like Word, Excel, etc.

Now, imagine for a moment that there is a way to create a bubble inside ring 1 that makes everyone think it is in ring 0, although ring 0 — the real one — is still running. Now imagine that you can have many of these bubbles. This is the main idea behind virtual machines.

A virtual machine is the heart of cloud computing. All that you have in the cloud is inside a virtual machine running on someone else's PC (Google, Microsoft, Amazon).
