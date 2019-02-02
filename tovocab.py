#from toclean import processed_text
import numpy as np
import math
processedfile= open("/Users/krishnamodi/PycharmProjects/projectOne/venv/processed_text.txt", "rb")
#processed_text = fileOpen.readlines()

processed_text = []

for line in processedfile.readlines():
    line=line.decode("utf-8")
    processed_text.append(str(line.strip()))


vocabulary=processed_text
print (vocabulary)


vocab_len = len(vocabulary)

weighted_edge = np.zeros((vocab_len, vocab_len), dtype=np.float32)

score = np.zeros((vocab_len), dtype=np.float32)
window_size = 3
covered_coocurrences = []
print("vocab length",vocab_len)
#xrange = range(0, vocab_len)
for i in range(0, vocab_len):
    print(i," - initial loop")
    score[i] = 1
    for j in range(0, vocab_len) :
        if j == i:
            weighted_edge[i][j] = 0
        else:
            for window_start in range(0, (len(processed_text) - window_size)):

                window_end = window_start + window_size

                window = processed_text[window_start:window_end]

                if (vocabulary[i] in window) and (vocabulary[j] in window):

                    index_of_i = window_start + window.index(vocabulary[i])
                    index_of_j = window_start + window.index(vocabulary[j])

                    # index_of_x is the absolute position of the xth term in the window
                    # (counting from 0)
                    # in the processed_text

                    if [index_of_i, index_of_j] not in covered_coocurrences:
                        if( math.fabs(index_of_i - index_of_j)!=0):
                            weighted_edge[i][j] += 1 / math.fabs(index_of_i - index_of_j)
                        covered_coocurrences.append([index_of_i, index_of_j])
inout = np.zeros((vocab_len),dtype=np.float32)

for i in range(0,vocab_len):
    for j in range(0,vocab_len):
        print(j)
        inout[i]+=weighted_edge[i][j]

MAX_ITERATIONS = 50
d = 0.85
threshold = 0.0001  # convergence threshold

for iter in range(0, MAX_ITERATIONS):
    prev_score = np.copy(score)

    for i in range(0, vocab_len):

        summation = 0
        for j in range(0, vocab_len):
            if weighted_edge[i][j] != 0:
                summation += (weighted_edge[i][j] / inout[j]) * score[j]

        score[i] = (1 - d) + d * (summation)

    if np.sum(np.fabs(prev_score - score)) <= threshold:  # convergence condition
        print
        "Converging at iteration " + str(iter) + "...."
        break
for i in range(0,vocab_len):
    print( "Score of "+vocabulary[i]+": "+str(score[i]))

#69- 12:01pm