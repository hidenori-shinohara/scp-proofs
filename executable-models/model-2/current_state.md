* `make proof` fails and shows a CTI.
  But I'm not quite sure how to proceed.

```
    The following set of external actions must preserve the invariant:
        (internal) ext:network.deliver_accept
            proof.ivy: line 12: heard_vote_implies_voted ... PASS
            proof.ivy: line 15: heard_accept_implies_accepted ... PASS
            proof.ivy: line 18: accept_means_at_least_one_vote ... PASS
            proof.ivy: line 21: if_node_is_ready_to_accept_it_must_accept ... PASS
            proof.ivy: line 24: if_node_is_ready_to_confirm_it_must_confirm ... PASS
            proof.ivy: line 27: accepted_implies_node_heard_itself_accept ... PASS
            proof.ivy: line 30: voted_implies_node_heard_itself_vote ... PASS
            proof.ivy: line 33: confirmed_implies_it_heard_at_least_one_node_accept ... PASS
            proof.ivy: line 36: accepted_implies_at_least_one_node_voted ... PASS
            proof.ivy: line 39: confirmed_implies_accepted ... PASS
            proof.ivy: line 42: confirmed_implies_there_exists_quorum_accepting_value ... PASS
            proof.ivy: line 46: heard_quorum_accept_implies_confirmed ... PASS
            proof.ivy: line 53: confirm_same_after_sufficient_messages ... FAIL
searching for a small model... done
[
    0:val_t = 0
    4:set_t = 4
    node.is_quorum(3) = true
    node.is_quorum(5) = true
    node.is_quorum(7) = true
    node.is_quorum(6) = true
    node.is_quorum(0) = false
    node.is_quorum(2) = false
    node.is_quorum(4) = false
    node.is_quorum(1) = false
    7:set_t = 7
    5:set_t = 5
    6:set_t = 6
    0:set_t = 0
    2:set_t = 2
    3:set_t = 3
    @VAL = 1
    1:set_t = 1
    1:val_t = 1
]
call network.deliver_accept

{
    [
        fml:src = v2
        fml:v = 1
        fml:dst = v0
    ]
    network.ivy: line 16: assume node.accepted(fml:src,fml:v)

    network.ivy: line 17: assume ~node.heard_accept(fml:dst,fml:src,fml:v)

    network.ivy: line 18: call node.recv_accept(fml:dst, fml:src, fml:v)
    {
        [
            fml:val = 1
            fml:src_a = v2
            fml:self_id = v0
        ]
        node.ivy: line 110: node.heard_accept(fml:self_id,fml:src,fml:val) := true

        node.ivy: line 116: node.confirmed(fml:self_id,fml:val) := true

    }

}
```

    I'm not quite sure what to make out of this.
    I'm very puzzled since the prestate contains so few relations and it feels that it's just not showing a lot of the values that I'd like to know. (e.g., whether each node has voted/accepted each statement.)

Some observations/guesses...

* Maybe, with `trace=true`, Ivy prints relations only if they are used in the CTI, and somehow in this `deliver_accept` we never used any of `voted, accepted, confirmed, heard_vote, heard_accept`.
* Upon `deliver_accept`, the node confirms the value, so the condition to confirm must have been met.
* I wonder if changing `bv[0]` to `{v0, v1, v2}` means something in formal verification that I don't know about.
