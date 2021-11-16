from typing import List, Set
from unittest import TestCase
tc = TestCase()

class Solution:
    # This uses iterative DFS with a stack. It's also quite slow, according to Leetcode
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        board_ints = [[ord(col) - 97 for col in row] for row in board]
        m = len(board_ints)
        n = len(board_ints[0])
        results = set()
        for i in range(m):
            for j in range(n):
                if trie.head.next[board_ints[i][j]] is not None:
                    self.helper(board_ints, i, j, m, n, trie.head.next[board_ints[i][j]], results)

        return list(results)

    def helper(self, board, i: int, j: int, m: int, n: int, t: 'TrieNode', results: Set[str]):
        stack = [(i, j, t)]

        visited = dict()
        for ii in range(m):
            for jj in range(n):
                visited[(ii,jj)] = False

        # was stuck for a while, but fixed after seeing https://leetcode.com/problems/word-search-ii/discuss/733402/Python-Trie-Iterative-Dfs
        while stack:
            ni, nj, nt = stack[-1]
            # already visited, mark it as unvisited and continue to next iteration of loop
            if visited[(ni,nj)] == True:
                visited[(ni, nj)] = False
                stack.pop()
                continue

            visited[(ni, nj)] = True

            if nt.end:
                # print("found a match", nt.word)
                results.add(nt.word)

            for nix, njy in [(ni-1,nj),(ni+1,nj),(ni,nj-1),(ni,nj+1)]:
                if 0 <= nix < m and 0 <= njy < n \
                    and visited[(nix,njy)] == False \
                    and nt.next[board[nix][njy]] is not None:
                    # print("appending", nix, njy, board[nix][njy], stack)
                    stack.append((nix, njy, nt.next[board[nix][njy]]))

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        c = self.head
        for letter in word:
            i = ord(letter) - 97 # ord("a")
            if c.next[i] is None:
                c.next[i] = TrieNode()
            c = c.next[i]
        c.word = word
        c.end = True

class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.word = None
        self.end = False

    def __repr__(self): return "T"

s = Solution()

b1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
w1 = ["oath","pea","eat","rain"]
tc.assertCountEqual(s.findWords(b1, w1), ["oath", "eat"])

b2 = [["a","b","c"],["a","e","d"],["a","f","g"]]
w2 = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
tc.assertCountEqual(s.findWords(b2, w2), ["abcdefg","befa","eaabcdgfa","gfedcbaaa"])

b3 = [["a", "b", "c"],["a","a","d"]]
w3 = ["ababab"]
assert s.findWords(b3, w3) == []

b4 = [["b","a","b","a","b","a","b","a","b","a"]
     ,["a","b","a","b","a","b","a","b","a","b"]
     ,["b","a","b","a","b","a","b","a","b","a"]
     ,["a","b","a","b","a","b","a","b","a","b"]
     ,["b","a","b","a","b","a","b","a","b","a"]
     ,["a","b","a","b","a","b","a","b","a","b"]
     ,["b","a","b","a","b","a","b","a","b","a"]
     ,["a","b","a","b","a","b","a","b","a","b"]
     ,["b","a","b","a","b","a","b","a","b","a"]
     ,["a","b","a","b","a","b","a","b","a","b"]]

w4 = ["aababababa","abbabababa","acbabababa","adbabababa","aebabababa","afbabababa","agbabababa"
     ,"ahbabababa","aibabababa","ajbabababa","akbabababa","albabababa","ambabababa","anbabababa"
     ,"aobabababa","apbabababa","aqbabababa","arbabababa","asbabababa","atbabababa","aubabababa"
     ,"avbabababa","awbabababa","axbabababa","aybabababa","azbabababa","bababababa","bbbabababa"
     ,"bcbabababa","bdbabababa","bebabababa","bfbabababa","bgbabababa","bhbabababa","bibabababa"
     ,"bjbabababa","bkbabababa","blbabababa","bmbabababa","bnbabababa","bobabababa","bpbabababa"
     ,"bqbabababa","brbabababa","bsbabababa","btbabababa","bubabababa","bvbabababa","bwbabababa"
     ,"bxbabababa","bybabababa","bzbabababa","cababababa","cbbabababa","ccbabababa","cdbabababa"
     ,"cebabababa","cfbabababa","cgbabababa","chbabababa","cibabababa","cjbabababa","ckbabababa"
     ,"clbabababa","cmbabababa","cnbabababa","cobabababa","cpbabababa","cqbabababa","crbabababa"
     ,"csbabababa","ctbabababa","cubabababa","cvbabababa","cwbabababa","cxbabababa","cybabababa"
     ,"czbabababa","dababababa","dbbabababa","dcbabababa","ddbabababa","debabababa","dfbabababa"
     ,"dgbabababa","dhbabababa","dibabababa","djbabababa","dkbabababa","dlbabababa","dmbabababa"
     ,"dnbabababa","dobabababa","dpbabababa","dqbabababa","drbabababa","dsbabababa","dtbabababa"
     ,"dubabababa","dvbabababa","dwbabababa","dxbabababa","dybabababa","dzbabababa","eababababa"
     ,"ebbabababa","ecbabababa","edbabababa","eebabababa","efbabababa","egbabababa","ehbabababa"
     ,"eibabababa","ejbabababa","ekbabababa","elbabababa","embabababa","enbabababa","eobabababa"
     ,"epbabababa","eqbabababa","erbabababa","esbabababa","etbabababa","eubabababa","evbabababa"
     ,"ewbabababa","exbabababa","eybabababa","ezbabababa","fababababa","fbbabababa","fcbabababa"
     ,"fdbabababa","febabababa","ffbabababa","fgbabababa","fhbabababa","fibabababa","fjbabababa"
     ,"fkbabababa","flbabababa","fmbabababa","fnbabababa","fobabababa","fpbabababa","fqbabababa"
     ,"frbabababa","fsbabababa","ftbabababa","fubabababa","fvbabababa","fwbabababa","fxbabababa"
     ,"fybabababa","fzbabababa","gababababa","gbbabababa","gcbabababa","gdbabababa","gebabababa"
     ,"gfbabababa","ggbabababa","ghbabababa","gibabababa","gjbabababa","gkbabababa","glbabababa"
     ,"gmbabababa","gnbabababa","gobabababa","gpbabababa","gqbabababa","grbabababa","gsbabababa"
     ,"gtbabababa","gubabababa","gvbabababa","gwbabababa","gxbabababa","gybabababa","gzbabababa"
     ,"hababababa","hbbabababa","hcbabababa","hdbabababa","hebabababa","hfbabababa","hgbabababa"
     ,"hhbabababa","hibabababa","hjbabababa","hkbabababa","hlbabababa","hmbabababa","hnbabababa"
     ,"hobabababa","hpbabababa","hqbabababa","hrbabababa","hsbabababa","htbabababa","hubabababa"
     ,"hvbabababa","hwbabababa","hxbabababa","hybabababa","hzbabababa","iababababa","ibbabababa"
     ,"icbabababa","idbabababa","iebabababa","ifbabababa","igbabababa","ihbabababa","iibabababa"
     ,"ijbabababa","ikbabababa","ilbabababa","imbabababa","inbabababa","iobabababa","ipbabababa"
     ,"iqbabababa","irbabababa","isbabababa","itbabababa","iubabababa","ivbabababa","iwbabababa"
     ,"ixbabababa","iybabababa","izbabababa","jababababa","jbbabababa","jcbabababa","jdbabababa"
     ,"jebabababa","jfbabababa","jgbabababa","jhbabababa","jibabababa","jjbabababa","jkbabababa"
     ,"jlbabababa","jmbabababa","jnbabababa","jobabababa","jpbabababa","jqbabababa","jrbabababa"
     ,"jsbabababa","jtbabababa","jubabababa","jvbabababa","jwbabababa","jxbabababa","jybabababa"
     ,"jzbabababa","kababababa","kbbabababa","kcbabababa","kdbabababa","kebabababa","kfbabababa"
     ,"kgbabababa","khbabababa","kibabababa","kjbabababa","kkbabababa","klbabababa","kmbabababa"
     ,"knbabababa","kobabababa","kpbabababa","kqbabababa","krbabababa","ksbabababa","ktbabababa"
     ,"kubabababa","kvbabababa","kwbabababa","kxbabababa","kybabababa","kzbabababa","lababababa"
     ,"lbbabababa","lcbabababa","ldbabababa","lebabababa","lfbabababa","lgbabababa","lhbabababa"
     ,"libabababa","ljbabababa","lkbabababa","llbabababa","lmbabababa","lnbabababa","lobabababa"
     ,"lpbabababa","lqbabababa","lrbabababa","lsbabababa","ltbabababa","lubabababa","lvbabababa"
     ,"lwbabababa","lxbabababa","lybabababa","lzbabababa","mababababa","mbbabababa","mcbabababa"
     ,"mdbabababa","mebabababa","mfbabababa","mgbabababa","mhbabababa","mibabababa","mjbabababa"
     ,"mkbabababa","mlbabababa","mmbabababa","mnbabababa","mobabababa","mpbabababa","mqbabababa"
     ,"mrbabababa","msbabababa","mtbabababa","mubabababa","mvbabababa","mwbabababa","mxbabababa"
     ,"mybabababa","mzbabababa","nababababa","nbbabababa","ncbabababa","ndbabababa","nebabababa"
     ,"nfbabababa","ngbabababa","nhbabababa","nibabababa","njbabababa","nkbabababa","nlbabababa"
     ,"nmbabababa","nnbabababa","nobabababa","npbabababa","nqbabababa","nrbabababa","nsbabababa"
     ,"ntbabababa","nubabababa","nvbabababa","nwbabababa","nxbabababa","nybabababa","nzbabababa"
     ,"oababababa","obbabababa","ocbabababa","odbabababa","oebabababa","ofbabababa","ogbabababa"
     ,"ohbabababa","oibabababa","ojbabababa","okbabababa","olbabababa","ombabababa","onbabababa"
     ,"oobabababa","opbabababa","oqbabababa","orbabababa","osbabababa","otbabababa","oubabababa"
     ,"ovbabababa","owbabababa","oxbabababa","oybabababa","ozbabababa","pababababa","pbbabababa"
     ,"pcbabababa","pdbabababa","pebabababa","pfbabababa","pgbabababa","phbabababa","pibabababa"
     ,"pjbabababa","pkbabababa","plbabababa","pmbabababa","pnbabababa","pobabababa","ppbabababa"
     ,"pqbabababa","prbabababa","psbabababa","ptbabababa","pubabababa","pvbabababa","pwbabababa"
     ,"pxbabababa","pybabababa","pzbabababa","qababababa","qbbabababa","qcbabababa","qdbabababa"
     ,"qebabababa","qfbabababa","qgbabababa","qhbabababa","qibabababa","qjbabababa","qkbabababa"
     ,"qlbabababa","qmbabababa","qnbabababa","qobabababa","qpbabababa","qqbabababa","qrbabababa"
     ,"qsbabababa","qtbabababa","qubabababa","qvbabababa","qwbabababa","qxbabababa","qybabababa"
     ,"qzbabababa","rababababa","rbbabababa","rcbabababa","rdbabababa","rebabababa","rfbabababa"
     ,"rgbabababa","rhbabababa","ribabababa","rjbabababa","rkbabababa","rlbabababa","rmbabababa"
     ,"rnbabababa","robabababa","rpbabababa","rqbabababa","rrbabababa","rsbabababa","rtbabababa"
     ,"rubabababa","rvbabababa","rwbabababa","rxbabababa","rybabababa","rzbabababa","sababababa"
     ,"sbbabababa","scbabababa","sdbabababa","sebabababa","sfbabababa","sgbabababa","shbabababa"
     ,"sibabababa","sjbabababa","skbabababa","slbabababa","smbabababa","snbabababa","sobabababa"
     ,"spbabababa","sqbabababa","srbabababa","ssbabababa","stbabababa","subabababa","svbabababa"
     ,"swbabababa","sxbabababa","sybabababa","szbabababa","tababababa","tbbabababa","tcbabababa"
     ,"tdbabababa","tebabababa","tfbabababa","tgbabababa","thbabababa","tibabababa","tjbabababa"
     ,"tkbabababa","tlbabababa","tmbabababa","tnbabababa","tobabababa","tpbabababa","tqbabababa"
     ,"trbabababa","tsbabababa","ttbabababa","tubabababa","tvbabababa","twbabababa","txbabababa"
     ,"tybabababa","tzbabababa","uababababa","ubbabababa","ucbabababa","udbabababa","uebabababa"
     ,"ufbabababa","ugbabababa","uhbabababa","uibabababa","ujbabababa","ukbabababa","ulbabababa"
     ,"umbabababa","unbabababa","uobabababa","upbabababa","uqbabababa","urbabababa","usbabababa"
     ,"utbabababa","uubabababa","uvbabababa","uwbabababa","uxbabababa","uybabababa","uzbabababa"
     ,"vababababa","vbbabababa","vcbabababa","vdbabababa","vebabababa","vfbabababa","vgbabababa"
     ,"vhbabababa","vibabababa","vjbabababa","vkbabababa","vlbabababa","vmbabababa","vnbabababa"
     ,"vobabababa","vpbabababa","vqbabababa","vrbabababa","vsbabababa","vtbabababa","vubabababa"
     ,"vvbabababa","vwbabababa","vxbabababa","vybabababa","vzbabababa","wababababa","wbbabababa"
     ,"wcbabababa","wdbabababa","webabababa","wfbabababa","wgbabababa","whbabababa","wibabababa"
     ,"wjbabababa","wkbabababa","wlbabababa","wmbabababa","wnbabababa","wobabababa","wpbabababa"
     ,"wqbabababa","wrbabababa","wsbabababa","wtbabababa","wubabababa","wvbabababa","wwbabababa"
     ,"wxbabababa","wybabababa","wzbabababa","xababababa","xbbabababa","xcbabababa","xdbabababa"
     ,"xebabababa","xfbabababa","xgbabababa","xhbabababa","xibabababa","xjbabababa","xkbabababa"
     ,"xlbabababa","xmbabababa","xnbabababa","xobabababa","xpbabababa","xqbabababa","xrbabababa"
     ,"xsbabababa","xtbabababa","xubabababa","xvbabababa","xwbabababa","xxbabababa","xybabababa"
     ,"xzbabababa","yababababa","ybbabababa","ycbabababa","ydbabababa","yebabababa","yfbabababa"
     ,"ygbabababa","yhbabababa","yibabababa","yjbabababa","ykbabababa","ylbabababa","ymbabababa"
     ,"ynbabababa","yobabababa","ypbabababa","yqbabababa","yrbabababa","ysbabababa","ytbabababa"
     ,"yubabababa","yvbabababa","ywbabababa","yxbabababa","yybabababa","yzbabababa","zababababa"
     ,"zbbabababa","zcbabababa","zdbabababa","zebabababa","zfbabababa","zgbabababa","zhbabababa"
     ,"zibabababa","zjbabababa","zkbabababa","zlbabababa","zmbabababa","znbabababa","zobabababa"
     ,"zpbabababa","zqbabababa","zrbabababa","zsbabababa","ztbabababa","zubabababa","zvbabababa"
     ,"zwbabababa","zxbabababa","zybabababa","zzbabababa"]

assert s.findWords(b4, w4) == ["bababababa"]