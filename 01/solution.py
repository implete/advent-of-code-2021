import sys

SAMPLE_ONE = 'sample-part1.txt'
SAMPLE_TWO = 'sample-part2.txt'
INPUT = 'input.txt'

def part_one(fname):
  with fname as text:
    lines = text.readlines()
    lines = [int(line.rstrip()) for line in lines]
    increases = 0
    for i in range(1, len(lines)):
      if lines[i] > lines[i-1]:
        increases += 1
    return increases

def part_two(fname):
  with fname as text:
    lines = text.readlines()
    lines = [''.join((x for x in line if x.isdigit())) for line in lines]
    lines = [int(line.rstrip()) for line in lines]
    increases = 0
    for i in range(1, len(lines) - 2):
      if sum(lines[i:i+3]) > sum(lines[i-1:i+2]):
        increases += 1
    return increases 

def main():
  options = [1, 2]
  valid = False
  while not valid:
    print("Select a part:")
    for option in options:
      print("> " + str(option))
    try:
      part = input("Part: ")
      if part in options:
        fname = open(INPUT, 'r')
        answer = part == 1 and part_one(fname) or part_two(fname) 
        print('The puzzle answer is: ' + str(answer))
        fname.close()
        valid = True
        break
      else:
        print("Wrong part")
    except Exception as e:
      print(e)
      sys.exit(0)

if __name__ == '__main__':
  main()
