
class Task_manner(object):
    def __init__(self, init_url):
        self.task_lis = [init_url]
        self.done_lis = []
        self.iter_task_lis = iter(self.task_lis)

    def add_task(self, url):
        if url in self.done_lis:
            pass
        else:
            self.task_lis.append(url)

