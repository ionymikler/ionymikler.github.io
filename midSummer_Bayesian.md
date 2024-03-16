# Mid-Summer Bayesian Dream

On the fall semester of 2023, I took a class on theories of Logic and Reasoning. Using logic proposition and another bunch of fancy things mathematicians use to model knowledge update on different knowledge logic systems…

⚠️ <mark>I’m going to butcher terminology here. It’s an anecdote not a paper</mark>

… this class touched a little on bayesian learning and belief update (not what you and I think it means but what it means in the context of the field). Anyway, I learned about **bayesian information cascade.** The dream in this post.

See when you *follow the rules of reason,* in which you’ll want to be able to decide based upon the most update knowledge, yes? You want to be aware of the latest evidence to support or refute a claim, to decide whether or not you believe that *“I did not have sex with that woman”.*

However, if that knowledge is just wrong, and you’re base your reasoning on just the right wrong evidence, then you’ll never change your belief. The right amount of wrong information and you’ll be down a *cascade of information.*

## Two urns walk into a bar…

Imagine two urns 🏮, both have five balls. **Urn 1** has 3 blue balls and 2 red balls. **Urn 2** has the the opposite; 3 r and 2 b. One urn at random is put inside the room and, volunteers go one-by-one into the room see the ball, come out and write in a board visible to anyone, which urn (1 or 2) they *think* the urn in the room is. They, obviously, explode in a cloud of confetti right after they doing this so they can’t tell anybody what ball they picked. Oh, and they have this compelling need to not lie, never.

Let’s continue the experiment. Agent 1 come in, and picks a ball. The 1st ball is blue. This leads her to think: “hmm, its more likely that I pick blue in the blue-majority urn, urn 1, so this I think this is urn 1. Right before she could explain her reasoning, volunteer 1 squealed away leaving a dust of confetti (you thought that was a joke? nop, sorry)

$$
\begin{array}{|c|c|}
\hline
Agent & Guess \\ \hline
1     & B     \\ \hline
\end{array}
$$

In comes volunteer 2, and avoiding the confetti on the ground comes into the room, picks a ball, blue, comes out, sees the board and fills a row at the bottom:

$$
\begin{array}{|c|c|}
\hline
Agent & Guess \\ \hline
1     & B     \\ \hline
2     & B     \\ \hline
\end{array}
$$

> The question becomes then, how can this go wrong? (me, just now, 2024)
> 

In comes poor #3, oblivious to the fact that he’s been robbed of his randomness. What will he guess the urn is? This is the question, what will happen here?