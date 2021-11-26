def csv_to_tsv(input, output):
  lines = []

  with open(input) as file:
    lines = list(file)

  tab_lines = []

  for line in lines:
    inQuotes = False
    parsed_cell = []
    start = 0
    for cur in range(0, len(line)):
      if line[cur] == ',' and inQuotes == False:
        parsed_cell.append(line[start:cur])
        start = cur + 1
      if line[cur] == '"':
        inQuotes = not inQuotes
    tab_lines.append('\t'.join(parsed_cell) + '\n')
  
  with open(output, 'w') as outFile:
    outFile.writelines(tab_lines)


if __name__ == '__main__':
  csv_to_tsv("./ds.csv", "./ds.tsv")