def writeFile(text_file):
    """
    text files demo
    """
    fd = open(text_file, 'a')
    fd.write('First')
    fd.write('\n')
    fd.write('What?')

writeFile('../words1.txt')
