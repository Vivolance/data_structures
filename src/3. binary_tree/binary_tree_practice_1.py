"""
Implement an always balanced binary tree with the following methods:
insert (with rotations)
delete (with rotations)
inverse
inorder_traversal
preorder_traversal
postorder_traversal
"""

from typing import Optional


class BinaryTreeNode:
    def __init__(
        self,
        value: int,
        left: Optional["BinaryTreeNode"] = None,
        right: Optional["BinaryTreeNode"] = None,
    ) -> None:
        self.value = value
        self.right = right
        self.left = left
        self.height = self.recalculate_height()

    def recalculate_height(self) -> int:
        return (
            max(
                self.left.height if self.left else -1,
                self.right.height if self.right else -1,
            )
            + 1
        )


class BinaryTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self.root = root

    @staticmethod
    def left_rotate(old_parent: BinaryTreeNode) -> BinaryTreeNode:
        new_parent: BinaryTreeNode = old_parent.right
        old_parent.right = new_parent.left
        new_parent.left = old_parent
        old_parent.height = old_parent.recalculate_height()
        new_parent.height = new_parent.recalculate_height()
        return new_parent

    @staticmethod
    def right_rotate(old_parent: BinaryTreeNode) -> BinaryTreeNode:
        new_parent: BinaryTreeNode = old_parent.left
        old_parent.left = new_parent.right
        new_parent.right = old_parent
        old_parent.height = old_parent.recalculate_height()
        new_parent.height = new_parent.recalculate_height()
        return new_parent

    def iterative_insert(self, value: int) -> None:
        call_stack: list[BinaryTreeNode] = []
        new_node: BinaryTreeNode = BinaryTreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_ptr: BinaryTreeNode = self.root
            while True:
                if value < curr_ptr.value:
                    if curr_ptr.left:
                        call_stack.append(curr_ptr)
                        curr_ptr = curr_ptr.left
                    else:
                        curr_ptr.left = new_node
                        curr_ptr.height = curr_ptr.recalculate_height()

                        break
                elif value > curr_ptr.value:
                    if curr_ptr.right:
                        call_stack.append(curr_ptr)
                        curr_ptr = curr_ptr.right
                    else:
                        curr_ptr.right = new_node
                        curr_ptr.height = curr_ptr.recalculate_height()
                        break
                else:
                    raise ValueError("Node exist already!")

        while call_stack:
            curr_ptr: BinaryTreeNode = call_stack.pop()
            curr_ptr.height = curr_ptr.recalculate_height()
            left_height: int = curr_ptr.left.height if curr_ptr.left else -1
            right_height: int = curr_ptr.right.height if curr_ptr.right else -1
            balance_factor: int = left_height - right_height

            is_rotated: bool = False
            if balance_factor < -1:
                # Right Heavy
                is_rotated = True
                if curr_ptr.right and curr_ptr.right.right:
                    old_parent: BinaryTreeNode = curr_ptr
                    new_parent: BinaryTreeNode = BinaryTree.left_rotate(old_parent)
                elif curr_ptr.right and curr_ptr.right.left:
                    # Rotate right then left
                    old_parent: BinaryTreeNode = curr_ptr
                    new_parent_rotated: BinaryTreeNode = BinaryTree.right_rotate(
                        old_parent.right
                    )
                    old_parent.right = new_parent_rotated
                    new_parent: BinaryTreeNode = BinaryTree.left_rotate(old_parent)

            elif balance_factor > 1:
                # Left Heavy
                is_rotated = True
                if curr_ptr.left and curr_ptr.left.left:
                    old_parent: BinaryTreeNode = curr_ptr
                    new_parent: BinaryTreeNode = BinaryTree.right_rotate(old_parent)
                elif curr_ptr.left and curr_ptr.left.right:
                    # Rotate left then right
                    old_parent: BinaryTreeNode = curr_ptr
                    new_parent_rotated: BinaryTreeNode = BinaryTree.left_rotate(
                        old_parent.left
                    )
                    old_parent.left = new_parent_rotated
                    new_parent: BinaryTreeNode = BinaryTree.right_rotate(old_parent)

            if is_rotated:
                # Ensure the grandparent points to the new parent
                if call_stack:
                    grand_parent: BinaryTreeNode = call_stack[-1]
                    if value < grand_parent.value:
                        grand_parent.left = new_parent
                    else:
                        grand_parent.right = new_parent
                else:
                    self.root = new_parent

    def iterative_invert(self) -> None:
        """
        Idea is to swap the left child and right child
        """
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        call_stack: list[BinaryTreeNode] = [self.root]
        while call_stack:
            curr_ptr: BinaryTreeNode = call_stack.pop()
            curr_ptr.left, curr_ptr.right = curr_ptr.right, curr_ptr.left

            if curr_ptr.left:
                call_stack.append(curr_ptr.left)
            if curr_ptr.right:
                call_stack.append(curr_ptr.right)

    def inorder_traversal(self) -> list[int]:
        """
        Visit left, self, right

        Case 1: self.root is empty
        print empty list

        Case 2: self.root present
        - Assign curr_ptr to self.root
        - Create a stack to store the path that we have yet to visit
        - Create a visited set to store the nodes we have visited
        """
        if self.root is None:
            return []
        else:
            inorder_list: list[int] = []
            call_stack: list[BinaryTreeNode] = [self.root]
            visited: set[BinaryTreeNode] = set()
            while call_stack:
                # Check current node
                curr_ptr: BinaryTreeNode = call_stack[-1]
                # check if curr.left is visited
                if curr_ptr.left and curr_ptr.left not in visited:
                    call_stack.append(curr_ptr.left)
                else:
                    # curr.left is visited or not exist, visit curr node
                    inorder_list.append(curr_ptr.value)
                    visited.add(curr_ptr)
                    # pop curr node from call_stack since its visited
                    call_stack.pop()
                    # check if curr.right exist and not yet visited
                    if curr_ptr.right and curr_ptr.right not in visited:
                        call_stack.append(curr_ptr.right)
            return inorder_list

    def preorder_traversal(self) -> list[int]:
        """
        visit self, left, then right

        """
        if self.root is None:
            return []
        else:
            call_stack: list[BinaryTreeNode] = [self.root]
            preorder_list: list[int] = []
            while call_stack:
                curr_ptr: BinaryTreeNode = call_stack.pop()
                preorder_list.append(curr_ptr.value)
                if curr_ptr.right:
                    call_stack.append(curr_ptr.right)
                if curr_ptr.left:
                    call_stack.append(curr_ptr.left)
            return preorder_list

    def postorder_traversal(self) -> list[int]:
        if self.root is None:
            return []
        else:
            call_stack: list[BinaryTreeNode] = [self.root]
            visited: set[BinaryTreeNode] = set()
            postorder_list: list[int] = []
            while call_stack:
                curr_ptr: BinaryTreeNode = call_stack[-1]
                # If left child exists and hasn't been visited, push it
                if curr_ptr.left and curr_ptr.left not in visited:
                    call_stack.append(curr_ptr.left)
                # Else if right child exists and hasn't been visited, push it
                elif curr_ptr.right and curr_ptr.right not in visited:
                    call_stack.append(curr_ptr.right)
                # Both child visited
                else:
                    postorder_list.append(curr_ptr.value)
                    visited.add(curr_ptr)
                    call_stack.pop()
            return postorder_list


if __name__ == "__main__":
    bst_1: BinaryTree = BinaryTree()
    bst_1.iterative_insert(10)
    bst_1.iterative_insert(20)
    bst_1.iterative_insert(30)
    bst_1.iterative_insert(5)
    bst_1.iterative_insert(25)
    bst_1.iterative_insert(40)
    bst_1.iterative_insert(1)

    print(bst_1.root.value)
    print(bst_1.inorder_traversal())
    print(bst_1.preorder_traversal())
    print(bst_1.postorder_traversal())
    bst_1.iterative_invert()
    print(bst_1.inorder_traversal())
