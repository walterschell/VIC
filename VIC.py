from operator import itemgetter
class IntKey:
    _key = []
    def chain_expand(self, size):
        key = self._key
        spot = 0
        while len(self._key) < size:
            self._key.append((_key[spot] + _key[spot+1]) % 10)

def sequentialize(phrase, modreduce=True):
    result_prime = [None] * len(phrase)
    pre_sorted = [None] * len(phrase)
    for i, c in enumerate(phrase):
        pre_sorted[i] = (c, i)
    pre_sorted.sort(key=itemgetter(0))
    for i, seq_pos in enumerate(pre_sorted):
        result_prime[i] = (seq_pos[1], i+1)
    result_prime.sort(key=itemgetter(0))
    result = []
    for _,next_val in result_prime:
        if modreduce:
            next_val %= 10
        result.append(next_val)
    return result

def log(msg, verbose=True):
    if verbose:
        print 'VIC: %s' % msg
def test_sequentialize(verbose):
    passed = True
    reduce_cases = [
        ('ALLTHEPEOP',[1,5,6,0,4,2,8,3,7,9]),
        ('LEAREDEADB',[9,6,1,0,7,4,8,2,5,3]) 
    ]
    for case in reduce_cases:
        log('Sequentialize Testing: %s' % case[0])
        result = sequentialize(case[0])
        log('Sequentialize    Result: %s' % result)
        if result != case[1]:
            log('Sequentialize: FAIL')
            log('Sequentialize: Expected: %s' % case[1])
            passed = False
        else:
            log('Sequentialize: PASS')
    return passed


def testall(verbose=True):
    test_sequentialize(verbose)

testall()

                 
