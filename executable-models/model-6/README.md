This directory contains a model for an FBAS possibly containing Byzantine nodes.

Run `make proof` and Ivy verifies that the invariants specified in `proof.ivy` hold after initialization and any exported actions.

# Abstractions

The abstractions used in this model are heavily influenced by, if not identical to, the [the abstractions used by Giuliano Losa](https://github.com/stellar/scp-proofs#the-model).

More specifically, we will consider any set of nodes with the notion of quorums, blocking sets, intact nodes, and intertwined nodes that follow:

1. Intertwined nodes are well-behaved.
1. Intact nodes are intertwined.
1. The intersection of two quorums of intertwined nodes contains a well-behaved node.
1. The intersection of two quorums of intact nodes contains an intact node.
1. The set of intact nodes is a quorum.
1. [Cascade theorem] If `U` is a quorum of an intact node and if all intact members of `U` have accepted `val`, then either all intact nodes have accepted `val`, or there is an intact node `n` such that `n` has not accepted `val` and `n` is blocked by a set of intact nodes that have all accepted `val`.
1. If an intact node is blocked by a set of nodes `S`, then `S` contains an intact node.

It is important to emphasize that we consider any configuration as long as they satisfy the statements above, and we do not consider other concepts such as quorum slices.

Of course, this abstraction makes sense only if all the statements above are indeed in correct in the white paper.

# Proofs

## Intertwined nodes are well-behaved.

The term _intertwined_ is not defined in the white paper, but it is defined in [Fast and secure global payments with Stellar](http://www.scs.stanford.edu/~dm/home/papers/lokhava:stellar-core.pdf) and [Simplified SCP](https://www.scs.stanford.edu/~dm/blog/simplified-scp.html).
However, for the purpose of this abstraction, we turn this into a node's property by defining

> A non-faulty node `v` is intertwined if and only if all of its quorums intersect any quorum of any non-faulty node.

TODO: make sure that this is indeed correct

By definition, intertwined nodes must be well-behaved.

## Intact nodes are intertwined.

Due to quorum intersection, the set of befouled nodes, `B`, is a DSet by Theorem 3.
Thus, the given FBAS enjoys quorum intersection despite `B`.
In other words, the intersection of two quorums of intact nodes contains an intact node.
Since an intact node is by definition well-behaved, any intact nodes are intertwined.

## The intersection of two quorums of intertwined nodes contains a well-behaved node.

This is the definition of intertwined nodes.

## The intersection of two quorums of intact nodes contains an intact node.

We showed this under "Intact nodes are intertwined."

## The set of intact nodes is a quorum.

Due to quorum intersection, the set of befouled nodes, `B`, is a DSet by Theorem 3.
Thus, the given FBAS enjoys quorum availability despite `B`.
In other words, `V = B` or `V \ B` is a quorum in `<V, Q>`.
In each case, `V \ B` is a quorum.

## Cascade theorem

This is similar to Theorem 10, and the proof for Theorem 10 directly proves this since the proof only uses the fact that `(U \ B) ⊂ S` (TODO: Make sure that my understanding is correct)

## If an intact node is blocked by a set of nodes `S`, then `S` contains an intact node.

As mentioned above, the given FBAS enjoys quorum availability despite `B`.
Let `v` be an intact node.
Then `V \ B` is a quorum of `v`.
Thus `v` has a quorum slice that consists only of intact nodes.
Therefore, any `v`-blocking set must contain befouled nodes.

