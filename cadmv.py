# coding: utf-8

# Check the first available appointment date for a CA DMV office

# @author williamchai
# @version Aug 21, 2014

import urllib,urllib2,re,pickle

class Result:
    officeId=officeName=firstDate=None

def getPage(url, dataDic=None):
    html = ''; data = ''
    if dataDic:
        data = urllib.urlencode(dataDic)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24"}
    req = urllib2.Request(url, data, header)
    try:
        # print 'urlopen...'
        f = urllib2.urlopen(req, timeout=10)
        # if f.getcode()!=200:
        #     pass # HTTP error
        html = f.read()
    except Exception, e:
        if isinstance(e, urllib2.HTTPError):
            print 'HTTP Error: %s' % e.code
        else:
            print 'Error:', str(e)
    # print 'read finish'
    return html

def getAppDate(officeId=617):
    url = 'https://www.dmv.ca.gov/wasapp/foa/findOfficeVisit.do'
    form = {'officeId':officeId, 'numberItems':1, 'taskDL':'true', 'firstName':'y', 'lastName':'c', 'telArea':'213', 'telPrefix':'213', 'telSuffix':'2133', 'resetCheckFields':'true'}
    html = getPage(url, form)
    if not html:
        return
    
    html=html.replace('\n','')
    # print 'start matching...'
    pattern = re.compile(r'The first available appointment for this office is on.*?<p class="alert">(.*?)</p>')
    results = re.search(pattern, html)
    if results:
        return results.group(1)
    print 'Not found'

# return (id,name) pairs list
def getAllId():
    return [
    (587, 'ARLETA'),
    (661, 'ARVIN'),
    (570, 'AUBURN'),
    (529, 'BAKERSFIELD'),
    (679, 'BAKERSFIELD SW'),
    (641, 'BANNING'),
    (582, 'BARSTOW'),
    (576, 'BELL GARDENS'),
    (606, 'BELLFLOWER'),
    (585, 'BISHOP'),
    (528, 'BLYTHE'),
    (597, 'BRAWLEY'),
    (550, 'CAPITOLA'),
    (625, 'CARMICHAEL'),
    (520, 'CHICO'),
    (613, 'CHULA VISTA'),
    (580, 'CLOVIS'),
    (603, 'COALINGA'),
    (564, 'COLUSA'),
    (581, 'COMPTON'),
    (523, 'CONCORD'),
    (534, 'CORTE MADERA'),
    (628, 'COSTA MESA'),
    (524, 'CRESCENT CITY'),
    (514, 'CULVER CITY'),
    (599, 'DALY CITY'),
    (598, 'DAVIS'),
    (615, 'DELANO'),
    (669, 'EL CAJON'),
    (527, 'EL CENTRO'),
    (556, 'EL CERRITO'),
    (685, 'EL MONTE'),
    (526, 'EUREKA'),
    (621, 'FAIRFIELD'),
    (643, 'FALL RIVER MILLS'),
    (655, 'FOLSOM'),
    (657, 'FONTANA'),
    (590, 'FORT BRAGG'),
    (644, 'FREMONT'),
    (505, 'FRESNO'),
    (646, 'FRESNO NORTH'),
    (607, 'FULLERTON'),
    (627, 'GARBERVILLE'),
    (623, 'GILROY'),
    (510, 'GLENDALE'),
    (670, 'GOLETA'),
    (541, 'GRASS VALLEY'),
    (565, 'HANFORD'),
    (609, 'HAWTHORNE'),
    (579, 'HAYWARD'),
    (635, 'HEMET'),
    (546, 'HOLLISTER'),
    (508, 'HOLLYWOOD'),
    (652, 'HOLLYWOOD WEST'),
    (578, 'INDIO'),
    (610, 'INGLEWOOD'),
    (521, 'JACKSON'),
    (647, 'KING CITY'),
    (605, 'LAGUNA HILLS'),
    (687, 'LAKE ISABELLA'),
    (530, 'LAKEPORT'),
    (595, 'LANCASTER'),
    (617, 'LINCOLN PARK'),
    (622, 'LODI'),
    (589, 'LOMPOC'),
    (507, 'LONG BEACH'),
    (502, 'LOS ANGELES'),
    (650, 'LOS BANOS'),
    (640, 'LOS GATOS'),
    (533, 'MADERA'),
    (658, 'MANTECA'),
    (566, 'MARIPOSA'),
    (536, 'MERCED'),
    (557, 'MODESTO'),
    (511, 'MONTEBELLO'),
    (639, 'MOUNT SHASTA'),
    (540, 'NAPA'),
    (584, 'NEEDLES'),
    (662, 'NEWHALL'),
    (586, 'NORCO'),
    (686, 'NOVATO'),
    (504, 'OAKLAND CLAREMONT'),
    (604, 'OAKLAND COLISEUM'),
    (596, 'OCEANSIDE'),
    (522, 'OROVILLE'),
    (636, 'OXNARD'),
    (683, 'PALM DESERT'),
    (659, 'PALM SPRINGS'),
    (690, 'PALMDALE'),
    (601, 'PARADISE'),
    (509, 'PASADENA'),
    (574, 'PASO ROBLES'),
    (634, 'PETALUMA'),
    (592, 'PITTSBURG'),
    (525, 'PLACERVILLE'),
    (631, 'PLEASANTON'),
    (532, 'POMONA'),
    (573, 'PORTERVILLE'),
    (676, 'POWAY'),
    (544, 'QUINCY'),
    (612, 'RANCHO CUCAMONGA'),
    (558, 'RED BLUFF'),
    (551, 'REDDING'),
    (626, 'REDLANDS'),
    (548, 'REDWOOD CITY'),
    (633, 'REEDLEY'),
    (577, 'RIDGECREST'),
    (545, 'RIVERSIDE'),
    (656, 'RIVERSIDE EAST'),
    (673, 'ROCKLIN'),
    (543, 'ROSEVILLE'),
    (501, 'SACRAMENTO'),
    (602, 'SACRAMENTO SOUTH'),
    (539, 'SALINAS'),
    (568, 'SAN ANDREAS'),
    (512, 'SAN BERNARDINO'),
    (648, 'SAN CLEMENTE'),
    (506, 'SAN DIEGO'),
    (519, 'SAN DIEGO CLAIREMONT'),
    (503, 'SAN FRANCISCO'),
    (516, 'SAN JOSE'),
    (547, 'SAN LUIS OBISPO'),
    (620, 'SAN MARCOS'),
    (593, 'SAN MATEO'),
    (619, 'SAN PEDRO'),
    (677, 'SAN YSIDRO'),
    (542, 'SANTA ANA'),
    (549, 'SANTA BARBARA'),
    (632, 'SANTA CLARA'),
    (563, 'SANTA MARIA'),
    (616, 'SANTA MONICA'),
    (630, 'SANTA PAULA'),
    (555, 'SANTA ROSA'),
    (668, 'SANTA TERESA'),
    (567, 'SEASIDE'),
    (660, 'SHAFTER'),
    (680, 'SIMI VALLEY'),
    (569, 'SONORA'),
    (538, 'SOUTH LAKE TAHOE'),
    (517, 'STOCKTON'),
    (531, 'SUSANVILLE'),
    (575, 'TAFT'),
    (672, 'TEMECULA'),
    (663, 'THOUSAND OAKS'),
    (608, 'TORRANCE'),
    (642, 'TRACY'),
    (513, 'TRUCKEE'),
    (594, 'TULARE'),
    (553, 'TULELAKE'),
    (649, 'TURLOCK'),
    (638, 'TWENTYNINE PALMS'),
    (535, 'UKIAH'),
    (588, 'VACAVILLE'),
    (554, 'VALLEJO'),
    (515, 'VAN NUYS'),
    (560, 'VENTURA'),
    (629, 'VICTORVILLE'),
    (559, 'VISALIA'),
    (624, 'WALNUT CREEK'),
    (583, 'WATSONVILLE'),
    (572, 'WEAVERVILLE'),
    (618, 'WEST COVINA'),
    (611, 'WESTMINSTER'),
    (591, 'WHITTIER'),
    (571, 'WILLOWS'),
    (637, 'WINNETKA'),
    (561, 'WOODLAND'),
    (552, 'YREKA'),
    (562, 'YUBA CITY')]



if __name__ == '__main__':
    for oId,oName in getAllId():
        print oName,getAppDate(oId)
