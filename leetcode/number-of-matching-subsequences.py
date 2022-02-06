from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        t = Trie()
        for word in words:
            t.insert(word)

        count = 0
        seen = set()
        def helper(s: str, i: int, trie) -> None:
            nonlocal count
            if trie.end and trie.word not in seen:
                count += trie.count
                seen.add(trie.word)
                # print("match", s[:i], trie.word, count)

            if i == len(s):
                return

            while i < len(s):
                code = ord(s[i])
                if trie.children[code] is not None:
                    helper(s, i + 1, trie.children[code])
                i += 1

        helper(s, 0, t)
        return count

class Trie:
    def __init__(self):
        self.children = [None] * 128
        self.count = 0
        self.end = False
        self.word = ""

    def insert(self, s):
        if not s:
            return

        curr = self
        for letter in s:
            pos = ord(letter)
            if curr.children[pos] is None:
                curr.children[pos] = Trie()
            curr = curr.children[pos]

        curr.count += 1
        curr.end = True
        curr.word = s

s = Solution()

assert s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]) == 3
assert s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2
assert s.numMatchingSubseq("qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]) == 2
# s.numMatchingSubseq(
# ("ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisk" +
#  "sutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugp" +
#  "eekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrs" +
#  "urrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvn" +
#  "digovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryz" +
#  "dmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzk" +
#  "hndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjy" +
#  "ljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnh" +
#  "rptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddv" +
#  "dlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxj" +
#  "hsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd"),
# ["iowuuudrgzmw",
#  "azfcxtvhkruvuturdicnucvndigovkzrq",
#  "ylmmo",
#  "maptilrbfpjxiarmwalhbd",
#  "oqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqgl",
#  "ytldcdlxqbaszbuxsacqwqnhrewhagldzhr",
#  "zeeab",
#  "cqie",
#  "pvrazfcxtvhkruvuturdicnucvndigovkzrqiya",
#  "zxnvpluwicurrtshyvevkriudayyysepzq",
#  "wyhxltligahroyshfn",
#  "nhrewhagldzhryzdmmrwn",
#  "yqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmw",
#  "nhrptuugyfsghluythksqhmxlmggtcbdd",
#  "yligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjsc",
#  "zdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzq",
#  "ncygycdpehteiugqbptyqbvokpwovbnplshnzafun",
#  "gdzutwgjofowhryrubnxkahocqjzww",
#  "eppapjoliqlhbrbgh",
#  "qwhgobwyhxltligahroys",
#  "dzutwgjofowhryrubnxkah",
#  "rydhxkdhffyytldcdlxqbaszbuxs",
#  "tyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjc",
#  "khvyjyrydhxkdhffyytldcdlxqbasz",
#  "jajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqn",
#  "ppapjoliqlhbrbghq",
#  "zmwwxzjckmaptilrbfpjxiarm",
#  "nxkahocqjzwwagqidjhwbunvlchoj",
#  "ybfxpvqywqjdlyznmojdhbeomyjqptltp",
#  "udrgzmwnxae",
#  "nqglnpjvwddvdlmjjyzmww",
#  "swlvtlbmkrsurrcsgdzutwgjofowhryrubn",
#  "hudqbfnzxnvpluwicurr",
#  "xaezuqlsfvchjf",
#  "tvibbwxnokzkhndmdhweyeycamjeplec",
#  "olnswlvtlbmkrsurrcsgdzu",
#  "qiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyyt",
#  "eiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwyl",
#  "cgiowuuudrgzmwnxaezuqlsfvchjflocz",
#  "rxric",
#  "cygycdpehteiugqbptyqbvokpwovbnplshnzaf",
#  "g",
#  "surrcsgd",
#  "yzenflfnhrptuugyfsghluythksqh",
#  "gdzutwgjofowhryrubnxkahocqjzwwagqid",
#  "ddeoincygycdpeh",
#  "yznmojdhbeomyjqptltpugzceyzenflfnhrptuug",
#  "ejuisks",
#  "teiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoi",
#  "mrwnxhaqfezeeabuacyswollycgio",
#  "qfskkpfakjretogrokmxemjjbvgmmqrfdxlkfvycwalbdeumav",
#  "wjgjhlrpvhqozvvkifhftnfqcfjmmzhtxsoqbeduqmnpvimagq",
#  "ibxhtobuolmllbasaxlanjgalgmbjuxmqpadllryaobcucdeqc",
#  "ydlddogzvzttizzzjohfsenatvbpngarutztgdqczkzoenbxzv",
#  "rmsakibpprdrttycxglfgtjlifznnnlkgjqseguijfctrcahbb",
#  "pqquuarnoybphojyoyizhuyjfgwdlzcmkdbdqzatgmabhnpuyh",
#  "akposmzwykwrenlcrqwrrvsfqxzohrramdajwzlseguupjfzvd",
#  "vyldyqpvmnoemzeyxslcoysqfpvvotenkmehqvopynllvwhxzr",
#  "ysyskgrbolixwmffygycvgewxqnxvjsfefpmxrtsqsvpowoctw",
#  "oqjgumitldivceezxgoiwjgozfqcnkergctffspdxdbnmvjago",
#  "bpfgqhlkvevfazcmpdqakonkudniuobhqzypqlyocjdngltywn",
#  "ttucplgotbiceepzfxdebvluioeeitzmesmoxliuwqsftfmvlg",
#  "xhkklcwblyjmdyhfscmeffmmerxdioseybombzxjatkkltrvzq",
#  "qkvvbrgbzzfhzizulssaxupyqwniqradvkjivedckjrinrlxgi",
#  "itjudnlqncbspswkbcwldkwujlshwsgziontsobirsvskmjbrq",
#  "nmfgxfeqgqefxqivxtdrxeelsucufkhivijmzgioxioosmdpwx",
#  "ihygxkykuczvyokuveuchermxceexajilpkcxjjnwmdbwnxccl",
#  "etvcfbmadfxlprevjjnojxwonnnwjnamgrfwohgyhievupsdqd",
#  "ngskodiaxeswtqvjaqyulpedaqcchcuktfjlzyvddfeblnczmh",
#  "vnmntdvhaxqltluzwwwwrbpqwahebgtmhivtkadczpzabgcjzx",
#  "yjqqdvoxxxjbrccoaqqspqlsnxcnderaewsaqpkigtiqoqopth",
#  "wdytqvztzbdzffllbxexxughdvetajclynypnzaokqizfxqrjl",
#  "yvvwkphuzosvvntckxkmvuflrubigexkivyzzaimkxvqitpixo",
#  "lkdgtxmbgsenzmrlccmsunaezbausnsszryztfhjtezssttmsr",
#  "idyybesughzyzfdiibylnkkdeatqjjqqjbertrcactapbcarzb",
#  "ujiajnirancrfdvrfardygbcnzkqsvujkhcegdfibtcuxzbpds",
#  "jjtkmalhmrknaasskjnixzwjgvusbozslrribgazdhaylaxobj",
#  "nizuzttgartfxiwcsqchizlxvvnebqdtkmghtcyzjmgyzszwgi",
#  "egtvislckyltpfogtvfbtxbsssuwvjcduxjnjuvnqyiykvmrxl",
#  "ozvzwalcvaobxbicbwjrububyxlmfcokdxcrkvuehbnokkzala",
#  "azhukctuheiwghkalboxfnuofwopsrutamthzyzlzkrlsefwcz",
#  "yhvjjzsxlescylsnvmcxzcrrzgfhbsdsvdfcykwifzjcjjbmmu",
#  "tspdebnuhrgnmhhuplbzvpkkhfpeilbwkkbgfjiuwrdmkftphk",
#  "jvnbeqzaxecwxspuxhrngmvnkvulmgobvsnqyxdplrnnwfhfqq",
#  "bcbkgwpfmmqwmzjgmflichzhrjdjxbcescfijfztpxpxvbzjch",
#  "bdrkibtxygyicjcfnzigghdekmgoybvfwshxqnjlctcdkiunob",
#  "koctqrqvfftflwsvssnokdotgtxalgegscyeotcrvyywmzescq",
#  "boigqjvosgxpsnklxdjaxtrhqlyvanuvnpldmoknmzugnubfoa",
#  "jjtxbxyazxldpnbxzgslgguvgyevyliywihuqottxuyowrwfar",
#  "zqsacrwcysmkfbpzxoaszgqqsvqglnblmxhxtjqmnectaxntvb",
#  "izcakfitdhgujdborjuhtwubqcoppsgkqtqoqyswjfldsbfcct",
#  "rroiqffqzenlerchkvmjsbmoybisjafcdzgeppyhojoggdlpzq",
#  "xwjqfobmmqomhczwufwlesolvmbtvpdxejzslxrvnijhvevxmc",
#  "ccrubahioyaxuwzloyhqyluwoknxnydbedenrccljoydfxwaxy",
#  "jjoeiuncnvixvhhynaxbkmlurwxcpukredieqlilgkupminjaj",
#  "pdbsbjnrqzrbmewmdkqqhcpzielskcazuliiatmvhcaksrusae",
#  "nizbnxpqbzsihakkadsbtgxovyuebgtzvrvbowxllkzevktkuu",
#  "hklskdbopqjwdrefpgoxaoxzevpdaiubejuaxxbrhzbamdznrr",
#  "uccnuegvmkqtagudujuildlwefbyoywypakjrhiibrxdmsspjl",
#  "awinuyoppufjxgqvcddleqdhbkmolxqyvsqprnwcoehpturicf"])