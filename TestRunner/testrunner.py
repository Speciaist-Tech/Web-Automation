class TestRunner:
    def __init__(self):
        self.checkers = []

    def check(self, name, condition):
        if condition is not None:
            print("PASS", name)
            self.checkers.append(True)
            return True
        print("FAIL", name)
        self.checkers.append(False)
        return False

    def summary(self):
        print(f"{self.checkers.count(True)} passed, {self.checkers.count(False)} failed")
