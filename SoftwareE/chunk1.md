# fundamental for tecnology and computers

We will explain the path from where you turn on your computer or cellphone until you
start a conversation with other  in other computer and  throug these path explain the diferent concepts  
you must know.

## Bios wUefi or BOOtloader

Electricity come  true via your  power network (220-110 volts in the socket but then lower to your device needed voltage)
 you puch on on your device and the first part that wakes app
and send something call a post **power on self test**  this process reconice qthe other parts on your computer,

- key board :wich can be  in diferet distributions like qwerty
- screen: made  from pixels that are 3 little ligth bolbs green red and blue
- hard disk: a long term data save device that can be ssd or hd
- RAM: rapid acces memory in wich your files are transported from the hard disk  to use them in "real time"
- CPU: a bunch of transistors  that are the core of your proccessing power, doing one task at the time in multitasking mode

### architectures and the bit and bytes sistem

Your CPU is made trougth a process call litography ,the  company that does the best this process  in 2025
is LSM,  pringthing in 3d citys of transistors with  streets of 12 atoms wide. there are diferent architectures of
CPUs based on cummon  tasks they normally have to do, having on acount the use they are put  to.

- **ARM**: Are build having energy cumsomttion and compactability  in acount, are really popular for mobile devices

- **X86**: Optymice for the commun operations in Windows Operative sistems

- **RISK**: Very simple  mainly use in datacenters and servers, they are multy purpuse

### memory asignation and manage

Well we have 2 types of memories persistent and volatil, the first one is on devices like the BIOS the mechanical drive or the ssd, the second type of memory is on devices like cache in cpus and RAM.
Volatil memories are the fastest, being cache  the faster of all, then ram, after this we can talck about ssd and  finally mechanical drives.
The RAM gets filled with the files you are working on. When they are open but not used they are sent to the SWAP memory a pice of the  ssd or hdd use as ram but wich is much more slower. a bunch of  programming languajes now use something call  garbage collector to clean the RAM from stuff that are not longer usefull, if they are not implemented the pc will star to get slower.

Now your  operative sistem will encrypt your files  using your pasword and user name, this encryption will happen in diferent 
formats

#### formats of persistent memory

- AFPS:Apple file system

- fat32:The original format used by windows  files could not be lasrger than 4Gb did not had much security or a robust permissins system

- NFTs: Fastest safer and newer and is the now days format of windows systems 

- ext 3 or 4:Linux distributions default formats higth security and  fast 

what this formats provide is a header of the file map  is an index like a table of content  what happens when you delete a
 file is not that the file is really deleted but the pointer to that pice of memory  in the table of content
 (in a book will be like pag 4  Humanity kinkiest secrets)  is deleted. 
Now when you need to save something else the OS will think that space in mamery is available and over write what ever is there.

## OS

Then your operating sistem enters the scene working as a bridge  between thee hard ware of your device and the other software
 that you will run,  using APIs to comunicate whit higth level software, like a word app or a browser, and  drivers to comunicate
with hardware like your screen think of this 2  terms , drivesr and APIs like  a set of rules and protocols that defines the comunication between the kernell and the hardware and third parties software.

### kernel and virtual machines

Kernell is the heart of your operative system, where  the really important and unprecidible stuff are program in a low level
 language like C, your OS have to manage a lot of security processes were it has to manage  the comunications between a lot of things in diferent levels of security, so for example your bank website can be acces  with out your
 word aplication  knowing  your bank password or bank data, for this they use a scheme in 4 rings of security inside the first ring  the kernel runs in then inside ring 1 and 2 you have your drivesr and APIs and inside ring 3 you have your third parthy
 apps like word, excel etc.

Now for a moment imagine that  there is a way to create a bobble inside ring 1 that makes every one thinks that is a 0 ring althoug 
ring 0  the real one is still running. and now imagine that you can have many of this bubles this is the main idea 
behind virtual machines, and a virtual machine is  the heart of cloud computting, all that you have in the cloud 
is  inside a virtual machine running in some one else pc (google, microsoft amazon ).
