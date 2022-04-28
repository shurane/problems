from typing import List, Dict
from helpers2 import Color as C

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = [0 for _ in range(len(words))]

        for letter in s:
            for i in range(len(words)):
                if indices[i] < len(words[i]) and letter == words[i][indices[i]]:
                    indices[i] += 1

        count = 0
        for i in range(len(words)):
            count += int(len(words[i]) == indices[i])
        return count

    def numMatchingSubseqTrieTooManyCalls(self, s: str, words: List[str]) -> int:
        t = Trie()
        for word in words:
            t.insert(word)

        count = 0
        seen = set()
        def helper(s: str, i: int, trie) -> None:
            nonlocal count
            print("helper", i, f"{s[:i]}{C.RED}{s[i]}{C.RESET}{s[i+1:]}", "count", count)
            if trie.end and trie.word not in seen:
                count += trie.count
                seen.add(trie.word)
                # print("match", s[:i], trie.word, count)

            while i < len(s):
                letter = s[i]
                if letter in trie.children:
                    helper(s, i + 1, trie.children[letter])
                i += 1

        helper(s, 0, t)
        return count

class Trie:
    def __init__(self):
        self.children: Dict[str, Trie] = dict()
        self.count = 0
        self.end = False
        self.letter = "*"
        self.word = ""

    def __repr__(self):
        return f"{self.letter}"

    def insert(self, s):
        if not s:
            return

        curr: Trie = self
        for letter in s:
            if letter not in curr.children:
                curr.children[letter] = Trie()
            curr = curr.children[letter]
            curr.letter = letter

        curr.count += 1
        curr.end = True
        curr.word = s

s = Solution()

assert s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]) == 3
assert s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2
assert s.numMatchingSubseq("qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]) == 2
assert s.numMatchingSubseq("a" * 5, ["a" * i for i in range(1,6)]) == 5
assert s.numMatchingSubseq("a" * 20, ["a" * i for i in range(1,21)]) == 20
assert s.numMatchingSubseq("a" * 50, ["a" * i for i in range(1,51)]) == 50
assert s.numMatchingSubseq("a" * 100, ["a" * i for i in range(1,101)]) == 100
assert s.numMatchingSubseq(
("ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisk" +
 "sutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugp" +
 "eekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrs" +
 "urrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvn" +
 "digovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryz" +
 "dmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzk" +
 "hndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjy" +
 "ljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnh" +
 "rptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddv" +
 "dlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxj" +
 "hsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd"),
["iowuuudrgzmw",
 "azfcxtvhkruvuturdicnucvndigovkzrq",
 "ylmmo",
 "maptilrbfpjxiarmwalhbd",
 "oqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqgl",
 "ytldcdlxqbaszbuxsacqwqnhrewhagldzhr",
 "zeeab",
 "cqie",
 "pvrazfcxtvhkruvuturdicnucvndigovkzrqiya",
 "zxnvpluwicurrtshyvevkriudayyysepzq",
 "wyhxltligahroyshfn",
 "nhrewhagldzhryzdmmrwn",
 "yqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmw",
 "nhrptuugyfsghluythksqhmxlmggtcbdd",
 "yligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjsc",
 "zdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzq",
 "ncygycdpehteiugqbptyqbvokpwovbnplshnzafun",
 "gdzutwgjofowhryrubnxkahocqjzww",
 "eppapjoliqlhbrbgh",
 "qwhgobwyhxltligahroys",
 "dzutwgjofowhryrubnxkah",
 "rydhxkdhffyytldcdlxqbaszbuxs",
 "tyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjc",
 "khvyjyrydhxkdhffyytldcdlxqbasz",
 "jajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqn",
 "ppapjoliqlhbrbghq",
 "zmwwxzjckmaptilrbfpjxiarm",
 "nxkahocqjzwwagqidjhwbunvlchoj",
 "ybfxpvqywqjdlyznmojdhbeomyjqptltp",
 "udrgzmwnxae",
 "nqglnpjvwddvdlmjjyzmww",
 "swlvtlbmkrsurrcsgdzutwgjofowhryrubn",
 "hudqbfnzxnvpluwicurr",
 "xaezuqlsfvchjf",
 "tvibbwxnokzkhndmdhweyeycamjeplec",
 "olnswlvtlbmkrsurrcsgdzu",
 "qiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyyt",
 "eiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwyl",
 "cgiowuuudrgzmwnxaezuqlsfvchjflocz",
 "rxric",
 "cygycdpehteiugqbptyqbvokpwovbnplshnzaf",
 "g",
 "surrcsgd",
 "yzenflfnhrptuugyfsghluythksqh",
 "gdzutwgjofowhryrubnxkahocqjzwwagqid",
 "ddeoincygycdpeh",
 "yznmojdhbeomyjqptltpugzceyzenflfnhrptuug",
 "ejuisks",
 "teiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoi",
 "mrwnxhaqfezeeabuacyswollycgio",
 "qfskkpfakjretogrokmxemjjbvgmmqrfdxlkfvycwalbdeumav",
 "wjgjhlrpvhqozvvkifhftnfqcfjmmzhtxsoqbeduqmnpvimagq",
 "ibxhtobuolmllbasaxlanjgalgmbjuxmqpadllryaobcucdeqc",
 "ydlddogzvzttizzzjohfsenatvbpngarutztgdqczkzoenbxzv",
 "rmsakibpprdrttycxglfgtjlifznnnlkgjqseguijfctrcahbb",
 "pqquuarnoybphojyoyizhuyjfgwdlzcmkdbdqzatgmabhnpuyh",
 "akposmzwykwrenlcrqwrrvsfqxzohrramdajwzlseguupjfzvd",
 "vyldyqpvmnoemzeyxslcoysqfpvvotenkmehqvopynllvwhxzr",
 "ysyskgrbolixwmffygycvgewxqnxvjsfefpmxrtsqsvpowoctw",
 "oqjgumitldivceezxgoiwjgozfqcnkergctffspdxdbnmvjago",
 "bpfgqhlkvevfazcmpdqakonkudniuobhqzypqlyocjdngltywn",
 "ttucplgotbiceepzfxdebvluioeeitzmesmoxliuwqsftfmvlg",
 "xhkklcwblyjmdyhfscmeffmmerxdioseybombzxjatkkltrvzq",
 "qkvvbrgbzzfhzizulssaxupyqwniqradvkjivedckjrinrlxgi",
 "itjudnlqncbspswkbcwldkwujlshwsgziontsobirsvskmjbrq",
 "nmfgxfeqgqefxqivxtdrxeelsucufkhivijmzgioxioosmdpwx",
 "ihygxkykuczvyokuveuchermxceexajilpkcxjjnwmdbwnxccl",
 "etvcfbmadfxlprevjjnojxwonnnwjnamgrfwohgyhievupsdqd",
 "ngskodiaxeswtqvjaqyulpedaqcchcuktfjlzyvddfeblnczmh",
 "vnmntdvhaxqltluzwwwwrbpqwahebgtmhivtkadczpzabgcjzx",
 "yjqqdvoxxxjbrccoaqqspqlsnxcnderaewsaqpkigtiqoqopth",
 "wdytqvztzbdzffllbxexxughdvetajclynypnzaokqizfxqrjl",
 "yvvwkphuzosvvntckxkmvuflrubigexkivyzzaimkxvqitpixo",
 "lkdgtxmbgsenzmrlccmsunaezbausnsszryztfhjtezssttmsr",
 "idyybesughzyzfdiibylnkkdeatqjjqqjbertrcactapbcarzb",
 "ujiajnirancrfdvrfardygbcnzkqsvujkhcegdfibtcuxzbpds",
 "jjtkmalhmrknaasskjnixzwjgvusbozslrribgazdhaylaxobj",
 "nizuzttgartfxiwcsqchizlxvvnebqdtkmghtcyzjmgyzszwgi",
 "egtvislckyltpfogtvfbtxbsssuwvjcduxjnjuvnqyiykvmrxl",
 "ozvzwalcvaobxbicbwjrububyxlmfcokdxcrkvuehbnokkzala",
 "azhukctuheiwghkalboxfnuofwopsrutamthzyzlzkrlsefwcz",
 "yhvjjzsxlescylsnvmcxzcrrzgfhbsdsvdfcykwifzjcjjbmmu",
 "tspdebnuhrgnmhhuplbzvpkkhfpeilbwkkbgfjiuwrdmkftphk",
 "jvnbeqzaxecwxspuxhrngmvnkvulmgobvsnqyxdplrnnwfhfqq",
 "bcbkgwpfmmqwmzjgmflichzhrjdjxbcescfijfztpxpxvbzjch",
 "bdrkibtxygyicjcfnzigghdekmgoybvfwshxqnjlctcdkiunob",
 "koctqrqvfftflwsvssnokdotgtxalgegscyeotcrvyywmzescq",
 "boigqjvosgxpsnklxdjaxtrhqlyvanuvnpldmoknmzugnubfoa",
 "jjtxbxyazxldpnbxzgslgguvgyevyliywihuqottxuyowrwfar",
 "zqsacrwcysmkfbpzxoaszgqqsvqglnblmxhxtjqmnectaxntvb",
 "izcakfitdhgujdborjuhtwubqcoppsgkqtqoqyswjfldsbfcct",
 "rroiqffqzenlerchkvmjsbmoybisjafcdzgeppyhojoggdlpzq",
 "xwjqfobmmqomhczwufwlesolvmbtvpdxejzslxrvnijhvevxmc",
 "ccrubahioyaxuwzloyhqyluwoknxnydbedenrccljoydfxwaxy",
 "jjoeiuncnvixvhhynaxbkmlurwxcpukredieqlilgkupminjaj",
 "pdbsbjnrqzrbmewmdkqqhcpzielskcazuliiatmvhcaksrusae",
 "nizbnxpqbzsihakkadsbtgxovyuebgtzvrvbowxllkzevktkuu",
 "hklskdbopqjwdrefpgoxaoxzevpdaiubejuaxxbrhzbamdznrr",
 "uccnuegvmkqtagudujuildlwefbyoywypakjrhiibrxdmsspjl",
 "awinuyoppufjxgqvcddleqdhbkmolxqyvsqprnwcoehpturicf"]) == 51
