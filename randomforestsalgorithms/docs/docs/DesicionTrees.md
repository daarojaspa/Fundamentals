# 🍬 Decision Trees, Dragees, and Forests

As any fan of *Harry Potter*, you've bought Bertie Bott's Every Flavor Beans (dragees) to try them out. You've heard from online reviews that each color usually has two associated flavors, and that the pink one can be the best... but also the worst.

So, you plant your first **yes/no** question:

> **Is the dragee pink?**

- If **yes**, you write the next step on the **left** sheet of your logbook.
- If **no**, you write it on the **right** sheet.

Whatever the answer, the next step is to ask the second yes/no question:

> **Does it taste bad?**

- On the **left**, you count the **yes** answers.
- On the **right**, you count the **no** answers.

```mermaid
graph TD
    A[Is the dragee pink?] -->|Yes| B[Does it taste bad?]
    A -->|No| C[Does it taste bad?]

    B -->|Yes| D["Record as 'Pink & Bad' on left sheet"]
    B -->|No| E["Record as 'Pink & Good' on right sheet"]

    C -->|Yes| F["Record as 'Not Pink & Bad' on left sheet"]
    C -->|No| G["Record as 'Not Pink & Good' on right sheet"]
```

The first question is called the **root**. Other questions are called **nodes**, and the final answers are called **leaves**.

This is a very simple **decision tree** to predict the flavor of a dragee based on whether it's pink or not. Of course, we could include more criteria, like other colors, shape, or even the shop where it was bought. No matter how many features you have, always think about asking questions with **binary answers** (yes/no, true/false, 1/0, up/down).

---

###### What Question Should I Ask First?  
###### How Do I Know When to Stop Asking?

Let me show you the **Gini in the bottle** 🧞

---

## Impurity and How to Calculate It

"Impurity" refers to how mixed the votes (or classes) are in a leaf.

- If they're 50/50, it's said to have **high impurity**.
- If they're unanimous, it has **0 impurity**.

We can also talk about **node impurity**, which is the **weighted average** of the impurity of each leaf.
There are different ways to calculate it, but the most common is **Gini Impurity**:

\[
Gini = 1 - \sum_{i=1}^{C} p_i^2
\]

Where:
- \( C \) is the number of classes
- \( p_i \) is the probability (or proportion) of class \( i \) in the node

---

## What Question to Ask First?

1. Try all the questions.
2. The one with the **lowest impurity** is used first.
3. Next, ask the question that **reduces impurity** the fastest.

---

## When to Stop Asking?

- The node you're in is completely **pure** (all samples are the same class).
- The **maximum depth** you decided your tree should have is reached.
- There are **too few samples** to split on.
- There are **no more questions** left.

Depending on which stopping criteria you pick, your tree can get really big —  
but you can still **prune** it using your favorite library’s pruning algorithms.

---

## What If the Features Are Numerical?

Let’s suppose you have a list of dragee **radii**, and you want to predict flavor based on that.


1. **Sort the list** of data.
2. Calculate all the **adjacent averages**:
   - Average between first and second, second and third, and so on.
3. Ask a **binary question** for each average (e.g., "Is the radius ≤ avg?").
4. Calculate **impurity** for each.
5. **Pick the one** with the lowest impurity to use in the tree.

- When a tree **predicts categories**, it's a **classification tree**.  
- When it **predicts numbers**, it's a **regression tree**.

In essence, they work very similarly.

---

## Overfitting

Overfitting is like studying for a test by memorizing all past questions.  
- If the same question comes up, you’re fine.  
- If a new question appears — you get it wrong.

Decision trees are **prone to overfitting**, which brings us to democracy, but first ...

---

## Let's Plant a Forest 🌲

From your original dataset, take a random sample with the same number of data points (allowing repetition).  
This is called **bootstrapping**.

Then:

1. Train a decision tree using the **bootstrapped sample**.
2. At **each node**, only consider a **random subset of features**.

Now **repeat** the process **many times**.  
You’ll get many trees of different shapes and sizes — a **forest** full of **variety**.

Each tree gets a vote, and the **forest decides by majority**.  
The category with the most votes **wins**.

> The important thing here is **variety**.  
> Without it, it's not a democracy... it's a **demo‑crazy** 🪓

Now get out and plant some trees, invite your friends , tell them what you learn here.

If you want to see code, chek