#stripping spaces
# rtext = open('short.txt')
# for line in rtext:
#     line = line.rstrip()
#     if line.startswith('Received:'):
#         print(line)

# #counting the number of characters
# fname = input('enter name of file::')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Received:'):
#         count = count +1
# print('There were', count, 'subject in', fname)


#using try and catch
fname = input('enter name of file::')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Received:'):
        count = count +1
print('There were', count, 'subject in', fname)
