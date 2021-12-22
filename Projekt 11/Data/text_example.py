class information(object):
    def __init__(self, country):
        self.country = country

    def show_text(self):
        print(self.country)


example_1 = information("Germany")
example_2 = information("France")

all_examples = [example_1, example_2]

def read_all():
    x=0
    for item in all_examples:
        all_examples[x].show_text()
        x = x + 1
