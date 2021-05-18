from __future__ import annotations
from typing import Any
import sys

# NodeとLinkedListはネットに載っていたものを使いました
class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class LinkedList(object):
    def __init__(self, head: Node = None, tail: Node = None) -> None:
        self.head = head
        self.tail = tail

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node


# これは自分で作成
class HashTable(object):
    def __init__(self, linkedList: LinkedList) -> None:
        self.table = [None] * 1000
        self.linkedList = linkedList

    def hash(self, data: tuple) -> int:
        cnt = 0
        for c in data[0].strip():
            cnt += ord(c)
        return cnt


    def add(self, data: tuple) -> None:
        hashed_key = self.hash(data)
        head_node = self.linkedList.head
        tail_node = self.linkedList.tail

        # ハッシュテーブルにデータがあれば，既に連結リストにデータがあるということなので，付け替えて先頭に持ってくる
        if self.table[hashed_key] and (self.table[hashed_key].prev is not None) and (self.table[hashed_key].next is not None):
            node = self.table[hashed_key]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node.prev = None
            head_node.prev = node
            node.next = head_node
            head_node = node

        # ハッシュテーブルにデータが無いなら，連結リストにデータが無いので，先頭にデータを追加・末尾を削除
        else:
            new_node = Node(data, head_node)
            head_node.prev = new_node
            tail_node.prev.next = None
            tail_node.prev = None

    def print(self) -> None:
        current_node = self.linkedList.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

linkedList = LinkedList()
hash_table = HashTable()

page_name = sys.argv[1]
url = sys.argv[2]
data = (page_name, url)

hash_table.add()
