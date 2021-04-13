import networkx as nx


class Throne():
    def __init__(self, first_king_name):  # heading
        self.first_king_name = first_king_name  # the formal argument is assigned the actual one (self.first_king_name is a class field)
        self.all = dict()  # all people in the dynasty
        self.all[first_king_name] = 'M'
        self.who_is_king_now = first_king_name
        self.isalive = dict()
        self.isalive[first_king_name] = True
        self.cooples = dict()
        self.parents = dict()
        self.children = dict()
        self.die1 = list()
        pass

    def marry(self, first_spouse_name, second_spouse_name):  # class method
        # Handles marriage. Takes as input the id (number) of the one who is getting married (and exists in this class) and the name of the second spouse (not from this class).
        if (first_spouse_name in self.all.keys()):  # if a boy gets married
            self.all[second_spouse_name] = "F"  # add a new member of the dynasty
            self.cooples[second_spouse_name] = [first_spouse_name]
            self.cooples[first_spouse_name] = [second_spouse_name]
        elif (second_spouse_name in self.all.keys()):  # if a girl gets married
            self.all[first_spouse_name] = "M"  # add a new member of the dynasty
            self.cooples[second_spouse_name] = [first_spouse_name]
            self.cooples[first_spouse_name] = [second_spouse_name]
        else:
            print('ERROR')
        pass

    def new_born(self, first_parent_name, second_parent_name, child_name, newborngender):
        # Handles the birth of a child. It accepts the names of the parents and the name of the new child as input, adds it to the structure.
        self.all[child_name] = newborngender
        self.isalive[child_name] = True
        if first_parent_name in self.parents:
            self.parents[first_parent_name].append(child_name)
        else:
            self.parents[first_parent_name] = [child_name]
        if second_parent_name in self.parents:
            self.parents[second_parent_name].append(child_name)
        else:
            self.parents[second_parent_name] = [child_name]
        self.children[child_name] = [first_parent_name, second_parent_name]

    def who_is_the_king(self):
        # Returns the name of the current king.
        if self.isalive[self.who_is_king_now] == 'False':
            for i in self.parents[self.who_is_king_now]:
                if self.all[i] == 'M':
                    who_is_king_now = i
            print(who_is_king_now)

    def die(self, name):
        # Handles the death of a character by id.
        self.isalive[name] = False
        self.die1.append(name)
        if name == self.who_is_king_now:
            romanovy.who_is_the_king()

        pass

    def print_dinasty(self):
        print(self.all.keys())
        print(self.isalive.keys())
        # print (self.who_is_king_now)

    def visualise(self):
        self.Gr = nx.Graph()
        self.Gr.add_nodes_from(self.all)
        for key in self.parents.keys():
            # for i in range (len(self.parents[key])):
            for i in self.parents[key]:
                self.Gr.add_edge(key, i)
                # self.Gr.add_edge(key, self.parents[key][i])
        nx.draw_circular(self.Gr, with_labels=True, node_color='green', node_size=1500)


romanovy = Throne('Michail Fodorovich I')  # many people from the dynasty
romanovy.marry('Michail Fodorovich I', 'Maria Dolgorukova I')
romanovy.die('Maria Dolgorukova I')
romanovy.marry('Michail Fodorovich I', 'Evdokia I')
romanovy.new_born('Michail Fodorovich I', 'Evdokia I', 'Aleksey Mihaylovich I', 'M')
romanovy.marry('Aleksey Mihaylovich I', 'Maria Ilynichna I')
romanovy.die('Michail Fodorovich I')
romanovy.new_born('Aleksey Mihaylovich I', 'Maria Ilynichna I', 'Fedor Alekseevich III', 'M')
romanovy.new_born('Aleksey Mihaylovich I', 'Maria Ilynichna I', 'Sofia Alekseevna I', 'W')
romanovy.new_born('Aleksey Mihaylovich I', 'Maria Ilynichna I', 'Ivan V', 'M')
romanovy.die('Maria Ilynichna I')
romanovy.marry('Aleksey Mihaylovich I', 'Natalia Kirillovna I')
romanovy.new_born('Aleksey Mihaylovich I', 'Natalia Kirillovna I', 'Petr I', 'M')

romanovy.die('Natalia Kirillovna I')
romanovy.die('Aleksey Mihaylovich I')
romanovy.die('Fedor Alekseevich III')
romanovy.die('Ivan V')
romanovy.marry('Petr I', 'Ekaterina Alekseevna I')
romanovy.new_born('Petr I', 'Ekaterina Alekseevna I', 'Petr II', 'M')

romanovy.visualise()  # visualization
romanovy.who_is_the_king()