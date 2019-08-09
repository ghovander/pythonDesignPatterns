class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries: \n{j}')

file = r'c:\temp\journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())