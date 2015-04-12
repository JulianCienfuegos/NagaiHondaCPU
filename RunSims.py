import os 

gamma = [0, 0.1, 1, 10]
beta = gamma
lam = beta
area = [1.0, 4.0, 10.0]

pi = 3.141592

def write_line(name, value, semicolon):
    if semicolon:
        return 'const double ' + name + ' = ' + str(value) + ';\n'
    else:
        return 'const double ' + name + ' = ' + str(value) + ' ;\n'

intro = '#ifndef PARAMS\n#define PARAMS\n\n'
close = '\n#endif'
n = 1

for g in gamma:
    for b in beta:
        for l in lam:
            for a in area:
                if( g !=0 or b != 0 or l != 0):
                    params = open('parameters.hpp', 'w')
                    params.write(intro)
                    params.write(write_line('beta', b, 1))
                    params.write(write_line('lambda', l, 1))
                    params.write(write_line('pi', pi, 1))
                    params.write(write_line('t_area', a, 0))
                    params.write(write_line('t_gamma', g, 1))
                    params.write(close)
                    params.close()
                    os.system('make clean')
                    os.system('make')
                    title = 'simulation' + str(n)
                    n = n + 1
                    new_dir = 'mkdir ' + title 
                    copy2dir = 'cp Images/* ' + title
                    os.system('./NagaiHondaModel')
                    os.system(new_dir)
                    os.system(copy2dir)
