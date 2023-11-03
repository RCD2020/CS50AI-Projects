# Lecture 2: Uncertainty

## Possible Worlds

Represented as *⍵* *(omega)*, is the possibility of a certain situation.

To represent the probability of a possible world, use *P(⍵)*.

Every probability value must be 0 to 1 ($0 ≤ P(⍵) ≤ 1$), where the higher values are more likely.

When we add together all possibilities it should add up to one, we can represent this using the sigma **Σ** symbol.
$$\sum P(\omega) = 1$$

## Unconditional Probability

degree of belief in a proposition in the absence of any other evidence

## Conditional Probability

degree of belief in a proposition given some evidence that has already been revealed

$$P(a | b)$$
> Represents the probability of *a* given that we know that *b* is true

### Formula

$$
P(a | b) = \frac{P(a \wedge b)}{P(b)}
$$
> All probabilities where *a* and *b* are true divided by the probabilities where *b* is true

## Random Variable

a variable in probability theory with a domain of possible values it can take on

### Probability Distribution

Shows the odds of a value in a random variable, for example, let's say this:

$$
Flight \newline
\{on \space time, delayed, cancelled\}
$$

And then our distribution might look like:

$$
P(Flight = on \space time) = 0.6 \newline
P(Flight = delayed) = 0.3 \newline
P(Flight = cancelled) = 0.1
$$

Or we can represent it as a vector using a bold ***P*** (meaning probability distribution) and <>

$$
\mathbf{P}(Flight) = \langle 0.6, 0.3, 0.1 \rangle
$$
> And then we just need to know which is which using the first part

## Independence

the knowledge that one event occurs does not affect the probability of the other event

$$
P(a \wedge b) = P(a)P(b)
$$
> $P(b|a)$ becomes $P(b)$ because $a$ does not affect $b$

## Bayes' Rule

We already know that these equations are true:

$$
P(a \wedge b) = P(b) P(a|b) \newline
P(a \wedge b) = P(a) P(b|a)
$$

And so then we also know that:

$$
P(a) P(b|a) = P(b) P(a|b)
$$

And then Bayes' Rule is solving for $P(b|a)$:

$$
P(b|a) = \frac{P(a|b) P(b)}{P(a)}
$$

Meaning we now know $P(b|a)$ by using our knowledge of $P(a|b)$.

### Example

Given clouds in the morning, what's the probability of rain in the afternoon?

- 80% of rainy afternoons start with cloudy mornings
- 40% of days have cloudy mornings
- 10% of days have rainy afternoons

Using these probabilities, we can solve for $P(b|a)$.

$$
P(rain|clouds) = \frac{P(clouds|rain)P(rain)}{P(clouds)}
$$
$$
= \frac{(.8)(.1)}{.4}
$$
$$
= 0.2
$$

So now we know the probability of rain given that it is cloudy in the morning is .2 or 20%.

## Joint Probability

for getting the probability of many events together

### Example

Say we know the probability of it being cloudy and rainy:

| $C = cloud$ | $C = \neg cloud$ |
| ----------- | ---------------- |
| 0.4         | 0.6              |

| $R = rain$ | $R = \neg rain$ |
| ---------- | --------------- |
| 0.1        | 0.9             |

Then this would be their joint probability *(this wasn't inferred from the previous data)*

|                  | $R = rain$ | $R = \neg rain$ |
| ---------------- | ---------- | --------------- |
| $C = cloud$      | 0.08       | 0.32            |
| $C = \neg cloud$ | 0.02       | 0.58            |

And then we can calculate new information:

$$
P(C | rain)
$$
$$
P(C|rain) = \frac{P(C,rain)}{P(rain)}
$$
> The comma can stand in for $\wedge$
$$
P(C|rain) = \frac{P(C,rain)}{P(rain)} = \alpha P(C, rain)
$$
> Because we know that *rain* is a constant value, I don't know enough about mathematics to know why it can be represented as multiplying by $\alpha$.
$$
= \alpha\langle 0.08, 0.02 \rangle = \langle 0.8, 0.2 \rangle
$$
> I guess $\alpha$ is acting as a normalization constant???

## Negation

$$
P(\neg a) = 1 - P(a)
$$

## Inclusion - Exclusion

$$
P(a \vee b) = P(a) + P(b) - P(a \wedge b)
$$

## Marginalization

$$
P(a) = P(a,b) + P(a, \neg b)
$$

We can figure out the probability of a by taking the probability of a and b and adding it to the probability of a and not b.

$$P(X = x_{i}) = \sum_{j} P(X=x_{i}, Y = y_{j})$$

### Example

|                  | $R = rain$ | $R = \neg rain$ |
| ---------------- | ---------- | --------------- |
| $C = cloud$      | 0.08       | 0.32            |
| $C = \neg cloud$ | 0.02       | 0.58            |

$$
P(C = cloud)
$$
> What is the probability that it is cloudy?
$$
= P(C = cloud, R = rain) + P(C = cloud, R = \neg rain)
$$
$$
= 0.08 + 0.32
$$
$$
= 0.40
$$

## Conditioning

$$
P(a) = P(a|b)P(b) + P(a|\neg b)P(\neg b)
$$

$$
P(X=x_{i}) = \sum_{j}P(X = x_{i}|Y=y_{j})P(Y=y_{j})
$$

## Bayesian Network

data structure that represents the dependencies among random variables

- directed graph (nodes pointing in a direction)
- each node represents a random variable
- arrow from $X$ to $Y$ means $X$ is a parent of $Y$
- each node $X$ has probability distribution $\mathbf{P}(X|Parents(X))$

### Example

![example](images/bayesiannetwork.png)

Let's look at the conditional probability distribution of the $Rain$ node

| $R$     | $yes$ | $no$ |
| ------- | ----- | ---- |
| $none$  | 0.4   | 0.6  |
| $light$ | 0.2   | 0.8  |
| $heavy$ | 0.1   | 0.9  |

And then looking at two variables, we can figure out the train node, let's look at that conditioning

| $R$     | $M$   | $on\space time$ | $delayed$ |
| ------- | ----- | --------------- | --------- |
| $none$  | $yes$ | 0.8             | 0.2       |
| $none$  | $no$  | 0.9             | 0.1       |
| $light$ | $yes$ | 0.6             | 0.4       |
| $light$ | $no$  | 0.7             | 0.3       |
| $heavy$ | $yes$ | 0.4             | 0.6       |
| $heavy$ | $no$  | 0.5             | 0.5       |

And finally, $Train$

| $T$             | $attend$ | $miss$ |
| --------------- | -------- | ------ |
| $on\space time$ | 0.9      | 0.1    |
| $delayed$       | 0.6      | 0.4    |

Now let's say we want to calculate $P(light, no)$

$$
P(light)P(no|light)
$$

Or $P(light, no, delayed)$
$$
P(light)P(no|light)P(delayed|light, no)
$$

## Inference

- Query $\mathbf{X}$: variable for which to compute distribution
- Evidence variable $\mathbf{E}$: observed variables for event $e$
- Hidden variables $\mathbf{Y}$: non evidence, non-query variable
- Goal" Calculate $\mathbf{P}(\mathbf{X}|e)$

Using this, let's go back to our previous example and solve
$$
\mathbf{P}(Appointment | light, no)
$$
> $light$ and $no$ are our evidence

$$
= \alpha \mathbf{P}(Appointment, light, no)
$$
> $\alpha$ means proportional

$$
= \alpha [\mathbf{P}(Appointment, light, no, on \space time) \newline
+ \mathbf{P}(Appointment, light, no, delayed)]
$$

## Inference by Enumeration

$$
\mathbf{P}(\mathbf{X}|e) =
\alpha \mathbf{P}(\mathbf{X}, e) =
\alpha \sum_{y}\mathbf{P}(\mathbf{X}, e, y)
$$

$\mathbf{X}$ is the query variable \
$e$ is the evidence \
$y$ ranges over values of hidden variables \
$\alpha$ normalizes the result

## Approximate Inference

### Sampling

picking random values based on probability in our Bayesian Network to get quick approximations

### Likelihood Weighting

- Start by fixing the values for evidence variables
- Sample the non-evidence variables using conditional probabilities in the Bayesian Network
- Weight each sample by its likelihood: the probability of all of the evidence

## Markov Assumption

the assumption that the current state depends on only a finite fixed number of previous states

### Markov Chain

a sequence of random variables where the distribution of each variable follows the Markov assumption

### Transition Model

columns: Tomorrow ($\mathbf{X}_{t+1}$) \
rows: Today ($\mathbf{X}_{t}$)

|         | $sunny$ | $rainy$ |
| ------- | ------- | ------- |
| $sunny$ | 0.8     | 0.2     |
| $rainy$ | 0.3     | 0.7     |

### Hidden Markov Model

a Markov model for a system with hidden states that generate some observed event

### Sensor Model

columns: Observation ($\mathbf{E}_{t}$) \
rows: State ($\mathbf{X}_{t}$)

|         | $umbrellas$ | $no\space umbrellas$ |
| ------- | ----------- | -------------------- |
| $sunny$ | 0.2         | 0.8                  |
| $rainy$ | 0.9         | 0.1                  |
