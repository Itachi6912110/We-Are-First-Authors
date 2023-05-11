import sys

def weAreFirstAuthors(names):
    names = sorted(names, key=len)
    new_name = ""
    len_authors = len(names)
    while True:
        new_name += ''.join([ x[0] for x in names])
        names = [x[1:] for x in names if len(x) > 1]
        if len(names) != len_authors:
            new_name += ''.join([' ']*(len_authors-len(names)))
            len_authors = len(names)
        if len(names) == 0:
            break
        names = names[1:] + [names[0]]

    return new_name

def whoAreWe(combined_name):
    author_len = combined_name.count(' ')
    names = [''] * author_len
    finalized_name = []
    pointer = 0
    while True:
        names = [ x+combined_name[i] for i, x in enumerate(names) ]
        combined_name = combined_name[len(names):]
        while combined_name[0] == ' ':
            finalized_name.append(names[pointer])
            names.pop(pointer)
            pointer = 0 if pointer == len(names) else pointer
            combined_name = combined_name[1:]
            if len(combined_name) == 0:
                break
        if len(names) == 0:
            break
        names = names[1:] + [names[0]]
        pointer = pointer-1 if pointer-1 >= 0 else len(names)-1

    return finalized_name

if __name__ == '__main__':
    assert len(sys.argv) > 1, "At least one name should be entered!"
    names = sys.argv[1:]
    combined_name = weAreFirstAuthors(names)
    print(f'Author list: {names}')
    print(f'Combined name: {combined_name}')
    reconstructed = whoAreWe(combined_name)
    print(f'Reconstructed author list: {reconstructed}')