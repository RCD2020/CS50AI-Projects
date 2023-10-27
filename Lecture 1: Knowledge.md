# Knowledge

## Vocab

### Knowledge-Based Agents

agents that reason by operating on internal representations of knowledge

### Sentence

an assertion about the world in a knowledge representation language

### Model

assignment of a truth value to every propositional symbol (possible word)

### Knowledge Base

a set of sentences known by a knowledge-based agent

### Entailment

*α* ⊨ *β*

in every model in which sentence *α (alpha)* is true, sentence *β (beta)* is also true.

### Model Checking

To determine if **KB** ⊨ *α*:
- Enumerate all possible models
- If in every model where **KB** is true, *α* then **KB** entails *α*
- Otherwise, **KB** does not entail *α*

### Inference

the process of deriving new sentences from old ones

### Modus Ponens

*α* → *β*

*α*

Then we know *β*

### And Elimination

*α* ∧ *β*

Then *α*

### Double Negation Elimination

¬(¬*α*)

Then *α*

### Implication Elimination

*α* → *β*

Then ¬*α* ∨ *β*

### Biconditional Elimination

*α* ↔ *β*

Then (*α* → *β*) ∧ (*β* → *α*)

### De Morgan's Law

¬(*α* ∧ *β*)

Then ¬*α* ∨ ¬*β*

¬(*α* ∨ *β*)

Then ¬*α* ∧ ¬*β*

### Distributive Law

(*α* ∧ (*β* ∨ *γ*))

Then (*α* ∧ *β*) ∨ (*α* ∧ *γ*)

(*α* ∨ (*β* ∧ *γ*))

Then (*α* ∨ *β*) ∧ (*α* ∨ *γ*)

### Theorem Proving

- Initial State: starting knowledge base
- Actions: inference rules
- Transition Model: new knowledge base after inference
- Goal Test: check statement we're trying to prove
- Path Cost Function: number of steps in proof

### Unit Resolution Rule

*P* ∨ *Q*

¬*P*

Then *Q*

*P* ∨ *Q<sub>1</sub>* ∨ *Q<sub>2</sub>* ∨ ... ∨ *Q<sub>n</sub>*

¬*P*

Then *Q<sub>1</sub>* ∨ *Q<sub>2</sub>* ∨ ... ∨ *Q<sub>n</sub>*

*P* ∨ *Q*

¬*P* ∨ *R*

Then *Q* ∨ *R*

*P* ∨ *Q<sub>1</sub>* ∨ *Q<sub>2</sub>* ∨ ... ∨ *Q<sub>n</sub>*

¬*P* ∨ *R<sub>1</sub>* ∨ *R<sub>2</sub>* ∨ ... ∨ *R<sub>m</sub>*

Then *Q<sub>1</sub>* ∨ *Q<sub>2</sub>* ∨ ... ∨ *Q<sub>n</sub>* ∨ *R<sub>1</sub>* ∨ *R<sub>2</sub>* ∨ ... ∨ *R<sub>m</sub>*

### Clause

a disjunction of literals

*e.g. *P* ∨ *Q* ∨ *R**

### Conjunctive Normal Form

logical sentence that is a conjunction of clauses

*e.g. (A ∨ B ∨ C) ∧ (D ∨ ¬E) ∧ (F ∨ G)*

### Conversion to CNF

- Elminate biconditionals
    - turn (*α* ↔ *β*) into (*α* → *β*) ∧ (*β* → *α*)
- Eliminate implications
    - turn (*α* → *β*) into ¬*α* ∨ *β*
- Move ¬ inwards using De Morgan's Law
    - e.g. ¬(*α* ∧ *β*) into ¬*α* ∨ ¬*β*
- Use distributive law to distribute ∨ wherever possible

(*P* ∨ *Q*) → *R*
>Eliminate implication

¬(*P* ∧ *Q*) ∨ *R*
> De Morgan's Law

(¬*P* ∧ ¬*Q*) ∨ *R*
> Distributive Law

(¬*P* ∨ *R*) ∧ (¬*Q* ∨ *R*)

### Inference by Resolution

*P* ∨ *Q*

¬*P* ∨ *R*

Then (*Q* ∨ *R*)

*P* ∨ *Q* ∨ *S*

¬*P* ∨ *R* ∨ *S*

Then (*Q* ∨ *S* ∨ *R* ~~∨ *S*~~)
> We can eliminate the extra *S* by factoring

To determine if **KB** ⊨ *α*:
- Check if (**KB** ∧ ¬*α*) is a contradiction
    - If so, then **KB** ⊨ *α*
    - Otherwise, no entailment
- Convert (**KB** ⊨ *α*) to Conjunctive Normal Form
- Keep checking to see if we can use resolution to produce a new clause
    - If ever we produce the empty clause (equivalent to False), we have a contradiction, and **KB** ⊨ *α*
    - Otherwise, if we can't add new clauses, no entailment


## Propositional Logic

Propositional Logic makes use of Propositional Symbols that represents facts about the world

And then using Logical Connectives we can link together symbols.

| Symbol | Meaning | Description
| ------ | ------- | -----------
| ¬      | Not     | ¬P, only true if opperand is False
| ∧      | And     | P ∧ Q, only true if both opperands are true
| ∨      | Or      | P ∨ Q, only true if one or more of opperands are true
| →      | Implication | P → Q, if P is true, then it makes the implication that Q is true, meaning if Q is true, the outputs true, if Q is false, outputs false, but is P is false, always outputs true because no implication was made
| ↔      | Biconditional | P ↔ Q, opperands imply each other, so only true if both opperands are the same value

### Example

- *P*: It is a tuesday
- *Q*: It is raining
- *R*: Harry will go for a run

**KB** (knowledge base): (*P* ∧ ¬*Q*) → *R*
> P and not Q implies R

Additional Info: *P* ¬*Q*
> P is true, and Q is not true

Using this, we know that *R* is true


## First-Order Logic

### Universal Quantification

**∀** = for all symbol

**∀***x.BelongsTo(*x*, Gryffindor) →*

*¬BelongsTo(x, Hufflepuff)*

> For all objects x, if x belongs to Gryffindor, then x does not belong to Hufflepuff

> Anyone in Gryffindor is not in Hufflepuff

### Existential Quantification

**∃** = exists

**∃***x.House(x)* ∧ *BelongsTo(Minerva, x)*
> There exists an object x sunb that x is a house and Minerva belongs to x

> Minerva belongs to a house

**∀***x.Person(x) → (* **∃** *.House(y)* ∧ *BelongsTo(x, y))*
> For all objects x, if x is a person, them there exists an object y such that y is a house and x belongs to y

> Every person belongs to a house