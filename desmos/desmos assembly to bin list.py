import sys
import pyperclip
try:
    file = sys.argv[1]
except IndexError:
    file = 'a.txt'
try:
    output = sys.argv[2]
except IndexError:
    output = 'out.txt'
instructionSet = {'ADD':0,'SUB':1,'AND':10,'NOR':11,'___':100,'___':101,'___':110,'JMP':111,'STR':1000,'WRT':1001,'LDI':1010,'TRF':1011,'PSH':1100,'PLL':1101,'NOP':1110,'HLT':1111}
with open(file, 'r') as f:
    with open(output, 'w') as out:
        while True:
            line = f.readline()
            if line == '':
                break
            instruction = instructionSet[line[0:3]]
            #print(instruction, line)
            out.write(str(instruction))
            out.write(line[3:])
            if instruction == instructionSet['WRT']:
                out.write(' 0')
            #out.write('\n')
l=[]
with open(output, 'r') as f:
    text = f.readlines()
    for line in text:
        l.append(line.replace(' ', ',').replace('\n', ''))
l = str(l).replace('[', '').replace(']', '').replace("'", "").replace("'", "")
pyperclip.copy(l)
