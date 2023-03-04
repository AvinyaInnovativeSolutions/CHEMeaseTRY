import csv
import turtle

class Atom():

    def __init__(self, atomic_number, file_variable):
        self.atomic_number = atomic_number

        with open(file_variable, 'r') as f:
            readerObj = csv.reader(f)
            reader_list = list(readerObj)
            element_details = list(reader_list[atomic_number])
            
            global element_name
            element_name = element_details[1]

            global mass_number
            mass_number = int(element_details[4])

            global neutron_number
            neutron_number = (mass_number-atomic_number)

            global neutron_number_str
            neutron_number_str = f"{neutron_number} neutrons"
            global proton_number_str
            proton_number_str = f"{atomic_number} protons"
            print(f"This element is {element_name}, it has {neutron_number} neutrons and it's mass number is {mass_number}")
        self.element_name = element_name
        self.proton_number_str = proton_number_str
        self.neutron_number_str = neutron_number_str

    def calc_electron_distribution(self, atomic_number):
        global electron_configuration_list
        electron_configuration_list = []
        i = 1

        def get_maximum_electrons(energy_level):
            max_electrons = 2*(energy_level**2)
            return max_electrons

        while ((sum(electron_configuration_list)) <= (atomic_number)):
            electron_configuration_list.append(get_maximum_electrons(i))
            i += 1

        if(sum(electron_configuration_list) > atomic_number):
            to_append = electron_configuration_list[-1]-(sum(electron_configuration_list)-atomic_number)
            electron_configuration_list.pop()
            electron_configuration_list.append(to_append)

        if(electron_configuration_list[-1] > 8):
            to_append1 = electron_configuration_list[-1]-8
            electron_configuration_list.pop()
            electron_configuration_list.append(8)
            electron_configuration_list.append(to_append1)

        print(f"The distribution of electrons is {electron_configuration_list}")
        return electron_configuration_list

    def calculate_valency(self, electron_config_list):
        if(electron_config_list[-1]) <= 4:
            valency = electron_config_list[-1]
        elif(electron_config_list[-1]) > 4:
            valency = (8 - (electron_config_list[-1]))
        print(f"It's valency is {valency}")

    def draw_schematic_diagram(self, el_config):
        global electron_radius
        electron_radius = 20 

        global radii
        radii = []

        wn = turtle.Screen()
        turtle.title(element_name)
        turtle.hideturtle()
        radii = []
        
        def draw_orbits(el_config):
            radii_of_shell = 100
            for i in el_config:
                turtle.penup()
                turtle.home()
                turtle.goto(0, 10)
                turtle.write(proton_number_str, False, "center")
                turtle.goto(0, -20)
                turtle.write(neutron_number_str, False, "center")
                turtle.goto(0, -radii_of_shell)
                turtle.pendown()
                turtle.circle(radii_of_shell)
                radii.append(radii_of_shell)
                radii_of_shell +=100

        draw_orbits(electron_configuration_list)

        def draw_electrons(el_config):
            index_reference = 0
            electrons_filled = 0
            turtle.penup()
            turtle.home()   
            total_electrons = 0
            while electrons_filled <= el_config[index_reference]:
                turtle.penup()
                turtle.forward(radii[index_reference] - electron_radius)
                turtle.right(90)
                turtle.pendown()
                turtle.circle(electron_radius)
                turtle.left(90)
                electrons_filled += 1
                total_electrons += 1
                turtle.penup()
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.right(360/el_config[index_reference])

                if electrons_filled == el_config[index_reference]:
                    index_reference += 1
                    electrons_filled = 0

                if total_electrons == sum(el_config):
                    break
        
        draw_electrons(electron_configuration_list)
        turtle.done()
