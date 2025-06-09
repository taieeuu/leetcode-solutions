class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split('/')
        print(path_split)
        path_stack = []
        for dir in path_split:
            if dir == '' or dir == '.':
                continue
            if dir == '..':
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(dir)
        return '/' + '/'.join(path_stack)
sol = Solution()
res = sol.simplifyPath("/home//foo/")
print(res)