import copy
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def tree_to_array(cls, tree) -> List:
        if tree is None:
            return [None]

        prev_nodes = None
        curr_nodes = [tree]
        result = []

        while len(curr_nodes) > 0:
            prev_nodes = curr_nodes
            curr_nodes = []

            for node in prev_nodes:
                if node is None:
                    result.append(None)
                    continue

                result.append(node.val)

                if node.left is None and node.right is None:
                    continue

                curr_nodes.append(node.left)
                curr_nodes.append(node.right)

        if result[-1] is None:
            result = result[: -1]

        return result


class Solution:
    @classmethod
    def bst_insert(cls, tree: TreeNode, val: int) -> List[TreeNode]:
        if tree is None:
            return TreeNode(val)

        new_tree = copy.deepcopy(tree)
        prev_node = None
        curr_node = new_tree

        while curr_node is not None:
            prev_node = curr_node
            if val < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if val < prev_node.val:
            prev_node.left = TreeNode(val)
        else:
            prev_node.right = TreeNode(val)

        return new_tree

    @classmethod
    def bst_equal(cls, tree1, tree2) -> bool:
        if tree1 is None and tree2 is None:
            return True

        if (tree1 is None and tree2 is not None) or \
           (tree2 is None and tree1 is not None):
            return False

        node1_togo = [tree1]
        node2_togo = [tree2]

        while len(node1_togo) > 0:
            node1 = node1_togo.pop(0)
            node2 = node2_togo.pop(0)

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            node1_togo.append(node1.left)
            node2_togo.append(node2.left)
            node1_togo.append(node1.right)
            node2_togo.append(node2.right)

        return True

    @classmethod
    def generate_trees(cls, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        prev_trees = None
        curr_trees = [None]
        prev_elems_list = None
        curr_elems_list = [[]]

        for _ in range(n):
            prev_trees = curr_trees
            curr_trees = []
            prev_elems_list = curr_elems_list
            curr_elems_list = []

            for idx, tree in enumerate(prev_trees):
                for val in range(1, n + 1):
                    if val not in prev_elems_list[idx]:
                        new_tree = Solution.bst_insert(tree, val)
                        is_dup = False

                        for tree2 in curr_trees:
                            if Solution.bst_equal(new_tree, tree2):
                                is_dup = True
                                break

                        if not is_dup:
                            curr_trees.append(new_tree)
                            new_elems = copy.deepcopy(prev_elems_list[idx])
                            new_elems.append(val)
                            curr_elems_list.append(new_elems)

        return curr_trees

    def generateTrees(self, n: int) -> List[TreeNode]:
        return Solution.generate_trees(n)

    def generateTrees2(self, n: int) -> List[TreeNode]:
        def generate(l, r):  # split between [l, r)
            if l == r:
                return [None]
            nodes = []
            for i in range(l, r):
                for lchild in generate(l, i):
                    for rchild in generate(i+1, r):
                        # +1 to convert the index to the actual value
                        node = TreeNode(i+1)
                        node.left = lchild
                        node.right = rchild
                        nodes.append(node)
            return nodes
        return generate(0, n) if n else []

    def generateTrees3(self, n: int) -> List[TreeNode]:
        def _gen_trees_for_val(val, left_list, right_list):
            trees = []

            for left in left_list:
                for right in right_list:
                    tree = TreeNode(val)
                    tree.left = left
                    tree.right = right
                    trees.append(tree)

            return trees

        def _gen_trees_in_range(min_inc, max_exc):
            if min_inc == max_exc:
                return [None]

            trees = []

            for val in range(min_inc, max_exc):
                left_list = _gen_trees_in_range(min_inc, val)
                right_list = _gen_trees_in_range(val + 1, max_exc)
                trees += _gen_trees_for_val(val, left_list, right_list)

            return trees

        if n == 0:
            return []

        return _gen_trees_in_range(1, n + 1)

    def generateTrees4(self, n: int) -> List[TreeNode]:
        def gen_tree_by_offset(tree, offset):
            if tree is None:
                return None

            new_tree = copy.deepcopy(tree)
            nodes_togo = [new_tree]

            while len(nodes_togo) > 0:
                curr_node = nodes_togo.pop(0)

                if curr_node is None:
                    continue

                curr_node.val += offset
                nodes_togo.append(curr_node.left)
                nodes_togo.append(curr_node.right)

            return new_tree

        def gen_trees_by_offset(trees, offset):
            return [gen_tree_by_offset(tree, offset) for tree in trees]

        def gen_trees(root_val, left_trees, right_trees):
            trees = []

            for left_tree in left_trees:
                for right_tree in right_trees:
                    tree = TreeNode(root_val)
                    tree.left = left_tree
                    tree.right = right_tree
                    trees.append(tree)

            return trees

        def gen_trees_list(n):
            trees_list = []
            trees_list.append([None])

            for count in range(1, n + 1):
                trees = []

                for root_val in range(count):
                    left_count = root_val
                    right_count = count - (root_val + 1)
                    left_trees = trees_list[left_count]
                    right_trees = trees_list[right_count]

                    if not right_trees == [None]:
                        right_trees = \
                            gen_trees_by_offset(right_trees, root_val + 1)

                    trees += gen_trees(root_val, left_trees, right_trees)

                trees_list.append(trees)

            return trees_list

        if n == 0:
            return []

        return gen_trees_by_offset(gen_trees_list(n)[-1], 1)

    def generateTrees5(self, n: int) -> List[TreeNode]:
        # Helpers.
        def shift_tree(tree, offset):
            if tree is None:
                return None

            tree = copy.deepcopy(tree)
            nodes_togo = [tree]

            while len(nodes_togo) > 0:
                curr_node = nodes_togo.pop(0)

                if curr_node is None:
                    continue

                curr_node.val += offset
                nodes_togo.append(curr_node.left)
                nodes_togo.append(curr_node.right)

            return tree

        def shift_trees(trees, offset):
            return [shift_tree(tree, offset) for tree in trees]

        def create_trees(root_val, left_trees, right_trees):
            trees = []

            for left_tree in left_trees:
                for right_tree in right_trees:
                    tree = TreeNode(root_val)
                    tree.left = left_tree
                    tree.right = right_tree
                    trees.append(tree)

            return trees

        def create_listof_trees(n):
            listof_trees = [[None]]

            for count in range(1, n + 1):
                trees = []

                for root_val in range(count):
                    left_count = root_val
                    right_count = count - (root_val + 1)
                    left_trees = listof_trees[left_count]
                    right_trees = listof_trees[right_count]

                    if not right_trees == [None]:
                        right_trees = shift_trees(right_trees, root_val + 1)

                    trees += create_trees(root_val, left_trees, right_trees)

                listof_trees.append(trees)

            return listof_trees

        # Actual method.
        if n == 0:
            return []

        return shift_trees(create_listof_trees(n)[-1], 1)
