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

    def node_value(self):
        if self.header_child_nodes == 0:
            return sum(i for i in self.metadata_entries)
        else:
            sum_children = 0
            for metadata_entry in self.metadata_entries:
                if metadata_entry <= self.header_child_nodes:
                    sum_children += self.child_nodes[metadata_entry - 1].node_value()

            return sum_children


def day_08_task_1(instructions):
    instructions = list(map(int, instructions.split(" ")))
    tree = Node(instructions)
    return tree.sum_metadata_entries()


def day_08_task_2(instructions):
    instructions = list(map(int, instructions.split(" ")))
    tree = Node(instructions)
    return tree.node_value()
