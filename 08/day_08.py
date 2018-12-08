class Node:
    def __init__(self, instructions):
        self.header_child_nodes = instructions[0]
        self.header_metadata_entries = instructions[1]
        self.child_nodes = []
        i = 0
        current_position = 2
        while i < self.header_child_nodes:
            new_node = Node(instructions[current_position:])
            self.child_nodes.append(new_node)
            current_position += new_node.size
            i += 1
        child_sizes = sum(node.size for node in self.child_nodes)
        self.metadata_entries = instructions[child_sizes + 2:child_sizes + 2 + self.header_metadata_entries]
        self.size = 2 + len(self.metadata_entries) + child_sizes

    def sum_metadata_entries(self):
        return sum(i for i in self.metadata_entries) + sum(node.sum_metadata_entries() for node in self.child_nodes)


def day_08_task_1(instructions):
    instructions = list(map(int, instructions.split(" ")))
    tree = Node(instructions)
    return tree.sum_metadata_entries()
