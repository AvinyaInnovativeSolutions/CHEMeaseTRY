from element import Atom

atomic_no = int(input('Enter the atomic number : '))
file_obj = 'periodic_table.csv'

atom = Atom(atomic_no, file_obj)
atom.calc_electron_distribution(atomic_no)
el_conf = atom.calc_electron_distribution(atomic_no)
atom.calculate_valency(el_conf)
atom.draw_schematic_diagram(el_conf)
