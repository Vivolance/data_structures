from typing import Optional


class TrieNode:
    def __init__(self, char, end_of_word: bool = False) -> None:
        self.char = char
        self.end_of_word = end_of_word
        self.children: list[Optional[TrieNode]] = [None] * 26
        self.number_of_children = 0

    @staticmethod
    def char_to_index(char: str) -> int:
        return ord(char) - ord("a")


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode("*")

    def insert(self, word: str) -> None:
        curr_ptr: TrieNode = self.root
        for index, char in enumerate(word):
            curr_char_index = TrieNode.char_to_index(char)
            if curr_ptr.children[curr_char_index] is None:
                new_node: TrieNode = TrieNode(char)
                curr_ptr.children[curr_char_index] = new_node
                curr_ptr.number_of_children += 1
            curr_ptr = curr_ptr.children[curr_char_index]
            # reaches the last char of the word inserted, set end_of_word to be true
            if index == len(word) - 1:
                curr_ptr.end_of_word = True


