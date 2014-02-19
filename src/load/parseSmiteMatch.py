__author__ = 'aahammer'

import datetime
import time
from time import mktime

def getMatchData(tree):

    match_col = {}

    if tree.xpath('//span[@id="lblHeader"][1]')[0].text == None:
        return


    match_col['queue_type'], match_col['match_type'] = tree.xpath('//span[@id="lblHeader"][1]')[0].text.split(':')

    ids = ['lblMatchId','lblMatchTime','lblMatchDuration', None]
    ids_db = ['match_id', 'end_time', 'duration']

    match_statistics = tree.xpath('//div[@id="detailsTopBar"][1]')
    for mstats in match_statistics:
        id_index = 0
        for element in mstats.iter():
            if element.attrib.has_key('id'):
                if element.attrib['id']  == ids[id_index]:
                    match_col[ids_db[id_index]] = element.text
                    id_index += 1

    match_col['match_id'] = int(match_col['match_id'])
    match_col['duration'] = int(match_col['duration'])
    match_col['end_time'] = datetime.datetime.fromtimestamp(mktime(time.strptime(match_col['end_time'], "%m/%d/%Y %H:%M:%S GMT")))

    return match_col


def getPlayerData(tree):

    teamData = []

    ids = ['lblGodName','pdName','pdKills','pdDeaths','pdAssists','pdGold', 'pdDamagePlayer', 'pdDamageStructure', 'Label1', 'pdDamageBot', 'pdDamageTaken', None]
    ids_db = ['god', 'name', 'kills', 'deaths', 'assists', 'gold','damage_player', 'damage_structure', 'healing', 'damage_creep', 'damage_taken']
    data_ids_db = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'active1', 'active2']

    # Entry Path for Playerdetails
    player_statistics = tree.xpath('//div[@id="detailsContent"]/div[2]//div[@id="panDetailsTable"]/table')
    for pstats in player_statistics:
        id_index = 0
        data_id_index = 0
        player = {}
        for element in pstats.iter():

            if element.attrib.has_key('id'):
                if element.attrib['id']  == ids[id_index]:
                    if element.attrib['id'] == 'lblGodName' or element.attrib['id'] == 'pdName': player[ids_db[id_index]] = element.text
                    else: player[ids_db[id_index]] = int(element.text)
                    #print element.attrib['id']+ ' : ' + element.text
                    id_index += 1
            elif element.attrib.has_key('class') and element.attrib['class'] == 'playerDetailsTable':
                #print 'level' + ' : ' + element.xpath('tr/td')[0].text.strip()
                player['level'] = int(element.xpath('tr/td')[0].text.strip())
            elif element.attrib.has_key('data-id'):
                player[data_ids_db[data_id_index]] = int(element.attrib['data-id'])
                data_id_index += 1
        teamData.append(player)

    return teamData