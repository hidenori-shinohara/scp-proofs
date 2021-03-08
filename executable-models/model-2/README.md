This directory contains a model for a very simple FBAS.

# Description of the network

* There are four nodes.
* In other words, any set of 3 nodes is a quorum slice as long as it contains the node.
* There is no Byzantine failure.

# How to use this
There are three ways to use this model. Executable model, fuzz testing, and verification.

1. Executable model.
    * Run `make && ./executable` to start a REPL environment.
      You can invoke actions to manually examine the model.
      For instance, `node.vote(0, 1)` makes node 0 vote for statement 1.
2. Fuzz testing
    * Run `make && ./fuzz`.
      Ivy randomly generates a sequence of actions.
      You can pass the seed as a command line argument. (e.g., `./fuzz seed=123`)
3. Formal verification
    * Run `make proof` and Ivy verifies that the invariants specified in `proof.ivy` hold after initialization and any exported actions.
