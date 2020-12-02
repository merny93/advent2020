with open("day2.txt", "r") as date_file:
    passwords = date_file.readlines()

count=0 

for line in passwords:
    frag = line.split(" ")
    num_frag = frag[0].split("-")
    freq = [int(num_frag[0]), int(num_frag[1])]
    letter = frag[1].replace(":", "")
    if frag[-1].count(letter) >= freq[0] and frag[-1].count(letter) <= freq[1]:
        print("word", frag[-1])
        print(freq)
        print(letter)
        count += 1

print("final", count)


count=0 

for line in passwords:
    frag = line.split(" ")
    num_frag = frag[0].split("-")
    pos = [int(num_frag[0])-1, int(num_frag[1])-1]
    letter = frag[1].replace(":", "")
    if (frag[-1][pos[0]] == letter and frag[-1][pos[1]] != letter) or (frag[-1][pos[1]] == letter and frag[-1][pos[0]] != letter):
        print("word", frag[-1])
        print(pos)
        print(letter)
        count += 1

print("second", count)