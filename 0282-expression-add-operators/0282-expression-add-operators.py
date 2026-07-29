class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    ans.append(path)
                return
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                cur_str = num[index: i + 1]
                cur = int(cur_str)
                if index == 0:
                    dfs(i + 1, cur_str, cur, cur)
                else:
                    dfs(i + 1, path + "+" + cur_str, value + cur, cur)
                    dfs(i + 1, path + "-" + cur_str, value - cur, -cur)
                    dfs(i + 1, path + "*" + cur_str, value - prev + prev * cur, prev * cur)
        dfs(0, "", 0, 0)
        return ans
                
        