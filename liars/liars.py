import itertools
import copy

N, M = map(int, input().split())

statements = []
for i in range(M):
    A, B, C = map(int, input().split())
    statements.append([A - 1, B - 1, C])

left_liars = [0] * M
for i in range(M - 2, -1, -1):
    left_liars[i] = left_liars[i + 1] + statements[i + 1][2]

def count_liar(is_liar):
    liar_cnt = 0
    undecided = 0
    for i in range(len(is_liar)):
        liar_cnt += 1 if is_liar[i] == True else 0
        undecided += 1 if is_liar[i] == -1 else 0
    return liar_cnt, undecided

def get_complement(rangeAB, liars):
    not_liar = []
    liars = set(liars)
    for soldier in rangeAB:
        if soldier not in liars: 
            not_liar.append(soldier)
    return not_liar

def backtrack(statements, level, is_liar, min_max):
    if level == M: 
        liar_cnt, undecided = count_liar(is_liar)
        #print 'liar_cnt[%d], undecided[%d]' % (liar_cnt, undecided)
        if liar_cnt < min_max[0]:  min_max[0] = liar_cnt 
        if liar_cnt + undecided > min_max[1]:  min_max[1] = liar_cnt + undecided 
        return 
    A, B, C = statements[level][0], statements[level][1], statements[level][2]
    #print 'A[%d], B[%d], C[%d]' % (A, B, C)
    rangeAB = range(A, B + 1)
    prob_liars = itertools.combinations(rangeAB, C)
    for liars in prob_liars:
        not_liars = get_complement(rangeAB, liars)
        eligible = True
        for liar in liars:
            if is_liar[liar] != -1 and is_liar[liar] == False: 
                eligible = False
                break
        if eligible:
            for not_liar in not_liars:
                if is_liar[not_liar] != -1 and is_liar[not_liar] == True:
                    eligible = False
                    break
        if eligible:
            cp_is_liar = copy.deepcopy(is_liar)
            for liar in liars:
                cp_is_liar[liar] = True
            # REMEMBER set the innocent soldiers
            for not_liar in not_liars:        
                cp_is_liar[not_liar] = False
            # pruning
            liar_cnt, undecided = count_liar(cp_is_liar)
            if liar_cnt < min_max[0] or liar_cnt + undecided > min_max[1]:
                backtrack(statements, level + 1, cp_is_liar, min_max)
    
is_liar = [ -1 ] * N
min_max = [10**18, -10**18]
backtrack(statements, 0, is_liar, min_max)
print (' '.join(map(str, min_max)))
