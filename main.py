import os

LINE = "One star. The wall is white, flat, and proud of it. It has never once tried."  # verified: 76 chars

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
