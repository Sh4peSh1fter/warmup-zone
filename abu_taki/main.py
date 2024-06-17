# modules
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import networkx as nx
from itertools import cycle

# consts
NUM_OF_OBJECTS = 10


class Note():
    def __init__(self, id):
        self.id = id


class Box():
    def __init__(self, id, note):
        self.id = id
        self.note = note

    def info(self):
        return self.id, self.note.id


class Programmer():
    def __init__(self, id):
        self.id = id
        self.picked_notes = []
        self.movement_path = []

    def get_note(self, boxes):
        current_box_id = self.id
        while len(self.picked_notes) <= NUM_OF_OBJECTS:
            self.movement_path.append(current_box_id)
            current_box = boxes[current_box_id - 1]
            note = current_box.note
            self.picked_notes.append(note.id)
            if note.id == self.id:
                break
            current_box_id = note.id

    def info(self):
        return self.id, self.picked_notes


def main():
    # set notes and shuffle
    notes = [Note(id) for id in range(1, NUM_OF_OBJECTS + 1)]
    random.shuffle(notes)
    # set boxes and put notes in them
    boxes = [Box(id, note) for id, note in enumerate(notes, start=1)]
    # set programmers
    programmers = [Programmer(id) for id in range(1, NUM_OF_OBJECTS + 1)]

    # setup graph view
    colors = cycle(['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown'])
    color_map = {}
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

    # ax1 setup
    programmer_ids = [p.id for p in programmers]
    ax1.set_xlabel('Programmer ID')
    ax1.set_ylabel('Number of Attempts')
    ax1.set_title('Number of Attempts for Each Programmer to Find Their Note')

    # ax2 setup
    # draw the path directed graph
    G = nx.DiGraph()
    ## add nodes
    for box in boxes:
        G.add_node(box.id, label=f"Box {box.id}\nNote {box.note.id}")
    node_pos = nx.circular_layout(G)     # position nodes on a circle
    node_labels = nx.get_node_attributes(G, 'label')     # add labels to the nodes
    nx.draw(G, node_pos, with_labels=True, labels=node_labels, node_size=3000, node_color='lightblue', font_size=10,
            font_weight='bold', edge_color='gray')
    ax2.set_title("Programmer's Note Picking Path")

    ############################################# run an attempt ######################################################
    # let the programmers try to get their note
    for programmer, color in zip(programmers, colors):
        programmer.get_note(boxes)

        # add edges based on the movement path
        color_map[programmer.id] = color
        path_edges = list(zip(programmer.movement_path[:-1], programmer.movement_path[1:]))
        # draw ax2 path
        nx.draw_networkx_edges(G, node_pos, edgelist=path_edges, edge_color=color, width=6, alpha=0.7,
                               connectionstyle='arc3,rad=0.2', arrows=True)

    # Add legend
    ax2_handles = [plt.Line2D([0], [0], color=color, lw=2) for color in color_map.values()]
    ax2_labels = [f'Programmer {id}' for id in color_map.keys()]
    ax2.legend(ax2_handles, ax2_labels, loc='center left', bbox_to_anchor=(1, 0.5), title='Programmers')

    # Show number of attempts for each programmer
    programmer_attempts = [len(p.picked_notes) for p in programmers]
    ax1.bar(programmer_ids, programmer_attempts, color=[color_map[id] for id in programmer_ids])
    ax1.set_xticks(programmer_ids)

    # Adjust layout to make room for the legend
    fig.tight_layout()
    # Full screen the window
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()

    # # debug
    # print(f"boxes:")
    # for box in boxes:
    #     print(f"{box.info()}")
    #
    # print(f"programmers:")
    # for programmer in programmers:
    #     print(f"{programmer.info()}")


if __name__ == '__main__':
    main()
