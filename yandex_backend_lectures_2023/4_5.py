import collections


class FolderContentError(BaseException):
    pass


class File:
    def __init__(self, name, filetype, path):
        self.name = name
        self.filetype = filetype
        self.path = path

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'File({self.name})'

    def display(self, indent=0, indent_length=2, indent_symbol=' '):
        print(f'{indent_symbol * indent * indent_length}File({self.name})')


class Folder:
    def __init__(self, name):
        self.name = name
        self.content = []

    def __iadd__(self, obj):
        self.content.append(obj)
        return self

    def __isub__(self, obj):
        if obj in self.content:
            self.content.remove(obj)
            return self
        else:
            raise FolderContentError(f'Object `{obj}` is not in folder `{self.name}`')

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'Folder({self.name}): {self.content}'

    def display(self, indent=0, indent_length=2, indent_symbol=' '):
        print(f'{indent_symbol * indent * indent_length}Folder({self.name})')
        for content in self.content:
            content.display(indent + 1)


class Search:
    def find_obj_path_in_folder_by_name(self, obj_name, folder):
        queue = collections.deque()
        queue.append(folder)

        path =  {folder: None}

        while len(queue):
            folder_left = queue.popleft()

            for folder_content in folder_left.content:
                if folder_content.name == obj_name:
                    return f'{"/".join(self._restore_path(path, folder_left)[::-1])}/{obj_name}'

                if isinstance(folder_content, Folder):
                    queue.append(folder_content)
                    path[folder_content] = folder_left

        return 'No such file in folder'

    def _restore_path(self, path, file):
        while path.get(file):
            return [file.name] + self._restore_path(path, path[file])
        return [file.name]


def read_data():
    file_to_find = input()
    count = int(input())

    root_folder = Folder('')

    current_path = [root_folder]

    for _ in range(count):
        name = input()
        current_path = current_path[:name.count(' ') + 1]
        name = name.strip()

        if '.' in name:
            new_file = File(name, filetype=name.split('.')[-1], path=current_path)
            current_path[-1] += new_file

        else:
            new_folder = Folder(name)
            current_path[-1] += new_folder
            current_path.append(new_folder)
    return file_to_find, root_folder


def main():
    file_to_find, root_folder = read_data()

    root_folder.display()

    searcher = Search()
    path = searcher.find_obj_path_in_folder_by_name(file_to_find, root_folder)
    print(path)


if __name__ == '__main__':
    main()
