from anytree import *

root = Node('root')
input = open('day07_imput.txt', 'r')
line = input.readline()
line = line.replace('\n', '')
pointer = root
root_size = 0
line_nr = 1
while line != '':
    line = line.split(' ')
     ## Comands
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                tmp_list = str(pointer).split('/')
                tmp = ''
                for i in range(1, len(tmp_list)-1):
                    if i == 1:
                        tmp = tmp_list[i]
                    else:
                        tmp = tmp + '/' + tmp_list[i]
                pointer = Node(tmp)
            elif line[2] == '/':
                pointer = root
            else:
                pointer =  Node(str(pointer)[7:-2] + '/' + line[2])
        if line[1] == 'ls':
            pass
    # directories
    elif line[0] == 'dir':
        parent = str(pointer)[7:-2]
        parent = parent.replace('/', '_')
        tmp = parent + '_' +  line[1]
        locals()[tmp] = Node(line[1], parent=locals()[parent])
        tmp = tmp + '_size'
        # print(tmp)
        locals()[tmp] = 0
        # print('dir: ' + str(locals()[tmp]))
    # files
    elif line[0].isdigit():
        parent = str(pointer)[7:-2]
        parent = parent.replace('/', '_')
        tmp = parent + '_' + line[1]
        locals()[tmp] = Node(line[0], parent=locals()[parent])
        # print('file: ' + str(locals()[tmp]))
    line = input.readline()
    line = line.replace('\n', '')
    # print(str(line_nr) + ": " + str(pointer))
    line_nr = line_nr + 1
for pre, fill, node in RenderTree(root):
    tmp = str(node)[7:-2]
    tmp = tmp.split('/')
    if tmp[-1].isdigit():
        val = ''
        for i in range(0, len(tmp)-1):
            size = int(tmp[-1])
            val = val + tmp[i] + '_'
            # print(val + 'size')
            locals()[val + 'size'] = locals()[val + 'size'] + size
print("Size of root %d"  % root_size)
total_smaller = 0

for pre, fill, node in RenderTree(root):
    tmp = str(node)[7:-2]
    tmp = tmp.replace('/', '_')
    if not tmp.split('_')[-1].isdigit():
        if locals()[tmp + "_size"] < 100001:
            total_smaller = total_smaller + locals()[tmp + "_size"]
        print("%s%s" % (pre, node.name))
print(total_smaller)
