class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        rst = ""
        if key in self.dic:
            all_entries = self.dic[key]

            # binary search
            l, r = 0, len(all_entries) - 1

            while l <= r:
                m = (r-l)//2 + l

                if all_entries[m][1] == timestamp:
                    return all_entries[m][0]
                elif all_entries[m][1] > timestamp:
                    r = m - 1
                else:
                    l = m + 1

            if r != -1:
                rst = all_entries[r][0]

        return rst