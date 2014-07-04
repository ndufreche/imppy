import cmd

class PromptHelp(cmd.Cmd):

    def do_help(self, line):
        print "Commands availables :"
        print '- tables : "Show tables"'
        print '- dump : "dump database"'
        print '- restore <optional table> : "restore the last database or table dump"'
        print '- count <table> : "count the table entries"'
        print '- truncate <table> : "remove all table entries"'
        print '- set_path <path> : "change the imppy work folder destination'

    def complete_use(self, text, line, start_index, end_index):
        if text:
            return [
                data for data in self.databases
                if data.startswith(text)
            ]
        else:
            return self.databases

    def complete_count(self, text, line, start_index, end_index):
        return self.tables_complete(text)

    def complete_truncate(self, text, line, start_index, end_index):
        return self.tables_complete(text)

    def complete_restore(self, text, line, start_index, end_index):
        return self.tables_complete(text)

    def tables_complete(self, text):
        if text:
            return [
                table for table in self.tables
                if table.startswith(text)
            ]
        else:
            return self.tables

    def complete_set_path(self, path, line, start_index, end_index):
        if not path:
            return self.listdir('.')
        dirname, rest = os.path.split(path)
        tmp = dirname if dirname else '.'
        res = [
            p for p in self.listdir(tmp) if p.startswith(rest)
        ]
        if len(res) == 1:
            return [
                os.path.join(dirname, p)
                for p in self.listdir(tmp)
                if p.startswith(rest)
            ]

        if len(res) > 1 or not os.path.exists(path):
            return res
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self.listdir(path)]
        return [path + ' ']