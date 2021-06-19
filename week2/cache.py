from __future__ import annotations
from typing import Any
import sys

# 保存するキャッシュの数XはX=3としました
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


class HashTable(object):
    def __init__(self) -> None:
        self.table = [None] * 1000
        self.linkedList = LinkedList()

    def hash(self, data: tuple) -> int:
        cnt = 0
        for c in data[0].strip():
            cnt += ord(c)
        return cnt


    def add(self, data: tuple) -> None:
        hashed_key = self.hash(data)
        head_node = self.linkedList.head
        tail_node = self.linkedList.tail

        tmp_node = head_node
        len_list = 0

        # ALEX_COMMENT: the loop below is the main cause of ORDER N.
        #              you don't need to search for the last entry.  You
        #              can just use tail_node  -  it should always have the last entry.
        while tmp_node:
            len_list += 1
            tmp_node = tmp_node.next

        
        if len_list >= 3:
            # ハッシュテーブルにデータがあり，ノードの前後にノードがある場合：既に連結リストにデータがあるということなので，付け替えて先頭に持ってくる
            # ALEX_COMMENT:  the search algorithm is excluding both head and tail (is not None)...
            #                that is probably why you are getting duplicates.
            if self.table[hashed_key] and (self.table[hashed_key].prev is not None) and (self.table[hashed_key].next is not None):
                node = self.table[hashed_key]
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                node.prev = None
                head_node.prev = node
                node.next = head_node
                self.linkedList.head = node

            # それ以外の場合：連結リストにデータが無いので，先頭にデータを追加・末尾を削除
            else:
                new_node = Node(data, head_node)
                self.table[hashed_key] = new_node
                self.linkedList.head = new_node
                head_node.prev = new_node
                tail_node.prev.next = None
                self.linkedList.tail = tail_node.prev
                tail_node.prev = None
        # 連結リストの長さが3未満なら普通に追加
        else:
            new_node = Node(data, head_node)
            self.table[hashed_key] = new_node
            self.linkedList.head = new_node
            if head_node is not None:
                head_node.prev = new_node

            if tail_node is None:
                self.linkedList.tail = new_node
            

    def print(self) -> None:
        current_node = self.linkedList.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


hash_table = HashTable()

while 1:
    page_name, url = input("<pageName, url>: ").split()
    data = (page_name, url)
    hash_table.add(data)
    print("linked list: ")
    hash_table.print()
    
