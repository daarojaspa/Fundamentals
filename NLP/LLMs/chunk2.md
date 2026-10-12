# 2017-2025 review

In 2017, *Attention Is All You Need* was published by Google, proposing the self-attention paradigm.
2018: BERT came to life.
2019: OpenAI (it was really open at that time) published the paper *LLMs Are Multitask Learners* and the model GPT-2, where they applied the architecture that Google published in 2017 and realized something unusual: although the model was created to aim at translation tasks and prediction of the next word, when they asked for tasks it wasn't trained to do, it was not that horrible at them. In fact, the bigger the model was, the less horrible it was at those tasks.
So at the end of the whole experiment they had a hypothesis: maybe the multitask aspect of knowledge embedded in language could be reached with bigger models.
2020: GPT-3
2021: GPT-3
2022: ChatGPT

## Bigger is better? (Chinchilla came) 2022

By the release of ChatGPT, the conception of a better model was how big it could be, but a paper presented a model named Chinchilla, *Training-Compute-Optimal Large Language Models*, where this small model had the same performance as the big ones. How? It was trained on more data in proportion to the number of parameters the model had. What the paper found was groundbreaking, because that meant just a bigger model was a waste of resources. You had to increase all aspects of training at the same time, and they proposed a proportion:

training tokens = 20–40 times the number of parameters

Important not just for research, but for industry applications, because this meant you don't really need that many GPUs for the model you want to fine-tune (quality and domain specificity first) or RAG in your company. Just a smaller investment in data, so now you know what model to pick for sure: the one that matches your data budget. If what you want is to distill, the teacher should be between 3 and 10 times bigger than the student, and same ratio for data — the student should see 3 to 10 times more data.

## Multimodal Models are already here 2023

Imagine that you have a model that understands text, and you could see the vectors that represent each word in a 3D space: a white room filled with arrows that come from the same corner and go in every imaginable direction.
Then the same, but for a model that understands images, and for another model that understands sound.
Then somehow you put the text 3D space over the image 3D space, and then over the two of them the sound 3D space, ¡¡¡AND THEY FIT!!!

That is the essence of a multimodal model: the arrow that represents a dog in the text space is the same as the image of a dog in the image space, or the sound of a dog in the sound space. So yes, three different models are connected, but in a way that allows them to learn shared representations of the same concept. Of course this is not automatic; the models have to be trained using paradigms like contrastive learning and discriminative learning. This area of deep learning is a huge field that started around 2015, but with the transformer architecture implementation it started to shine with papers like ImageBind by Meta.

- Early fusion: all modalities are concatenated from the beginning, and a big transformer processes everything. They can develop strong reasoning, but consume a lot of computing power.
- Late fusion: all encoders are separate from each other until the last stage, where a smaller network merges them.
- Cross attention:
-

## How to train your Model 2024

First you want to build pre-tokenization and tokenization pipelines. This involves heuristics and some ML methods based on frequency, as far as I know. This part is crucial to how expensive and accurate inference will be. The main objective here is to deal with spaces, typos, capitalization, and punctuation, and normally — if you need it — you can use lemmatization and stemmers. To build the tokenization algorithm you can start by using every character as a token, then merge the most common ones, and repeat until you get an average length per token desired. Shorter tokens, more flexibility, but you will have a higher computation cost; longer tokens, the other way around. The optimal trade-off is around the subword length. If done right, the training can be 3 times faster than if not, and the dataset on which it is trained should be almost the same dataset the LLM will be trained on. So here comes the central question.

###### Can I code a subword and character-level tokenizer?

### How do I get the data?

The internet is actually kind of dirty to just take all documents in it, and since you will need to use a web crawler to scrape the whole internet, you will not get clean, beautiful, ready-to-use documents, but a bunch of HTML tags, attributes, and a lot more. So after the web crawling phase, you need to do something called HTML extraction, which is to keep the content of the page and not all the other stuff. Then you will need to filter the content. How? Well, blacklisted pages will be banned, so you have to have access to a big list like this one, then implement heuristic filters to eliminate low-quality documents, after that do deduplication (eliminate things that are too similar to each other). After that you could split the remaining data into validation and train datasets. Then with the train dataset you should somehow train a classifier model that will help you find which of your documents have been referenced by a high-credibility source, to give those documents more importance, and also a clustering model to group the content into domains. And if you want to give your model a better performance in a specific domain, well, upweight the documents in that domain. At the end you have a training set that is kind of stratified by quality, and you want to train on the whole dataset but kind of overfit on the higher-quality data.

This is just what I could find out, but there is a lot of secrecy around this area, and we did not mention synthetic data or multimodal data.

### Post-training

Now you have a probabilistic model of language that is really good at predicting the next token. Now let's train for alignment (a fancy word to say: teach the LLM to act as a human).

50k to 100k high-quality examples of prompts + ideal answers should be enough to do supervised fine-tuning, I think. Now it is possible to combine this with LLM-generated examples. After this, the RLHF stage starts, where the main goal is to clone human behavior. You can use Proximal Policy Optimization (PPO); this meant training a reward model on human preferences to reward the LLM when it had a good answer. But now Direct Preference Optimization is being used, where you show the model a good answer vs. a bad answer. And how does the human get in? Well, human annotators first rank the answers that the fine-tuned model provides. The ratings are converted into a continuous function (Bradley-Terry), and that function is used to train PPO and DPO models.

### Evaluation?

After all that work (and 50–100 million dollars), now you have your model. Congrats!! Let's call him Thoughtless =)

---

## MoE, give me a Duff? (2025)

The Mixture of Experts intuition is easy to grasp. Instead of having a huge network that activates the same when solving cancer questions and when asking for a Duff, wouldn't it be better to just activate the part of it that is good at asking for fiction beers when it needs to? Obviously it can't be as demanding as solving cancer, right? That way the scaling laws are not going to limit us as much, and we can still grow our models without making inference slower and more expensive.

### Broader instead of deeper

MoE was originally conceived in 1991, and that was the whole architecture. You had experts made of one MLP, then a non-linear function like hyperbolic tangent, and again a linear layer. There was a smaller network with the same architecture whose only job was to decide which token should go to each expert in a probabilistic way. Then the token was sent to all experts and their answers were weighted on the previously calculated probabilities — a lot like a random forest if you ask me (random forest post)[].
The concept was applied again in 2017 with RNNs, in 2019 with transformers, and finally DeepSeek used it in 2024, which eventually materialized in January 2025 in the DeepSeek V3 model. What changed between 1991 and 2025?

A linear relationship was established between the size of the expert and the number of experts; a load balancing method that consisted in taking the 2 most probable experts to send the token and averaging the answers; a balancing loss that "punishes" the default network (router) when too many tokens are sent to the same expert (or when too few tokens go to another expert); and now the experts have a limited capacity for tokens to bound compute.

### How it interacts with multimodal architectures

Because these experts are essentially the feed-forward part of the network chopped into smaller pieces, you can put them after the tokens are mixed, or inside each modality encoder before the tokens are mixed, or inside the fusion head where the tokens are mixed. The most popular is cross attention + MoE.

### Good for everything?

#### The real bottleneck:

Yes, you will need fewer GPUs for inference, and yes, latency can go down, but have you heard about the KV cache and memory bandwidth?

If you don't have a very good KV cache or high-speed bandwidth memory, maybe MoE is not for you — maybe distillation or quantization, but that will be for another blog. Stay fine-tuned. And go outside.