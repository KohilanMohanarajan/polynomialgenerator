import random
def make_polynomials(limit, latexify):
    ''' (str, bool)
    Generates a set of random polynomials.
    '''
    # Keep making polynomials until limit is reached
    for j in range(0, int(limit)):
        finstr = make_polynomial(latexify)
        print(finstr)

def make_polynomial(latexify):
    ''' (bool) -> str

    Generates a random polynomial.
    '''
    # Languages of variables, degrees, and operations
    varbs = ["x","y","z"]
    degs = ["","^2","^3"]
    ops = ["+","-"]
    # Option for latex-compatible text
    if (latexify == True):
        degs = ["","^{2}","^{3}"]
    # Determine number of terms in polynomial
    strlength = random.randint(3,6)
    finstr = ""
    for i in range(0,strlength):
        # Randomly choose elements of current term
        coeff = random.randint(2,10)
        chovar = random.randint(0,2)
        chosops = random.randint(0,1)
        chodegs = random.randint(0,2)
        # Append term to final string
        finstr = finstr + " " + str(coeff) + varbs[chovar] + degs[chodegs] + " " + ops[chosops]
    # Strip extra characters
    finstr = finstr[1:-2]
    return finstr


if __name__ == "__main__":
    import os, sys, getopt
    def usage():
        print ('Usage:    ' + os.path.basename(__file__) + ' limit latexify')
        print ('Options:')
        print ('\t -l limit, --limit=limit')
        print ('\t -t latex, --latex')
        sys.exit(2)
    try:
      opts, args = getopt.getopt(sys.argv[1:],"h:l:t",["help", "limit=", "latex"])
    except getopt.GetoptError as err:
      print(err)
      usage()
    # extract parameters
    polylimit = None
    latexify = False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
           usage()
        elif opt in ("-l", "--limit"):
           polylimit = arg
        elif opt in ("-t", "--latex"):
           latexify = True
    # check arguments
    if (polylimit is None):
       print('limit missing \n')
       usage()
    # run the command
    make_polynomials(polylimit, latexify)