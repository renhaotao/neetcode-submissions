class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        # print("storing", [value, timestamp])
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # print("getting {} at ts {}".format(key, timestamp))
        if key in self.store:
            l, r = 0, len(self.store[key]) - 1
            # print("l: {}, r: {}".format(l, r))
            
            rst = ""
            while l <= r:
                m = (l + r) // 2
                # print("m: ", m)

                if self.store[key][m][1] > timestamp:
                    r = m - 1
                elif self.store[key][m][1] < timestamp:
                    rst = self.store[key][m][0]
                    l = m + 1
                else:
                    return self.store[key][m][0]

            return rst

        return ""

            
