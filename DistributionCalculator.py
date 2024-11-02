from fractions import Fraction

def initUniformProbabilities(min, max):
    probabilities = {}
    for i in range(min, max + 1):
        probabilities[i] = Fraction(1, (max-min+1))
    return probabilities
    
def composeProbabilities(prob1, prob2):
    probabilities = {}
    for i in prob1.keys():
        for j in prob2.keys():
            probabilities[i + j] = probabilities.get(i + j, Fraction(0, 1)) + prob1[i] * prob2[j]
    return probabilities
    
def probabilityBeatX(X, distribution):
    winProb = 0
    for key in distribution.keys():
        if key < X:
            winProb += distribution.get(key)
    return winProb

def probabilityEqual(X, distribution):
    return distribution.get(X, 0)

def winLossProb(myDistribution, generalDistribution):
    winProb = 0
    tieProb = 0
    loseProb = 0

    for myKey in myDistribution.keys():
        for generalKey in generalDistribution.keys():
            if myKey == generalKey:
                tieProb += myDistribution.get(myKey) * generalDistribution.get(generalKey)
            elif myKey > generalKey:
                winProb += myDistribution.get(myKey) * generalDistribution.get(generalKey)
            else:
                loseProb += myDistribution.get(myKey) * generalDistribution.get(generalKey)
    return (winProb, tieProb, loseProb)

def additiveExpected(givenDistribution, winResult = 100, tieResult = 0, loseResult = -100):
    outputExpectation = {}
    for key in givenDistribution.keys():
        winRate, tieRate, loseRate = givenDistribution[key]
        outputExpectation[key] = winRate * winResult + tieRate * tieResult + loseRate * loseResult
    return outputExpectation

def multiplicativeExpected(givenDistribution, winResult = 1.1, tieResult = 1, loseResult = 0.9):
    outputExpectation = {}
    for key in givenDistribution.keys():
        winRate, tieRate, loseRate = givenDistribution[key]
        outputExpectation[key] = winResult**winRate * tieResult**tieRate * loseResult ** loseRate
    return outputExpectation


def main():
    D6 = initUniformProbabilities(1, 6)
    DicePair = composeProbabilities(D6, D6)

    givenProbabilities = {}

    for seen in range(1, 7):
        resultProbability = composeProbabilities({seen : Fraction(1, 1)}, D6)
        print(resultProbability)
        winRate, tieRate, loseRate = winLossProb(resultProbability, DicePair)
        givenProbabilities[seen] = (winRate, tieRate, loseRate)
        print(f"The probability that I win after seeing {seen} is {winRate}, tie is {tieRate} and lose is {loseRate}\n")

    print(additiveExpected(givenProbabilities))

    for i in range(0, 11):
        betSize = i/10
        expected = multiplicativeExpected(givenProbabilities, 1 + betSize, 1, 1 - betSize)
        for key in givenProbabilities.keys():
            print(f"If you see {key} and you bet {betSize * 100}% of your money, you can expect to get {expected[key]}x as much money each time.")
        print()


    print(multiplicativeExpected(givenProbabilities))





if __name__ == "__main__":
    main()
