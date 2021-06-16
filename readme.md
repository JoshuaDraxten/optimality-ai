# Optimality AI

Can machine learning be reduced to sorting an array?

## Background

In linguistics there's this theory called [Optimality Theory](https://en.wikipedia.org/wiki/Optimality_theory) which describes how our brains structure phonological rules. The basic idea is that every human is born with the same language constraints, and language aquisition is a process of ordering those constraints into what's more important than the others.

- Generator
- Constrains
- Evaluator

## Oportunity

We can create a machine learning example by defining a generator function and specifying a function to define the constraints. We then want a fourth part, this will be function that sorts which constraints are more important than the other ones. We do this by showing the algorithm a situation, and then giving it the ideal output.

## This example

## Differences with Neural Networks

Neural networks are good for statistically correct decisions that find features automatically

Optimality could be used for reproducing functions that you can simulate without understanding. Possibly for describing what Neural nets are doing

## Learning function

The learning function has access to two things: All previous games played and the constraints functions

```
if (current constraints make us do the previous move):
    check previous move
else:
    sort moves so that they do
```

## Possible things to try

- Automatically inversing constraint functions when useful
