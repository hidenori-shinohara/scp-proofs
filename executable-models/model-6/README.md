This directory contains a model for a relatively general FBAS possibly containing Byzantine nodes.

Run `make proof` and Ivy verifies that the invariants specified in `proof.ivy` hold after initialization and any exported actions.

# Abstractions

The abstractions used in this model are heavily influenced by, if not identical to, what is described in https://github.com/stellar/scp-proofs#the-model.

More specifically,

1. The intersection of two quorums of intertwined nodes contains a well-behaved node.
1. The intersection of two quorums of intact nodes contains an intact node.
1. The set of intact nodes is a quorum.
1. If `Q` is a quorum of an intact node and if all members of `Q` have accepted `val`, then either all intact nodes have accepted `val`, or there is an intact node `n` such that `n` has not accepted `val` and `n` is blocked by a set of intact nodes that have all accepted `val`.
1. If an intact node is blocked by a set of nodes S, then S contains an intact node.

Note that 1-3 and 5 have been copied and pasted from the [the abstractions used by Giuliano Losa](https://github.com/stellar/scp-proofs#the-model), and the 4th one is almost identical.

Here is a proof that any FBAS with quorum intersection satisfies 4:

## Proof of 4

Let `Q` be a quorum containing an intact node.
Suppose that all members of `Q` have accepted `val`.
Let `S` be the set of all nodes that have accepted `val`.
Clearly, `Q ⊆ S`.

Define
* `S⁺ = S \ B` (the set of intact nodes in `S`)
* `S⁻ = (V \ S) \ B` (the set of intact nodes _not_ in `S`)

By Theorem 10 on P.16 of [The Stellar Consensus Protocol: A Federated Model for Internet-level Consensus](https://www.stellar.org/papers/stellar-consensus-protocol) (the white paper), we conclude that:

* `S⁻` is empty, _or_
  * This happens if and only if _all_ intact nodes are in `S`.
    Since we defined `S` to be the set of all nodes that have accepted `val`, we conclude that all intact nodes have accepted `val`.
* There exists `n ∈ S⁻` such that `S⁺` is `n`-blocking.
  * Since `S⁻` is the set of intact nodes _not_ in `S`, `n` is intact.
    Furthermore, since `n` is not in `S`, `n` has not accepted `val`.
    Finally, `S⁺` is exactly _the_ set of intact nodes that have accepted `val`.
    Therefore, we can conclude that there is an intact node `n` such that `n` has not accepted `val` and `n` is blocked by _a_ set of intact nodes that have all accepted `val`.
    (Note that the last sentence is slightly weaker than what we could say. However, it is unnecessary for this abstraction.)

Therefore, the 4th statement is always satisfied by any FBAS with quorum intersection.
