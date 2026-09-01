from game import Game

class Command_parser:
    
    def __init__(self, game):
        self.game = game
        
    def parse(self, command):
        
        if command.split(' ', 1)[0] == "travel" and ' ' in command:
                            output_message = self.game.move(command.split(' ', 1)[1])
        
        elif command == "engage":
            output_message = self.game.engage()
            
        elif command == "search":
            output_message = self.game.search()
            
        elif command.split(' ', 1)[0] == "use" and ' ' in command:
            output_message = self.game.use(command.split(' ', 1)[1])

        elif command.split(' ', 1)[0] == "equip" and ' ' in command:
            output_message = self.game.equip(command.split(' ', 1)[1])

        elif command == "":
            output_message = None

        else:
            output_message = f"Unknown command: '{command}'. Click Commands to see the full list."
            
        return output_message