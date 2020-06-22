class Solution:
    def simplifyPath(self, path: str) -> str:
        length = len(path)
        idx = 0
        result = []
        name = ''
        while idx < length:
            if path[idx] == '/' or idx == length - 1:
                if path[idx] != '/' and idx == length - 1:
                    name += path[idx]
                # print(f'name:{name}')
                if name == '' or name == '.':
                    pass
                elif name == '..':
                    if len(result) == 0:
                        pass
                    else:
                        result.pop()
                else:
                    result.append(name)
                name = ''
            else:
                name += path[idx]
            idx += 1
        return '/' + '/'.join(result)
