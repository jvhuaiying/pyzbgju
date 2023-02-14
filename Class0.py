import psutil


class NetworkCard:
    def __init__(self):
        self.netcard_info = []
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    self.netcard_info.append(k)

    def data(self):
        return self.netcard_info
