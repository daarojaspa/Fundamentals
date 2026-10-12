## artificial neuron
There was a creature wans that look like the  peon on chess and this criture had thougts that where preaty basic and 
complex at the same time, first, the lenguge it  understood was matematics, only that, so  it only  
spoke numbers and heard numbers, and the thougth that it  had where eather a linear regration  or a  logistic regration,
sow if you tell them numbers it " imagine  a line that fit  the best those numbers,  or a squigle  that put a limit
on wich 2 clases of numbers where  separated eather way in a matematic sens this toughts where lineal
# neural networkl
now imagine 2 lines of peons  the peons dont talk to the one bisides them but it talks to all the peons
 in the line infront of them.A neural network is this arrange type of peon like criatures
##types of neural networks
 - Fnn: This feed forward architecture is used  for clasification problems whit structure data, and are escential to all oter types	
 - cnns:  To proces spatial information that comes in a grid like formatby default, like images and videos, the peons 
	the  neural networks of peons  started to as a hole make a more complex operation called convolution 
 - rnns are really good  for secuential time  data like oudio. LSTMs for example have  a  feedback loop, in their
neurons that allowthem  short term memory, how ?  the last line of  peons gave an output that was a input  for the 
first line 
 - Auto encoders: compress and decompress the information, and they can be deep ( many layers) , the idea is that
 you can filter the noise in  a bunch of information to capure the escense  play with it and then give back the information 
mor less as it was give to you. imagine a first line  that is 10 peons  a second that is 8 a third that is 4, they have a funnel like form. (decoders are just a funnel out ) 
- gans: A discriminator  has to figure out if what the generator created is a fake sample or not
- transformers: Just wait for it ¡¡¡

# the matematics of lenguage
When i was a kid i love to sit in the back of the class room  and talk with my friends, the teacher did not love it, 
so we end up passing by little pices of paper with messages, we change  consonants by numbers, so if we got cougth , 
no body will know what we wrotte about. Imagine my sorprise  when i found out that thats how  esentially  we teach these 
creatures call Neural Networks about our languaje, offcorse for they  are just numbers, they dont get the meanning, 
like the teacher  when he got our message.
## stimers
Algorithms that help us reduce words into the closes  root form for example running will be convert to run it uses 
rules not machine learnning, and some times  can chop of the word to a non existing word like passing to pas 
##lematization
Now this  goes dipper  it returns a dictionary base form , so better could become  good, but it needs  tagging, 
remember when in school you had to reconize which word in the sentence was a noun or a verb or and adjective, thats
 tagging
##tokenization
Now tockenization is as simple as divide a sentence into words, or syllables, or lemmas ( from lematization) or 
steams (after applying a steamer). Now you can  convert thouse words into numbers or array of numbers
## embeddings or frquencie vectorizer
The diference beween and embeding,and a vector is if saves contextual meaning, remember we still are talking about
converting words into numbers,one way to do this is after lematizing and tokenization to take a big bag of words
normally  call a corpus, and messure  how much each word in the bag repeets in a set of documents, this is a 
frecuency aproximation
and  as you can see there is not information on how  one word relate to  other words in terms of meanning.

Other metoth is  to use pre train models, that were train to change the value of the vector depending the what it 
meant and how close  the vectors that represent similar words would end up  in regart of that first word. so the vectors 
for words like : snow, cold,ice,winter will be relaive closer to each other and not so close from the
 ones that reprecent words like canguru,monkey, tiger 

## Atention position matters and  is not new 
The first  application of the concept of attention , that idea that a word can affect or reffer to a previus word, was  
used in feed forward networks that am to  compress  the hole sentence ,but  it was a bottle neck, then they used additi>
attention, where a small neural network computed a score of how each tocken matter in each state of the neural network. 
then thay realize that they could use dot product to  seee how similar  two vectors   where and this will be more efici>
then in 2016  self attention was born, where trougth  a series of matrixes Key, Query and Value, they compute how  all  
tockens in a sequence relatted to each other inside an RNN that was until that time the default network for language.   
                                                                                                                        
Then Multihead self attention came along and  since then  the concept have been evolving, solving  problems of long     
context (the amount of text you can pass before starts forgetting).  

Now as you  already know in such a obvios sens ,"Atention is not new and position matters" is not the same than what  the title 
above says . positional ordering is part of how we understand language the firs attempts to embed this in to the  input of the network ( vectors/ embedings ) 
words was . 
###Transformers.....¡¡ Ensamble ¡¡                                                                                                     
Lets recap, for  along time, in deep learnning, image processing and recognition was the  hip new thing                                            
because Cnns , but for languaje the best we had was Rnns, the thing is that languaje is secuantial, so if you                        
shuffle the order of the woeds  on a sentence you change  the sentence meanning, so they were used for  translation                  
and did good  for short sentence but with long sentences,lets say the RNNs have a little les memory                                  
than Dory from Nemo. Then a anew architecture of neural networks ( the peon's lines ) was created , this new architecture used  positional
encoding, and self atention mechanisms                                                                                                          
                                                                                                                                                                                                                                              
                                                                                                      
