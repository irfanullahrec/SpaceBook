p = r'D:\SpaceBook\SpaceBook Web\js\biology_12_data.js'
with open(p, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# line 9987 was '}\n', line 9988 was 'add("24.2...', line 9989 was '}\n'
# Let's inspect around lines 9985-9992
for idx in range(len(lines)):
    if 'add("24.5.3 Hardy–Weinberg' in lines[idx]:
        print('Found at', idx)
        # line idx+1 is '}\n'
        # line idx+2 is 'add("24.2...'
        # line idx+3 is '}\n'
        if lines[idx+1].strip() == '}' and 'add("24.2' in lines[idx+2] and lines[idx+3].strip() == '}':
            # Swap lines[idx+1] and lines[idx+2], and delete lines[idx+3]
            line_add = lines[idx+2]
            lines[idx+1] = line_add
            lines[idx+2] = '}\n'
            del lines[idx+3]
            print('Successfully fixed biology_12_data.js!')
            break

with open(p, 'w', encoding='utf-8') as f:
    f.writelines(lines)
