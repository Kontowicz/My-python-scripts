import re
import os
from generete_readme import generate_medium, get_files, add_top
def get_files_main(path):
	files = os.listdir(path)
	final_medium = []
	for file in files:
		if file[len(file)-8:len(file)] == 'medium.h' and file != 'include_medium.h':
			with open(path + file) as f:
				read_data = f.read()
				namespace = re.search(r'namespace( +)_([0-9]+)', read_data)
				final_medium.append([file, int(namespace.group(2))])
	new = sorted(final_medium, key=lambda x:x[1])
	return new
	
def generate_include_medium(data, path):
	file = open(path, 'w')
	for i in data:
		file.write('#include \"' + i[0] + "\"\n")
		
def generate_main(data, path):
	file = open(path, 'w')
	parsed_data = []
	for d in data:
		tmp = d[0]
		tmp = tmp[0:-9]
		tmp = tmp.replace('_', ' ')
		t = tmp[0].upper() + tmp[1::]
		
		parsed_data.append([t, d[1]])
	print(parsed_data)
		
	file.write('#include "include_medium.h"\n')

	file.write('\nvoid print()\n{\n')
	file.write('\tstd::vector<std::string> name;\n')
	for i in parsed_data:
		file.write('\tname.emplace_back("%s");\n' %i[0])	
	file.write('\tint max_len = name[0].length();\n')
	file.write('\tfor (auto it = name.begin(); it != name.end(); ++it)\n\t{\n')
	file.write('\t\tif(max_len < (*it).length())\n')
	file.write('\t\t\tmax_len = (*it).length();\n')
	file.write('\t}\n')
	file.write('\tstd::cout.fill(\' \');\n')
	file.write('\tstd::cout.width(max_len + std::to_string(name.size()).length());\n')
	
	file.write('\tstd::cout << "Medium:" << std::endl;\n')
	file.write('\tint cnt(1);\n')
	file.write('\tfor (int i = 0; i < name.size(); ++i)\n\t{\n')
	file.write('\t\tstd::cout.width(max_len + std::to_string(name.size()).length());\n')
	file.write('\t\tstd::cout.width(max_len + 2);\n')
	file.write('\t\tstd::cout.fill(\'-\');\n')
	file.write('\t\tstd::cout << std::left << cnt++ << std::internal << name[i] << std::endl;\n')	
	file.write('\t}\n')
	file.write('}\n')
	file.write('\n\n\nint main()\n{\n')
	
	file.write('\tint n(0);\n')
	file.write('\tdo\n')
	file.write('\t{\n')
	file.write('\t\tprint();\n')
	file.write('\t\tstd::cin>>n;\n')
	file.write('\t\tstd::cin.ignore();\n')
	file.write('\t\tswitch(n)\n')
	file.write('\t\t{\n')
	
	for i in range(1, len(parsed_data)+1):
		file.write('\t\t\tcase %d: _%d::run(); break;\n' %(i,i))
		
	file.write('\t\t\tcase 0: break;\n')
	file.write('\t\t}\n')
	file.write('\t} while(n > 0);\n')
	file.write('}\n')
	
	
path_main = 'E:/Repos/C++/Hackerank-Problem-Solving-Medium/Medium/Medium/main.cpp'
path_include_medium = 'E:/Repos/C++/Hackerank-Problem-Solving-Medium/Medium/Medium/include_medium.h'
path_medium = 'E:/Repos/C++/Hackerank-Problem-Solving-Medium/Medium/Medium/'
read_me_path = 'E:/Repos/C++/Hackerank-Problem-Solving-Medium/'

f = get_files_main(path_medium)
generate_include_medium(f, path_include_medium)
generate_main(f, path_main)
add_top( read_me_path )
generate_medium(get_files(path_medium), read_me_path)
