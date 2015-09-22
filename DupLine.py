import sublime
import sublime_plugin


class DupLineCommand(sublime_plugin.TextCommand):

    def run(self, edit, direction="down"):

        sels = self.view.sel()

        if direction == "up":
            for region in reversed(sels):
                line = self.view.line(region)
                line_contents = '\n' + self.view.substr(line)
                self.view.insert(edit, line.end(), line_contents)

        else:
            for region in sels:
                line = self.view.line(region)
                line_contents = self.view.substr(line) + '\n'
                self.view.insert(edit, line.begin(), line_contents)
