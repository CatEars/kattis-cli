import collections

Submission = collections.namedtuple('Submission', 'id time result')


def make_submission(id, time, result):
    return Submission(id, time, result)


class KattisResult:

    def __init__(self):
        self.AC = []
        self.WA = []

    def add_AC(self, id, time):
        self.AC.append(make_submission(id, time, 'AC'))

    def add_WA(self, id, time):
        self.WA.append(make_submission(id, time, 'WA'))

    def get_plugins(self):
        def checker(context, tree):
            return isinstance(tree, dict) and 'solved' in tree
        def handler(context, tree):
            return any(result.id == tree['solved'] for result in self.AC)
        return [(checker, handler)]
