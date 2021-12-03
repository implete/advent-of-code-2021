import sys

SAMPLE = 'sample.txt'
INPUT = 'input.txt'

def part_one(fname):
  with fname as infile:
    lines = [line.rstrip() for line in infile.readlines()]
    gamma = epsilon = []

    for i in range(0, len(lines[0])):
      counter = 0
      k = [num[i] for num in lines]
      if k.count('0') > k.count('1'):
        counter += 1
      else:
        counter -= 1
      if counter > 0:
        gamma.append('0')
      else:
        gamma.append('1')

    gamma = ''.join(gamma)
    epsilon = [1-int(num) for num in gamma]
    epsilon = ''.join(str(v) for v in epsilon)
    power_consumption = int(gamma, 2) * int(epsilon, 2)
    return power_consumption

def part_two(fname):
  with fname as infile:
    lines = [line.rstrip() for line in infile.readlines()]
    oxygen, carbon_dioxide = list(lines), list(lines)

    for i in range(0, len(lines[0])):
      bit = None
      k = [num[i] for num in oxygen]
      if k.count('0') > k.count('1'):
        bit = 0
      else:
        bit = 1
      
      oxygen_len = len(oxygen)
      if(oxygen_len > 1):
        oxygen = [num for num in oxygen if int(num[i]) == bit]
      l = [num[i] for num in carbon_dioxide]
      if l.count('0') <= l.count('1'):
        bit = 0
      else:
        bit = 1
      
      carbon_dioxide_len = len(carbon_dioxide)
      if(carbon_dioxide_len > 1):
        carbon_dioxide = [num for num in carbon_dioxide if int(num[i]) == bit]
      
      if oxygen_len == 1 and carbon_dioxide_len == 1:
        break
        
    life_support = int(''.join(oxygen), 2) *  int(''.join(carbon_dioxide), 2)
    return life_support

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
        infile = open(INPUT, 'r')
        answer = part == 1 and part_one(infile) or part_two(infile) 
        print('The puzzle answer is: ' + str(answer))
        valid = True
        infile.close()
        break
      else:
        print("Wrong part")
    except Exception as e:
      print(e)
      sys.exit(0)

if __name__ == '__main__':
  main()
