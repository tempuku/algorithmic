from __future__ import annotations

from typing import Dict, Any, List, Optional


class TreeNode:
    children: List[TreeNode]

    def __init__(self, id: int, children: List[TreeNode] = None, data: Dict[str, Any] = None):
        if children is None:
            self.children = []
        if data is None:
            self.data = {}
        self.id = id

    def __repr__(self):
        return f'TreeNode {self.id}'


def bfs_iterating(root_node: TreeNode):
    if root_node.children is None:
        yield root_node

    stack = [root_node]

    while stack:
        node = stack.pop(0)
        yield node
        stack.extend(node.children)


def dfs_iterating(root_node: TreeNode):
    if root_node.children is None:
        yield None

    yield root_node
    for child_node in root_node.children:
        for node in dfs_iterating(child_node):
            yield node


if __name__ == '__main__':
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    root.children = [node1, node2]
    node1.children = [node3, node4]

    iter1 = list(bfs_iterating(root))
    iter2 = list(dfs_iterating(root))
    print(iter1, iter2)
