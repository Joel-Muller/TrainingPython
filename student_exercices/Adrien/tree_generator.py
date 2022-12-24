#     +
#    + +
#   + + +
#  + + + +
# + + + + +
#     |
import random


def get_width_row(height):
    # 2 => 3 / 3 => 5 / 4 => 7 / 5 => 9
    # double de la hauteur -1
    return height * 2 - 1


def compute_tree_row_space_left(tree_row, width_base):
    # (taille de la ligne - taille de l'arbre)/2
    tree_row_size = get_width_row(tree_row)
    return (width_base - tree_row_size) // 2


def generate_tree_row(tree_row, width_base):
    space_left = compute_tree_row_space_left(tree_row, width_base)
    space_str = space_left * ' '

    if random.randint(0, 100) > 70 and tree_row > 3:
        tree_row_str = (tree_row * '==')[:-1]
    else:
        tree_row_str = tree_row * '+ '
        tree_row_str = randomly_create_ball(tree_row_str)
    print(space_str + tree_row_str)


def randomly_create_ball(tree_row_str):
    # + + +
    new_row_str = ''

    for element in tree_row_str:
        # add spaces
        if element == ' ':
            new_row_str += ' '
        # add ball or tree
        else:
            if random.randint(1, 100) > 80:
                new_row_str += 'o'
            else:
                new_row_str += '+'
    return new_row_str


def generate_tree_trunk(width_base):
    space_left = compute_tree_row_space_left(1, width_base)

    space_str = space_left * ' '
    tree_row_str = '|'
    print(space_str + tree_row_str)


def generate_tree(height):
    if height < 2:
        return

    width_base = get_width_row(height)
    for tree_row in range(1, height + 1):
        generate_tree_row(tree_row=tree_row, width_base=width_base)
    generate_tree_trunk(width_base=width_base)


if __name__ == '__main__':
    generate_tree(height=10)
