from operator import itemgetter
class IntKey:
    _key = []
    def chain_expand(self, size):
        key = self._key
        spot = 0
        while len(self._key) < size:
            self._key.append((_key[spot] + _key[spot+1]) % 10)
    def __getitem__(self, index):
        return self._key[index]
    @classmethod
    def from_number_string(cls, numbers):
        result = IntKey()
        for i in numbers:
            result._key.append(int(i))
        return result
    def __str__(self):
        result = ''
        for i in self._key:
            result += '%d' % i
        return result
class StraddlingCheckerboard:
    def __init__(self, key, rows=None):
        self.key = key
        if rows is None:
            rows = ['ESTONIAR  ', #Vowels to encode with one number
                    'BCDFGHJKLM', #First row of leftovers
                    'PQUVWXYZ.#'] #Second row of leftovers
        self.rows = rows

    def decode(self, msg):
        keymap = {}
        for i in range(10):
            keymap[self.key[i]] = i
        result = ''
        i = 0
        while i < len(msg):
            ci = int(msg[i])
            c = ''
            if ci == self.key[-1]:
                i += 1
                c = self.rows[2][keymap[int(msg[i])]]
            elif ci == self.key[-2]:
                i += 1
                c = self.rows[1][keymap[int(msg[i])]]
            else:
                c = self.rows[0][keymap[ci]]
            result += c
            i += 1
        return result
    def encode(self, msg):
        result = ''
        for c in msg.upper():
            symbol = None
            try:
                symbol = str(self.key[self.rows[0].index(c)])
            except: pass
            try:
                 
                symbol = str(self.key[-2]) + str(self.key[self.rows[1].index(c)])
            except: pass
            try:
                symbol = str(self.key[-1]) + str(self.key[self.rows[2].index(c)])
            except: pass
            result += symbol
        return result
    def __str__(self):
        result = 'Checkerboard below\n'
        result += '_|' + '|'.join(str(self.key)) + '\n'
        result += '=====================' + '\n'
        result += ' |' + '|'.join(self.rows[0]) + '\n'
        result += str(self.key[-2]) + '|' + '|'.join(self.rows[1]) + '\n'
        result += str(self.key[-1]) + '|' + '|'.join(self.rows[2])
        return result
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

def test_checkerboard(verbose=True):
    key = IntKey.from_number_string('1234567890')
    board = StraddlingCheckerboard(key)
    log(str(board))
    test_phrase = 'THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG'
    log(test_phrase)
    ct = board.encode(test_phrase)
    log(ct)
    pt = board.decode(ct)
    log(pt)
all_tests = [
         test_sequentialize,
         test_checkerboard
         ]
def testall(verbose=True):
    for test in all_tests:
        test(verbose)

testall()

                 
