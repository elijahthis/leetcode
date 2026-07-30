package main

/**
 * Definition for a Node.
 */
type Node struct {
	Val       int
	Neighbors []*Node
}

func cloneGraph(node *Node) *Node {
	oldToNew := make(map[*Node]*Node)

	var dfs func(*Node) *Node
	dfs = func(old *Node) *Node {
		if clone := oldToNew[old]; clone != nil {
			return clone
		}
		clone := &Node{
			Val: old.Val,
		}
		oldToNew[old] = clone

		for _, nei := range old.Neighbors {
			clone.Neighbors = append(clone.Neighbors, dfs(nei))
		}

		return clone
	}

	if node != nil {
		return dfs(node)
	}
	return nil
}
