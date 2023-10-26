# Lecture 0: Intro to AI

## Vocab

### Agent
entity that perceives its environment and acts upon that environment

### State
a configuration of the agent and its environment

### Initial State
the state in which the agent begins

### Actions
choices that can be made in a state

we can think of actions as a function, where we give it a state, and then a list of actions that are valid in that state will be returned

### Transition Model
a description of what state results from performing any applicable action in any state

we can think of the transition model again as a function, where we give it a state and an action, and it will return the state that results from the given action in the given state

### State Space

the set of all states reachable from the initial state by any sequence of actions

### Goal Test

way to determine whether a given state is a goal state

### Path Cost

numerical cost associated with a given path

### Search Problems

using all of these concepts together, we define what is called a search problem, that takes an initial state, generates actions, perform those actions through a transition model, validates whether it helps us with a goal test, and then optimizes using the path cost

### Solution

a sequence of actions that leads from the initial state to a goal state

### Optimal Solution

a solution that has the lowest path cost among all solutions

### Node

a data structure that keeps track of
- a state
- a parent (node that generated this node)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)

### Stack

last-in first-out data type

### Depth-First Search

search algorithm that always expands the deepest node in the frontier

### Breadth-First Search

search algorithm that always expands the shallowest node in the frontier

### Queue

first-in first-out data type

### Uninformed Search

search strategy that uses no problem-specific knowledge

### Informed Search

search strategy that uses problem-specific knowledge to find solutions mode efficiently

### Greedy Best-First Search

search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function *h(n)*

### A* search

search algorithm that expands node with lowest value of *g(n) + h(n)*

- *g(n)* = cost to reach node
- *h(n)* = estimated cost to goal

optimal if
- *h(n)* is admissible (never overestimates the true cost)
- *h(n)* is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c)

### Minimax

- Max aims to maximize score
- Min aims to minimize score




## Approach

How do we approach solving this problems?

We can first start at one state, and then explore from there

We can keep track of all the options by grouping them into a data structure called a Frontier

- Start with a frontier that contains the initial state
- Repeat
    - If the frontier is empty, then no solution
    - Remove a node from the frontier
    - If node contains goal state, return the solution
    - Expand node, add resulting nodes to the frontier


## Revised Approach

In this revised approach, we can check different paths

- Start with a frontier that contains the intiial state
- Start with an empty explored set
- Repeat
    - If the frontier is empty, then no solution
    - Remove a node from the frontier
    - If node contains goal state, return the solution
    - Add the node to the explored set
    - Expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set

