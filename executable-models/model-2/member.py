nodeCount = 3

def isMajority(bitmask):
    return 2 * bin(bitmask).count("1") > nodeCount
def contains(bitmask, node):
    return ((bitmask >> node) & 1) == 1

members = []
for nodeId in range(nodeCount):
    for setId in range(1<<nodeCount):
        if contains(setId, nodeId):
            members.append("(X=v{}&S={})".format(nodeId, setId))

quorums = []
for setId in range(1<<nodeCount):
    if isMajority(setId):
        quorums.append("(S={})".format(setId))

v_blocking_pairs = []
for nodeId in range(nodeCount):
    for setId in range(1<<nodeCount):
        if not contains(setId, nodeId) and not isMajority(setId):
            # If the set does NOT the node AND the set is NOT the majority,
            # such a set is NOT v-blocking.
            v_blocking_pairs.append("(X=v{}&S={})".format(nodeId, setId))

template = """\
    relation member(X:id_t, S:set_t)
    definition member(X:id_t, S:set_t) = {}

    relation is_quorum(S:set_t)
    definition is_quorum(S:set_t) = {}

    relation is_v_blocking(X:id_t, S:set_t)
    definition is_v_blocking(X:id_t, S:set_t) = ~({})"""

print(template.format("|".join(members), "|".join(quorums), "|".join(v_blocking_pairs)))
