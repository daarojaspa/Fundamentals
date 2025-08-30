---
title: "Money + Tech = Bitcoin"
category: Software
--- 

## How Money Works

Since 1971, under Richard Nixon’s Republican period, the dollar stopped having an amount of gold standing behind it. From that year, all around the world, money stopped being something with a material meaning and started to be the reflection of trust in a system of government and private entities (national and private banks among them, but not the only ones). National banks can decide to create more money (papers or bills: dollars, euros, pesos). More papers, same trust,less value per paper, more inflation. Seems like a lot of power concentrated in a couple of hands, right? If there was only another way...

## What Is Proof of Work

When it’s guaranteed, you have to do some kind of effort to acquire a result, not take easy shortcuts. For example, having a strong, muscular body can be easy to check. And if the only place to get steroids was Mount Everest, you could either train or try to get to Mount Everest. It’s harder to cheat than to do the task.

### What Is an Algorithm

It is just a list of instructions that leaves no room for ambiguity. The language or structures that allow you to create a set of instructions like this, so a PC can interpret them, are normally known as programming languages.

## Accounting Notebooks

They used to keep a register of financial operations. Later, they changed to the form of Excel spreadsheets and books. At some point, someone decided to encrypt (disguise, like when you and your friend decided all “a” in your messages would be a “y” and only you could understand the meaning of them) a huge spreadsheet notebook to ensure the information in it was not changed.

### What Is a Hash

So, that person found a machine where they put all the text they wanted to encrypt and the output was 256 zeros and ones. This array is called a hash, and the machine a hash function. It’s easy to know if a machine like this is a hash function, a funny one, or a broken one.

- Same input = same output. ALWAYS.  
- No matter how long the text, the output is always 256 zeros and ones.  
- No way to reverse it or predict the hash.  
- It does the job fast.  
- Two inputs that give you the same output is almost impossible.  

### What Is Bitcoin

It is a way to transfer trust in the system itself, just like money since 1971. But this system does not depend on a central authority serving as referee for the transactions. Instead, it implements a mechanism where all the participants can be referees. How? Well, it runs over something called a blockchain. Every block is just an accounting book, and all accounting books have a reference to the last one that was filled up. Now, an algorithm groups a bunch of transactions for the new block, but in order to add this block to the blockchain, the persons (or machines) in the blockchain have to find the correct hash, putting in use the proof-of-work mechanism. They pass as input the transactions, the reference to the previous block, and a random number. What they change is the random number. Each guess can take at least 10 minutes to compute. The machines that do this are called miners and the process is called mining.

If a miner guesses correctly, they earn the right and the pay for being the intermediary in that transaction. They get paid the transaction fees and newly created bitcoin. Bitcoins have a limit. The system was created with only 21 million bitcoins in existence, so every 210,000 blocks (about 4 years), the amount of bitcoin created when a block is added is reduced by half. No inflation.

The popularization of these technologies and the massification of the use of LLM-based applications like ChatGPT, together with the necessity of less battery consumption, have made necessary changes in chip architectures. Becoming more popular is what is known as a “system on a chip,” which is the integration on a single chip of the CPU, TPU, GPU, NPU, Wi-Fi adapter, barometers, thermometers, etc.  
I know, I know — in this series we have only covered a couple of 'U's so far, so let’s review (take a little walk, let  what you have learn settle and keep reading).

## CPU

The most common processing unit. It processes things in series and switches between processes to give a sensation of parallelism.  
Intel, AMD, Snapdragon, M1 from Apple… Every operation occurs in what is called a cycle, controlled via a little crystal inside the PC.  
A 2.1 MHz frequency means 2.1 million cycles per second. An operation — the smallest one — needs about 4 cycles (just to save something like a number in memory). A click or writing a letter is a compilation of these small operations.

## TPU

A Tensor Processing Unit is a chip designed to do tensor math, where a tensor is a special kind of number array, like a matrix but with more than two dimensions. It uses 8-bit arithmetic to be precise and energy-saving. It is especially used for neural networks. It was invented by Google and has its own low-level programming language called CUDA. Imagine it like a monk that only does linear algebra.

## GPU

A GPU uses parallelism in processing; it does not just emulate it like a CPU would(real multitasking, not changing focus every 3 seconds). GPUs were developed especially because of the gaming industry. They usually have their own RAM memory called VRAM and their own cooling system, all minners are usually GPUs.  
We still use CPUs because GPUs are awful with general tasks.

## NPU

A Neural Processing Unit is a chip designed to accelerate AI workloads, particularly for deep learning models. It optimizes matrix multiplications and tensor operations, similar to a TPU, but is more general-purpose and designed for integration into consumer devices such as smartphones and laptops. An NPU makes AI applications like image recognition, speech processing, and natural language models run faster and more efficiently with less battery consumption.

congratulations, it's been a long journey, why dont you give it a try and  invite some one to hang out and share what you have learn here.