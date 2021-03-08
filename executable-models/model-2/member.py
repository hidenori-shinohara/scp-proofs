nodeCount = 4

def isMajority(bitmask):
    return 2 * bin(bitmask).count("1") > nodeCount
def contains(bitmask, node):
    return ((bitmask >> node) & 1) == 1

member = """\
    relation member(X:id_t, S:set_t)
    definition member(X:id_t, S:set_t) ="""
    
is_quorum = """\
    relation is_quorum(S:set_t)
    definition is_quorum(S:set_t) ="""
    
is_v_blocking = """\
    relation is_v_blocking(X:id_t, S:set_t) 
    definition is_v_blocking(X:id_t, S:set_t) ="""

members = []
for nodeId in range(nodeCount):
    for setId in range(1<<nodeCount):
        if contains(setId, nodeId):
            members.append("(X={}&S={})".format(nodeId, setId))
print(member)
print("      " + "|".join(members))
print()

quorums = []
for setId in range(1<<nodeCount):
    if isMajority(setId):
        quorums.append("(S={})".format(setId))
print(is_quorum)
print("      " + "|".join(quorums))
print()

v_blocking_pairs = []
for nodeId in range(nodeCount):
    for setId in range(1<<nodeCount):
        if contains(setId, nodeId) or isMajority(setId):
            # If the set contains the node AND/OR the set is the majority,
            # such a set is v-blocking.
            v_blocking_pairs.append("(X={}&S={})".format(nodeId, setId))
print(is_v_blocking)
print("      " + "|".join(v_blocking_pairs))
