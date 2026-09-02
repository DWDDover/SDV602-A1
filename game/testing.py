from game import Game
from command_parser import Command_parser

class TestResult:
    def __init__(self, command, output=None, error=None):
        self.command = command
        self.output = output
        self.error = error
        self.passed = error is None
        
    def __str__(self):
        if self.passed == True:
            status = "Passed"
            
        else:
            status = "Failed"
            
        return f"Test {status} for command: {self.command} with output: {self.output if self.passed else self.error}"

class TestRun:
    def __init__(self):
        self.results = []

    def run_command(self, parser, command):
        try:
            output = parser.parse(command)
            self.results.append(TestResult(command, output=output))
        except Exception as e:
            self.results.append(TestResult(command, error=str(e)))
            
    def __str__(self):
        results_list = ""
        for result in self.results:
            results_list += (str(result) + "\n")
        return results_list
            
def run_headless_tests():
    test_run = TestRun()

    playthroughs = [
        ["travel north", "travel east", "engage"],
        ["travel south", "search", "equip rusty sword"],
        ["travel east", "search", "use fire proof potion"]
    ]

    for commands in playthroughs:
        game = Game()
        parser = Command_parser(game)
        for command in commands:
            test_run.run_command(parser, command)

    return test_run