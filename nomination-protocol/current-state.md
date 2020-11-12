# Goal

My current goal is to prove that *once all messages have been delivered, every node will have confirmed the exact same thing*.

In IVy, I wrote it as:

```
# Try to prove that once all the messages have been delivered,
# every node will have confirmed the exact same nomination statements.
# Again, IVy can't seem to prove this.
invariant [eventually_same_candidate_set]
    (forall SRC, DST, VALUE.
        (have_broadcast_vote(SRC, VALUE) -> have_delivered_vote(SRC, DST, VALUE)) &
        (have_broadcast_accept(SRC, VALUE) -> have_delivered_accept(SRC, DST, VALUE)))
    -> (forall NODE1, NODE2, VALUE. nodes(NODE1).spec.have_confirmed(VALUE) -> nodes(NODE2).spec.have_confirmed(VALUE))
```

in `network.ivy`.

# Adding "preliminary" invariants 

When I ask IVy to just prove the invariant `[eventually_same_candidate_set]` after commenting out all other invariants, I get the following CTI:


```
    The following set of external actions must preserve the invariant:
        (internal) ext:net.intf.broadcast_accept
            network.ivy: line 139: net.spec.eventually_same_candidate_set ... PASS
        (internal) ext:net.intf.deliver_accept
            network.ivy: line 139: net.spec.eventually_same_candidate_set ... FAIL
searching for a small model... done
[
    net.intf.nset.member(0,0) = true
    net.intf.nset.member(1,0) = true
    net.spec.have_delivered_vote(0,0,0) = false
    net.spec.have_delivered_vote(0,1,0) = false
    net.spec.have_delivered_vote(1,0,0) = false
    net.spec.have_delivered_vote(1,1,0) = false
    nodes.spec.have_voted(0,0) = false
    nodes.spec.have_voted(1,0) = false
    nodes.spec.heard_vote(0,0,0) = false
    nodes.spec.heard_vote(0,1,0) = false
    nodes.spec.heard_vote(1,0,0) = false
    nodes.spec.heard_vote(1,1,0) = false
    net.intf.is_quorum(0) = true
    net.spec.have_broadcast_vote(0,0) = false
    net.spec.have_broadcast_vote(1,0) = false
    net.intf.nset.universe = 0
    net.spec.have_broadcast_accept(1,0) = true
    net.spec.have_broadcast_accept(0,0) = false
    nodes.spec.heard_accept(0,0,0) = false
    nodes.spec.heard_accept(0,1,0) = false
    nodes.spec.heard_accept(1,0,0) = false
    nodes.spec.heard_accept(1,1,0) = false
    nodes.spec.have_accepted(0,0) = false
    nodes.spec.have_accepted(1,0) = false
    net.spec.have_delivered_accept(0,0,0) = true
    net.spec.have_delivered_accept(0,1,0) = true
    net.spec.have_delivered_accept(1,0,0) = true
    net.spec.have_delivered_accept(1,1,0) = false
    nodes.spec.have_confirmed(0,0) = true
    nodes.spec.have_confirmed(1,0) = false
    nodes.spec.have_candidate_value(0) = false
    nodes.spec.have_candidate_value(1) = false
]
call net.intf.deliver_accept

{
    [
        fml:src = 1
        fml:value = 0
        fml:dst = 1
    ]
    network.ivy: line 81: assume net.spec.have_broadcast_accept(fml:src,fml:value)

    network.ivy: line 83: assume ~net.spec.have_delivered_accept(fml:src,fml:dst,fml:value)

    network.ivy: line 86: call ext:nodes.intf.recv_accept(fml:dst, fml:src, fml:value)
    {
        [
            fml:value_a = 0
            prm:ID = 1
            fml:src_a = 1
        ]
        node.ivy: line 94: nodes.spec.heard_accept(prm:ID,fml:src,fml:value) := true

        [
            nodes.spec.heard_accept(1,1,0) = true
        ]
    }

    network.ivy: line 87: net.spec.have_delivered_accept(fml:src,fml:dst,fml:value) := true

    [
        net.spec.have_delivered_accept(1,1,0) = true
    ]
}
```

This CTI starts with the following (seemingly counterintuitive) condition:

* `net.spec.have_broadcast_accept(1,0) = true` says Node 1 broadcast that it accepted Value 0.
* `nodes.spec.have_accepted(1,0) = false` says Node 1 has not accepted Value 0.

The only two places in the code where we modify `net.spec.have_broadcast_accept` are the initialization and the `intf.broadcast_accept` function. 
* The initialization sets `have_broadcast_accept(1, 0) = false`.
* `broadcast_accept(src, value)` is only called if `nodes(src).spec.have_accepted(value)`.

Of course, it is still possible that I made a mistake somewhere, but based on this, it really seems that the CTI starts with an unreachable state.

Thus I added the invariant `have_broadcast_accept(NODE, VALUE) -> nodes(NODE).spec.have_accepted(VALUE) `. (`network.ivy`)
Then IVy stops showing CTIs that contain such unreachable states (i.e., a state where some node has accepted a value even though no node voted for it).
But IVy still shows CTIs that start with (seemingly) unreachable states.

So, I kept adding (seemingly trivial) invariants in order to prevent IVy from coming up with CTIs that start with unreachable states.

# The CTI to the invariant that I'm trying to prove

After adding "preliminary" invariants, I get the following CTI:


```
    The following set of external actions must preserve the invariant:
        (internal) ext:net.intf.broadcast_accept
            network.ivy: line 97: net.spec.invar22 ... PASS
            network.ivy: line 99: net.spec.invar23 ... PASS
            network.ivy: line 102: net.spec.invar24 ... PASS
            network.ivy: line 103: net.spec.invar25 ... PASS
            network.ivy: line 106: net.spec.invar26 ... PASS
            network.ivy: line 108: net.spec.invar27 ... PASS
            network.ivy: line 110: net.spec.invar28 ... PASS
            network.ivy: line 111: net.spec.invar29 ... PASS
            network.ivy: line 114: net.spec.invar30 ... PASS
            network.ivy: line 116: net.spec.invar31 ... PASS
            network.ivy: line 141: net.spec.eventually_same_candidate_set ... PASS
        (internal) ext:net.intf.deliver_accept
            network.ivy: line 97: net.spec.invar22 ... PASS
            network.ivy: line 99: net.spec.invar23 ... PASS
            network.ivy: line 102: net.spec.invar24 ... PASS
            network.ivy: line 103: net.spec.invar25 ... PASS
            network.ivy: line 106: net.spec.invar26 ... PASS
            network.ivy: line 108: net.spec.invar27 ... PASS
            network.ivy: line 110: net.spec.invar28 ... PASS
            network.ivy: line 111: net.spec.invar29 ... PASS
            network.ivy: line 114: net.spec.invar30 ... PASS
            network.ivy: line 116: net.spec.invar31 ... PASS
            network.ivy: line 141: net.spec.eventually_same_candidate_set ... FAIL
searching for a small model... done
[
    net.intf.nset.member(0,0) = true
    net.intf.nset.member(1,0) = true
    net.spec.have_delivered_vote(1,0,0) = true
    net.spec.have_delivered_vote(1,1,0) = true
    net.spec.have_delivered_vote(0,0,0) = false
    net.spec.have_delivered_vote(0,1,0) = false
    net.intf.is_quorum(0) = true
    nodes.spec.have_voted(0,0) = true
    nodes.spec.have_voted(1,0) = true
    nodes.spec.heard_vote(0,1,0) = true
    nodes.spec.heard_vote(1,1,0) = true
    nodes.spec.heard_vote(0,0,0) = false
    nodes.spec.heard_vote(1,0,0) = false
    net.spec.have_broadcast_vote(1,0) = true
    net.spec.have_broadcast_vote(0,0) = false
    net.intf.nset.universe = 0
    net.spec.have_broadcast_accept(1,0) = true
    net.spec.have_broadcast_accept(0,0) = false
    nodes.spec.heard_accept(0,1,0) = true
    nodes.spec.heard_accept(0,0,0) = false
    nodes.spec.heard_accept(1,0,0) = false
    nodes.spec.heard_accept(1,1,0) = false
    nodes.spec.have_accepted(0,0) = true
    nodes.spec.have_accepted(1,0) = true
    net.spec.have_delivered_accept(1,0,0) = true
    net.spec.have_delivered_accept(0,0,0) = false
    net.spec.have_delivered_accept(0,1,0) = false
    net.spec.have_delivered_accept(1,1,0) = false
    nodes.spec.have_confirmed(1,0) = true
    nodes.spec.have_confirmed(0,0) = false
    nodes.spec.have_candidate_value(0) = false
    nodes.spec.have_candidate_value(1) = false
]
call net.intf.deliver_accept

{
    [
        fml:src = 1
        fml:value = 0
        fml:dst = 1
    ]
    network.ivy: line 81: assume net.spec.have_broadcast_accept(fml:src,fml:value)

    network.ivy: line 83: assume ~net.spec.have_delivered_accept(fml:src,fml:dst,fml:value)

    network.ivy: line 86: call ext:nodes.intf.recv_accept(fml:dst, fml:src, fml:value)
    {
        [
            fml:value_a = 0
            prm:ID = 1
            fml:src_a = 1
        ]
        node.ivy: line 94: nodes.spec.heard_accept(prm:ID,fml:src,fml:value) := true

        [
            nodes.spec.heard_accept(1,1,0) = true
        ]
    }

    network.ivy: line 87: net.spec.have_delivered_accept(fml:src,fml:dst,fml:value) := true

    [
        net.spec.have_delivered_accept(1,1,0) = true
    ]
}
```

This CTI contains only two nodes and one statement:
* The only quorum is {V_0, V_1}.
* V_0, V_1 both voted and accepted x.
* V_0 knows that V_1 voted and accepted x.
* V_1 confirmed x.
* The message that V_1 voted was also delivered to V _1.

```
+------------------------------------------------------------------+
|     V_0                             V_1                          |
|                                                                  |
|   voted x    <---delivered----    voted x   <-----------------+  |
|                                      |                        |  |
|                                      |                        |  |
|                                      +--delivered to itself---+  |
|                                                                  |
|                                                                  |
|  accepted x  <---delivered----   accepted x                      |
|                                                                  |
|                                                                  |
|                                                                  |
|                                  confirmed x                     |
+------------------------------------------------------------------+
```

The CTI says that after the message that says V_1 accepted x has been delivered V_1, all broadcast messages will have been delivered to everyone.
So, IVy would expect that V_0 and V_1 will have confirmed the same set of values.
However, that is not the case because V_0 will not have confirmed x.

The problem with this CTI is that V_1 cannot have accepted or confirmed x because no message has been delivered from V_0.
This is less obvious than any of the previous CTIs, but, once again, it seems to start with an unreachable state.
This leads to the following problem...

# The problem I can't solve

The last CTI suggests that I need to add a new invariant such as:
* If v has accepted x, either
    * there exists a quorum containing v in which every node either voted or accepted x, or
    * there exists a v-blocking set in which every node accepted x.
* If v has confirmed x, then there exists a quorum containing v in which every node accepted x.

(Essentially, just the definition of accepting and confirming in the white paper)

Both of them contain `forall NODE, VALUE. exists QUORUM`.
Because of skolemization, IVy generates a function whose signature is `NODE -> VALUE -> QUORUM`.
On the other hand, I do need the FBAS to enjoy quorum intersection, so I have

```
forall S1, S2. (is_quorum(S1) & is_quorum(S2)) -> (exists V. nset.member(V, S1) & nset.member(V, S2))
```

which, because of skolemization, leads to a function whose signature is `QUORUM -> QUORUM -> NODE`.
These two functions may result in an infinite cycle and the message "The following terms may generate an infinite sequence of instantiations" and this would put me in an undecidable fragment.
