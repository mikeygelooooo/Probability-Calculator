from math import factorial



def classicalProbability(nValue, NValue):
    # Probability of A occuring: P(A)
    probA = nValue/NValue
    # Probability of A NOT occuring: P(A')
    probNotA = 1 - probA
    
    return [nValue, NValue, probA, probNotA]

def permcombCalculator(nValue, rValue):
    #Total Number of Permutations: nPr
    permutations = factorial(nValue)/factorial(nValue - rValue)
    # Total Number of Combinations: nCr
    combinations = factorial(nValue)/(factorial(rValue) * factorial(nValue - rValue))
    
    return [nValue, rValue, int(permutations), int(combinations)]



# Recieves 4  inputs: (1, 2) Proabability for A and B
# (3) input mode for C (union or intersection); (4) probabilty for C
def conditionalProbability (probA, probB, Cmode, probC):
    aComp = round(1 - probA, 4)
    bCOmp = round(1 - probB, 4)

    results_list = []

    # If input mode is union
    if Cmode == 1: 
        # P(A∩B'); only areas in A that are not in B; removes B from Union area
        aExcl = round(probC - probB, 4)
        # P(A'∩B); only areas in B that are not in A; removes A from Union area 
        bExcl = round(probC - probA, 4)

        #  P(AUB) - P(A∩B') - P(A'∩B)
        # Removes, areas exclusive to A and B, leaving only the intersection
        probIntersection = round(probC - aExcl - bExcl, 4)
        probUnion = round(probC, 4)
           
        A_if_B = round(probIntersection / probB, 4)     # P(A|B)
        B_if_A = round(probIntersection / probA, 4)     # P(B|A)
        A_if_Bcomp = round(aExcl / bCOmp, 4)            # P(A|B')
        B_if_Acomp = round(bExcl / aComp, 4)            # P(B|A')
        
        results_list = [probA, probB, probC, A_if_B, B_if_A, A_if_Bcomp, B_if_Acomp, probUnion, probIntersection]

    # If input mode is intersection
    elif Cmode == 2:
        # P(A∩B'); only areas in A that are not in B; removes Intersection area from A
        aExcl = round(probA - probC, 4)
        # P(A'∩B); only areas in B that are not in A; removes Intersection area from B   
        bExcl= round(probB - probC, 4)
        
        # Computes Union and rounds Intersection for display
        probUnion = round(probA + probB - probC, 4)
        probIntersection = round(probC, 4)
        
        A_if_B = round(probC / probB, 4)            # P(A|B)
        B_if_A = round(probC / probA, 4)            # P(B|A)
        A_if_Bcomp = round(aExcl / bCOmp, 4)        # P(A|B')
        B_if_Acomp = round(bExcl / aComp, 4)        # P(B|A')
        
        results_list = [probA, probB, probC, A_if_B, B_if_A, A_if_Bcomp, B_if_Acomp, probUnion, probIntersection]
        
    return results_list



def independentProbability(probA, probB):
    aComp = round(1 - probA, 4)                             # P(A')
    bComp = round(1 - probB, 4)                             # P(B')
    intersect = round(probA * probB, 4)                     # P(A∩B)
    union = round((probA + probB) - intersect, 4)           # P(AUB)
    diverge = round((probA + probB) - (2* intersect), 4)    # P(AΔB)
    neither = round(1 - union, 4)                           # P((AUB)')
    aUbComp = round(probA * bComp, 4)                       # P(AUB')
    bUaCOmp = round(probB * aComp, 4)                       # P(A'UB)
    return [probA, probB, aComp, bComp, intersect, union, diverge, neither, aUbComp, bUaCOmp]