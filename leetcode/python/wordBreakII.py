# https://oj.leetcode.com/problems/word-break-ii/

# memoized DFS
class Solution:
  def wordBreak(self, s, dict):
    if (len(dict) == 0):
      return []
    self.cache = {}
    # self.maxLen = max(map(lambda x: len(x), iter(dict)))
    self.minLen = min(map(lambda x: len(x), iter(dict)))
    self.lens = set(map(lambda x: len(x), iter(dict)))
    return map(lambda x: ' '.join(x), self.walk(s, dict))

  def walk(self, s, dict):
    if s in self.cache:
      return self.cache[s]

    result = []
    if len(s) <= self.minLen:
      if s in dict:
        result = [[s]]
    else:
      result = {}
      size = len(s)
      for i in self.lens:
        if i >= size:
          continue
        firstList = self.walk(s[0:i], dict)
        secondList = self.walk(s[i:], dict)
        for firstItem in firstList:
          for secondItem in secondList:
            item = firstItem + secondItem
            result[':'.join(item)] = item
      if s in dict:
        result[s] = [s]
      result = result.values()
    self.cache[s] = result

    return result

inputs = [{
  's': "catsanddog",
  'dict': ["cat", "cats", "and", "sand", "dog"]
  },
  {
    's': "aaaaaaaab",
    'dict': ["a", "aa", "aaa", "aaaa", "aaaaaa", "aaaaaaa"]
  },
  {
    's': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    'dict': ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
  },
  {
    's': "bb",
    'dict': ["a","b","bbb","bbbb"]
  },
  {
    's': "fkjjlbhkbbefinemajmoebhjbkojmcaehiibankkomghncojbjgedebjfdocjhclmbalebladkcaidacaiiokemdmaabjalmbgggjjfjfedegmnkidceogjdgncmlhodkcmjkfolgfnaklkjbocjhhakgmigkcmilbikbhjcgz",
    'dict': ["gaggkdeo","igkcmil","mfljaieijcjk","nddenji","ihkao","k","halnhbcmabjb","aeb","hmamkhmlfce","mnkjgjjodida","gm","hancobi","g","hmoafjnono","meanolmbloog","nochomliagledo","ahdimafaacc","necn","goicmonlkil","jfigiglloi","jjfjfede","akgjlbgjldec","oooij","dk","elbofj","mmddfkfig","kaklf","bcbeenfeee","ajkooijb","oaanehdai","e","omk","mfmed","iheidmbjeinfebk","bikbhjcg","eh","hmbneijnk","cccganlndjo","igfmdoiihc","edoncgeohal","i","glie","ncojbjg","gnmifoifaec","ncogocd","kgogljaidon","dkghjha","mf","fmoimobjf","incmj","ihiehafnmilce","hji","daoklglc","obbomj","fh","f","mnmbhk","jaj","ikbdlhfhk","lihmboinijkkka","cda","boimoc","iohgjocn","gaof","lld","jhhak","jhjekma","jedihdccoojide","anibdmo","dfdgfnmldhaooae","nohgoc","jjlmggdbhno","odkimohjodbh","dmhkkgjcjhiid","fcdgbjgbbm","mhoomlad","nbofdoofom","cencoc","aefehagm","nnio","jjiigmc","cgel","ela","hhd","jkkddacaam","b","mo","md","damiock","ebeao","aab","dijb","mlbcnljogof","lnjadlm","ijgcicndm","cgnblkchngklbf","jbebfgk","hdjg","dl","honjckb","cdomnnhjocaoe","ebnje","igkgjalnbhinghi","iojginhi","fmmdnnjobikond","jeflgnl","noodabd","ojgd","nfkjdggjn","kajbdaikidneidm","klbjfcfjlkcibba","geecdcfbkede","ndjbgdadje","mokfehacdd","mjdkenofkaeli","mcmnj","mfggccd","nmonjefcjolhfgg","amdfecagjfkfdh","kbijncaeoon","febfhfjgkhdab","bgglmgmkjhne","mhhojoihflf","dfaffjcdnchb","mnh","fjcikedcd","odd","j","kjafgaiklcemkcd","lnhgochigmcgk","fnhijgnend","gniekccclcn","ofggcjlidbjeh","aojegacnehgbdgc","bbabogkdekleei","egcmokhdio","inl","fleeid","mmdcekhihfc","ckbbhaaoakfe","nadbaeddfjej","finiacgd","khid","haaiani","hekleijlafocdh","jihfh","aolhnacokig","nnggoafjl","fkhjghiaeojhi","oan","aajimcikcnaebe","achigecoboif","cjhed","ijhg","oonjh","allhnelgjdl","abh","cabncchfmbn","khnciickdoehol","jnof","bfmalenhf","bckmd","haln","iaiffadaadji","hoadjf","nagchlghjhk","hjlbacedkkdnk","ace","bmldoimodegcl","mdiojfhgmfg","omkblifelkfifjn","amnldcmobkkjmkj","iaibe","efnn","nmbf","a","foenajo","jgnkhn","ncagcgnfcfm","confnibafdeiiad","cdjgakfn","lmh","nlabndn","n","kc","gddjoojoeomanj","kmf","hj","jgnijhekbmbcbk","gjhfei","bfiladjlggjjh","fckgfmdeikdkkfi","abnldlg","fgnnjefaegg","mochafeafehelb","ncbdkecddnegbko","ceedljkegf","okhdgjkao","dfdcocheclaaj","ladkcaida","klfkbnbjeg","bihmahlknalkbb","gobo","edggcafghgbokfg","lfcdahkamfnnlbe","fhobdnbh","fllibcljdmajn","obhlnghf","njbcm","kmkbnlldhadfc","ghmk","ijbeihkojjml","clmbaleb","offmicbgejkh","hmmjfbkh","jkfehdlek","gbk","gmocchifcgmofhd","lbc","anicc","ejhddgheln","nemajmoebhjbkoj","naemi","nnenmabkhlm","bjhb","jmjhmnjkgh","admjcjbca","llem","hkbbe","nmdjmkjhdja","koniblnljgmmbbg","biljfalmflchb","dblnhfib","ok","emilcjdncm","ilfkbiodab","eoohdfhno","dgd","o","mbjj","legdidaoclb","nghlkbkbbljh","ekabk","ggkgfkbomme","ogfmlfcaklef","ikgg","kghbdjieniho","noighlblehf","jfmgihkonmbm","bimicdfhlifg","klimcfnojbiooc","lakbda","mkcoboaddi","nfaebmd","fbjlahcaajamjaj","gncllkii","fboglhliehal","jk","ocimnaceklgmoe","fcnh","ohcnnkamoaom","ccimaiofdealnjf","mkdanlkeekecc","hamboelbcdbai","lbljfeianmkhon","bhjbndfffcdhm","nafgoeceilmebn","jmb","fmmfmdmnigllb","dbaobkconcfcan","ajdibacdfg","iknhfe","abdaeca","l","becafg","eeieaeoiaagjbdi","odgfeca","anbceegkdn","bknkeonigb","fj","kacanki","jlkoncijbo","kaeobkadncbgn","eagocnmnjjhnlmh","adnnllieng","imlkbgfmolmj","nlmnkngheaof","kcockjm","ggmfbilldo","abagjicencjdhh","gedckmkehn","ijecleakkbndgl","joifkiccb","aiameogbecidakj","jdaiilnfh","kgdond","bnecbmebab","mfmlijibjdcoddh","nlcbiiejklclf","jlijddomde","gniiehcllnm","amj","fbcclace","ainmcmmhbc","cglfdaklhmmocl","hfkfdfkmlkai","hkfjjhejacc","kgm","anbhgnjhjfabiok","bdhmgigjbj","dokmfnldohbgk","cg","bgmkhfd","dfj","gjhd","idkmgmmnaejkdel","gekmbmmn","hccecjfbfij","cfek","fjeoegjlmligac","alhnjlacob","liedbjcj","adlif","okddmo","lgbkmbek","oobncia","moobafgelbmlehnc","jialklmcdlohkm","jbimboeijnbmgol","nndgm","hebjao","cijlobchgka","hljojiclje","gdb","kamgaigodfcbk","mi","lcjalnfojcmjbl","mdkmocngibmgnjb","fobhhgdf","dekdcobbeghi","elofjhgeackijdk","abjal","glnnkdccgi","kbcjlljgdnnbmi","bg","jnoffjafmaa","h","knhefdjjlaife","nbalab","jkhd","neaofeanlcidni","bdckcnlkbo","fkj","ihlknj","iggdjfk","nmmkjg","jhmimaem","minieag","fofgj","jafebbgi","cbanbcaknggl","nkncbcjlidilefo","filngail","oocb","hdhliiikjfhm","hfmaiekfb","af","hfjemfchd","hainei","mehfggjbghiomni","lcjnmbclgbin","djeokdahia","lh","lfbfoj","aohgcfcmbhmek","clfbgjichnmfa","chieogij","fglg","accifaokkgmnb","iamjljccnihcn","idocdnlj","dh","clhmcifbgcjf","bjmlcfhdjocgl","nbhajeoi","adeaadndhie","mlheaedi","jdbgkfadelbejhg","ohlecggkboamn","boinmneifn","angj","hoclbcdofng","gkjcegiifa","lakke","gfa","nnimh","iikjgcmfbagd","fefgjd","eeboefdackceb","mmkccjei","hloiook","hcge","gmhncohdjkk","clmkcojajn","ogjdgncmlh","dfookkmceiigmh","fhkjcimkiofoinn","mjahgdgnabdj","hb","obkkbdcjglm","le","cmninbjdhekcb","oodikoamlelcne","bnbafkkddmk","neagoocl","bhmdmlejaiji","mjlbealgl","cafnnmniln","labfg","leelb","ocifbibijfgdk","dbbb","ghbmcg","mom","igo","jcmfoebajefjdi","iikgmjn","obnckkadabjhfi","lhekmhildjkcn","njfogfnj","fcgacdhcclde","ichaeligmk","hmcjoigoea","cc","ickfcelfilkbk","ch","jkakkdlh","fkjjlb","dkcknlo","lc","nklohjhjif","jhgkjjfcjefc","kalkc","meglmnhlnem","lnbmmcbdgfkeem","ejkbobfilcnafel","lk","jlbncfd","eblmooggngamof","okmmomdmief","dahc","ackmjhnmfgaoafa","fmjgi","dbmflmfkdia","aeajncek","ehalibdilikeok","mnjojhdjngin","m","hfdlmjjcfmacb","ekciad","dkdfmnieiahio","nihfnbekbhk","okj","mmjf","anfjk","kocaoh","amfcflnla","jealekjf","fgokkddmfa","ffbbabn","okldhifhnhbm","edmaga","ajahiocomhbablk","danmbn","ilcjcheddnabll","ochfblfeldbo","ignhkon","meiailaib","aheodadm","dec","ianoghmba","bni","cenegah","jcnkiciendihdih","kegkcmnkh","fi","aeldnnmcbilelg","emejaicfjhafod","jjonddlecfgdm","elkcmmlfbiemeg","edebjfdocjh","ankghmibmgd","afmmgmi","afliaf","aecckchdf","mcnhfojki","la","blbaif","bifj","nkidce","ddhigddihlkm","bgjnn","haclkkjbjdjn","mcaehiiba","iebnfadil","kfgjab","bafdkg","gnbbgilljiacl","fdajjg","caiiokemdma","adfchcjninhho","meaaf","jahifegbhjj","hbhgkdl","egomnbc","ooccmbmicehi","afaecdcbjgf","mcaedecih","ihjnbgacjahfmj","hcnco","hbecolgk","jdknfnmjehoc","mnmbndjkono","mk","kmmcjjeab","lekbo","mcbaknmkcnebj","mbggg","men","jn","hgcchmkje","ncnlijanmcog","hll","jlhkhiggelnkhbk","bnoaah","enainmmdaamaicn","jieio","anadihbcbg","ligl","fmjkjmgmjmlonel","gifkkbkedeno","hmklhikf","jeoll","kbhi","cnkihoga","ihkndcibcgl","deogdlmcbc","mocghlg","gkaihhoa","miibddoebolibnc","ggecjoiodklb","nafdahhn","meboilne","olkhhkledm","hdklcdfmne","aclj","migeheccjgod","cejnilnhfadml","mfkmacdgomhcalm","faijmldniblnl","mmfcln","lhmdehaho","hcj","fkconhlmknloccn","hckhl","lheki","blenkofhj","bhjjgkmblen","dndjigjgikb","jnjamjglhim","hg","bnlbgllnkfemfgj","ll","hjekhnhnoam","mldahadgmegj","dmj","henklighfkah","lcl","lobhgifjflgcicc","chnfjdeije","jbaedijcdm","jcinegma","oojiijjcdh","bkejicnojmlj","jncnoc","embdomh","chkjonad","eekgln","aodogkkmodaoc","ee","ngnmdfldf","eajlnmjeckeek","lnnaiggam","hlohol","nibflancimmfk"]
  },
  {
    's': "aaaaaaa",
    'dict': ["aaaa","aa","a"]
  }
  ]

s = Solution()
for item in inputs:
  print s.wordBreak(item['s'], item['dict'])
