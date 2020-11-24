def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences


def numWords(sentence):
    splitSentence = sentence.split(' ')
    return len(splitSentence)

sentenceLengths = []   
allSentences = get_list_of_sentences() 
def longest_sentence():
    global allSentences 
    global sentenceLengths

    if isinstance(allSentences._tail, Nil) == True:
        sentenceLengths.append(numWords(allSentences._head))
        maxValue = max(sentenceLengths)
        return maxValue
               
    else:
        sentenceLengths.append(numWords(allSentences._head))
        allSentences = allSentences._tail
        return longest_sentence()
