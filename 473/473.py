from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        # 總長若不能被 4 整除，必定無解
        if total % 4 != 0:
            return False

        # 1. 排序（降序），不是 .sored()
        matchsticks.sort(reverse=True)
        side = total // 4
        # 最長火柴放不下也無解
        if matchsticks[0] > side:
            return False

        sides = [0] * 4  # 四條邊目前長度

        def dfs(indx: int) -> bool:
            # 所有火柴都放完，檢查四邊是否都剛好等於 side
            if indx == len(matchsticks):
                return all(s == side for s in sides)

            leng = matchsticks[indx]
            for i in range(4):
                # 如果能放得下，就放
                if sides[i] + leng <= side:
                    sides[i] += leng
                    # 如果下一層回傳 True，這條路徑就成功，立即回傳
                    if dfs(indx + 1):
                        return True
                    # 否則要回溯
                    sides[i] -= leng
                # 空邊剪枝：如果這條邊本來就是 0，放不成功就不用再試其它也是 0 的邊
                if sides[i] == 0:
                    break

            # 四條邊都試過還是無解，回傳 False
            return False

        # 從第 0 根火柴開始遞歸
        return dfs(0)
