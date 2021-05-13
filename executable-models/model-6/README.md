This directory contains a model for a relatively general FBAS possibly containing Byzantine nodes.

Run `make proof` and Ivy verifies that the invariants specified in `proof.ivy` hold after initialization and any exported actions.

# Abstractions

The abstractions used in this model are heavily influenced by, if not identical to, the [the abstractions used by Giuliano Losa](https://github.com/stellar/scp-proofs#the-model).

More specifically,

1. The intersection of two quorums of intertwined nodes contains a well-behaved node.
1. The intersection of two quorums of intact nodes contains an intact node.
1. The set of intact nodes is a quorum.
1. If `Q` is a quorum of an intact node and if all intact members of `Q` have accepted `val`, then either all intact nodes have accepted `val`, or there is an intact node `n` such that `n` has not accepted `val` and `n` is blocked by a set of intact nodes that have all accepted `val`.
1. If an intact node is blocked by a set of nodes S, then S contains an intact node.

# Explanation to the abstractions


TODO
* Define intertwined
* Prove the 4th one since it's slightly different from the one in the white paper

