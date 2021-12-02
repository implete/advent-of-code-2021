import sys

SAMPLE = 'sample.txt'
INPUT = 'input.txt'

def part_one(fname):
  with fname as text:
    lines = text.readlines()
    lines = [line.split() for line in lines]
    depth = horizontal = 0
    for command, unit in lines:
        if command == 'forward':
            horizontal += int(unit)
        elif command == 'down':
            depth += int(unit)
        elif command =='up':
            depth -= int(unit) 
    position = depth * horizontal;
    return position

def part_two(fname):
  with fname as text:
    lines = text.readlines()
    lines = [line.split() for line in lines]
    depth = horizontal = aim = 0
    for command, unit in lines:
        if command == 'forward':
            horizontal += int(unit)
            if aim == 0:
                continue
            else:
                depth += int(unit) * aim
        elif command == 'down':
            aim += int(unit)
        elif command =='up':
            aim -= int(unit) 
    position = depth * horizontal;
    return position

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
