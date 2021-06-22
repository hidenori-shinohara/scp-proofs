This directory contains a model for an FBAS possibly containing Byzantine nodes.

Run `make proof` and Ivy verifies that the invariants specified in `proof.ivy` hold after initialization and any exported actions.

# Abstractions

The abstractions used in this model are heavily influenced by, if not identical to, the [the abstractions used by Giuliano Losa](https://github.com/stellar/scp-proofs#the-model).

More specifically, we will consider any set of nodes with the notion of quorums, blocking sets, and intact nodes that satisfy the axioms:

1. Intact nodes are well-behaved.
1. The intersection of two quorums of intact nodes contains an intact node.
1. The set of intact nodes is a quorum.
1. [Cascade theorem] If `U` is a quorum of an intact node and if all intact members of `U` have accepted `val`, then either all intact nodes have accepted `val`, or there is an intact node `n` such that `n` has not accepted `val` and `n` is blocked by a set of intact nodes that have all accepted `val`.
1. If an intact node is blocked by a set of nodes `S`, then `S` contains an intact node.

And we consider any set `V` that satisfies the 5 statements above.

It is important to emphasize that we consider any configuration as long as they satisfy the statements above, and we do not consider other concepts.
Specifically, quorums are not defined in terms of quorum slices and any sets can block any nodes as long as they satisfy the 5 axioms.

Of course, this abstraction makes sense only if all the statements above are indeed in correct in the white paper, and the following is a sketch of a proof for each.

# Proofs

## Intact nodes are well-behaved.

This is true by the definition of intactness.

## The intersection of two quorums of intact nodes contains an intact node.

Due to quorum intersection, the set of befouled nodes, B, is a DSet by Theorem 3.
Thus, the given FBAS enjoys quorum intersection despite B.
In other words, the intersection of two quorums of intact nodes contains an intact node.

## The set of intact nodes is a quorum.

Since `B` is a DSet, the given FBAS enjoys quorum availability despite `B`.
In other words, `V = B` or `V \ B` is a quorum in `<V, Q>`.
In each case, `V \ B` is a quorum.

## Cascade theorem

This is similar to Theorem 10, and the proof for Theorem 10 directly proves this since the proof only uses the fact that `(U \ B) ⊂ S` (TODO: Make sure that my understanding is correct)

## If an intact node is blocked by a set of nodes `S`, then `S` contains an intact node.

Let `v` be an intact node.
`V \ B` is a quorum of `v` since the given FBAS enjoys quorum availability despite `B`.
Thus `v` has a quorum slice that consists only of intact nodes.
Therefore, any `v`-blocking set must contain befouled nodes.

