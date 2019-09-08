# -*- coding: utf-8 -*-
from linepy import *
#from thrift import*
from datetime import datetime
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse

cl = LINE("EI0vepzMtTXUzgOUg6B3.ICFw716fwC8cLRP7V+9ZuW.sa+kvtKgPRXELHScaVVZP8kezAuIVx/h2xrJWIvgP+Y=") 
k1 = LINE("EILgUf75drv5anejKcoa.M71AyYS6/I0Aj3NDq8ir2G.zA2Dqav7XM4v+BIA+2qRWHOukaJcpk3Gq/F5NyuX3mM=") 
k2 = LINE("EIC2S8ExX5XS8ygtlGp7.E6Y/22GggsX+wHBE9F3G9W.JQfW/JtPDmXILYPG+IbkCNImjGrAsfcO4JhqmYz7a5c=") 
k3 = LINE("EIiGpclyx6NSFgrKp4z5.sIV5wNSTPApyzk6p+k/VHq.jT3AVoOBHAg1l42/Qfd+LPUNBj6Ui0AnSLBeWunIxDw=") 
k4 = LINE("EIXpphY8oSLKfup1kImb.hxsH1f4WQNRw9EKcTunMEW.p2VwtktCXsHpICpFkpjCQTD0z8VgtCBkKd0A9ltAMfM=")
k5 = LINE("EI3rjXW7eAk8zvmuMP13.dUCL7n2ENsaSArzDytYEWW.R4siQARIF9aecdKO9T9Q4BoL3Ko2oLIgLAeU6TRxc4Q=")
k6 = LINE("EItB7pJ8f3CEt3PSGsRa.8eu3DpwCJR+DkJCmaKxkEG.u79lE7kGblT91kpm/ItccGlka3rIHrE9VIQSTLIeO8k=")
k7 = LINE("EIeK0iXEknVCnNCodm87.zrXwMqOEx1poldJd81d7rW.Qx7CbColCYfJGfgXRnDn2JWsxRobp3WcJzOOzHfQ4Hg=")
k8 = LINE("EIv2BgridhGGNRGZkJDc.JmCb723AU5EsCI6jSee9da.eyVHhDnoXBV9BzvzZjBtGZyALWGpicvPBLpb3094uQY=")

clMID = cl.profile.mid
k1MID = k1.profile.mid	
k2MID = k2.profile.mid	
k3MID = k3.profile.mid	
k4MID = k4.profile.mid	
k5MID = k5.profile.mid	
k6MID = k6.profile.mid
k7MID = k7.profile.mid
k8MID = k8.profile.mid
	


Bots = [clMID,k1MID,k2MID,k3MID,k4MID,k5MID,k6MID,k7MID,k8MID]

oepoll = OEPoll(cl)

banOpen = codecs.open("ban.json","r","utf-8")
groupOpen = codecs.open("group.json","r","utf-8")
ban = json.load(banOpen)
gp = json.load(groupOpen)
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def botJoin(to):
    G = cl.getGroup(to)
    G.preventedJoinByTicket = False
    cl.updateGroup(G)
    Ticket = cl.reissueGroupTicket(op.param1)
    k1.acceptGroupInvitationByTicket(to,Ticket)
    k2.acceptGroupInvitationByTicket(to,Ticket)
    k3.acceptGroupInvitationByTicket(to,Ticket)
    k4.acceptGroupInvitationByTicket(to,Ticket)
    k5.acceptGroupInvitationByTicket(to,Ticket)
    k6.acceptGroupInvitationByTicket(to,Ticket)
    k7.acceptGroupInvitationByTicket(to,Ticket)
    k8.acceptGroupInvitationByTicket(to,Ticket)


    G.preventedJoinByTicket = True
    cl.updateGroup(G)
def backupData():
    try:
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = gp
        f = codecs.open('group.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def helpmessage():
    helpMessage = """╔═════════
╠   😆 風兒 防翻 (自用) 😆
╠══✪〘 Help 〙✪═══
╠➥ Gc-查詢自己剩餘票數
╠➥ Speed-速度
╠➥ Join-分身入防
╠➥ @bye-解除防護
╠➥ Gadd @-新增群管
╠➥ Gdel @-刪除群管
╠➥ GM-查看本群管理者
╠➥ Banlist-黑單
╠➥ Adminlist-權限者清單
╚〘Created By ©風兒™ 〙"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╔═══════
╠   😆 風兒 防翻 (自用) 😆
╠══✪〘 Help 〙✪═══
╠➥ Gadd @-新增群管
╠➥ Gdel @-刪除群管
╠➥ GM-查看本群管理者
╠➥ Rebot-重新啟動
╠➥ Tk @-多標踢人
╠➥ Gc mid-MID查票
╠➥ Add @-新增權限
╠➥ Del @-刪除權限
╠➥ A mid (times)-加票
╠➥ Ban:mid-MID黑單
╠➥ Ban-友資黑單
╠➥ Ban @-標注黑單
╠➥ Unban:mid-MID黑單
╠➥ Unban-友資黑單
╠➥ Unban @-標注黑單
╠➥ Gc-查詢自己剩餘票數
╠➥ Speed-速度
╠➥ Join-分身入防
╠➥ @bye-解除防護
╠➥ Banlist-黑單
╠➥ Adminlist-權限者清單
╠➥ Clear ban-清除黑單
╠➥ Kg-全群掃黑
╠➥ Kill ban-當前群組掃黑
╚〘Created By ©風兒™ 〙"""
    return helpMessageTag
def helpn():
    helpN = """╔═══════
╠   😆 風兒 防翻 (自用) 😆
╠══✪〘 Help 〙✪═══
╠➥ Gc-查詢自己剩餘票數
╠➥ Speed-速度
╠➥ GM-查看本群管理者
╚              〘完〙"""
    return helpN

wait = {
    "ban" : False,
    "unban" : False,
    "add" : False,
    "del" : False
}

if clMID not in ban["owners"]:
    ban["owners"].append(clMID)
if k1MID not in ban["owners"]:		
    ban["owners"].append(k1MID)		
if k2MID not in ban["owners"]:		
    ban["owners"].append(k2MID)		
if k3MID not in ban["owners"]:		
    ban["owners"].append(k3MID)		
if k4MID not in ban["owners"]:		
    ban["owners"].append(k4MID)		
if k5MID not in ban["owners"]:		
    ban["owners"].append(k5MID)		
if k6MID not in ban["owners"]:		
    ban["owners"].append(k6MID)		
if k7MID not in ban["owners"]:		
    ban["owners"].append(k7MID)		
if k8MID not in ban["owners"]:		
    ban["owners"].append(k8MID)


def lineBot(op):
    try:
        if op.type == 11:
            if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                pass
            else:
                gs = cl.getGroup(op.param1)
                if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                   pass
                
                   
                else:
                    bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                    gs.preventJoinByTicket = True
                    bot.updateGroup(gs)
                    bot.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            #cl.findAndAddContactsByMid(op.param1) 自動加好友
            cl.sendMessage(op.param1, "你好 {} 感謝你加我為好友😆".format(str(cl.getContact(op.param1).displayName)))
            cl.sendMessage(op.param1, None, contentMetadata={'mid': 'u39b4afd3e38e0172f278b4b06f329dd3'}, contentType=13)
             
        if op.type ==19:
            a = 0
            if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                if op.param3 in clMID or op.param3 in k1MID or op.param3 in k2MID or op.param3 in k3MID or op.param3 in k4MID or op.param3 in k5MID or op.param3 in k6MID or op.param3 in k7MID or op.param3 in k8MID:
                    while (a<3):
                        try:
                            bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)


                        except:
                            a+=1
                            pass
                        else:
                            break
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
            elif op.param3 in clMID or op.param3 in k1MID or op.param3 in k2MID or op.param3 in k3MID or op.param3 in k4MID or op.param3 in k5MID or op.param3 in k6MID or op.param3 in k7MID or op.param3 in k8MID: 
                while (a<3):
                    try:
                        bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                        bot.kickoutFromGroup(op.param1,[op.param2])
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bot.updateGroup(G)
                        Ticket = bot.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)

                    except:
                        a+=1
                        pass
                    else:
                        break
                try:
                    ban["blacklist"][op.param2] = True
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
                except:
                    pass
            else:
                bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                G=cl.getGroup(op.param1)
                if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                    pass
                else:
                    bot.kickoutFromGroup(op.param1,[op.param2])
                    ban["blacklist"][op.param2] = True
        if op.type == 0:
            return
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                if op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    botJoin(op.param1)
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                        bot.kickoutFromGroup(op.param1,[jj])
                elif op.param2 in ban["user"]:
                    ban["user"][op.param2] =ban["user"][op.param2] -1
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"你還擁有{}張票".format(str(ban["user"][op.param2])))
                    botJoin(op.param1)
                    if ban["user"][op.param2] == 0:
                        del ban["user"][op.param2]
                    G = cl.getGroup(op.param1)
                    gp["s"][G.id] =[]
                    gp["s"][G.id].append(op.param2)
                    backupData()
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                        bot.kickoutFromGroup(op.param1,[jj])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"你的票不夠啦！")
                    cl.leaveGroup(op.param1)
            if k1MID in op.param3:
            	k1.rejectGroupInvitation(op.param1)
            if k2MID in op.param3:	
            	k2.rejectGroupInvitation(op.param1)
            if k3MID in op.param3:	
            	k3.rejectGroupInvitation(op.param1)
            if k4MID in op.param3:	
            	k4.rejectGroupInvitation(op.param1)
            if k5MID in op.param3:	
            	k5.rejectGroupInvitation(op.param1)
            if k6MID in op.param3:	
            	k6.rejectGroupInvitation(op.param1)
            if k7MID in op.param3:	
            	k.rejectGroupInvitation(op.param1)
            if k8MID in op.param3:	
            	k.rejectGroupInvitation(op.param1)

            elif op.param2 in ban["admin"] or op.param2 in Bots or op.param2 in ban["owners"]:
                pass
            else:
                bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                G=bot.getGroup(op.param1)
                matched_list = []
                for tag in ban["blacklist"]:
                    if tag in op.param3:
                        matched_list.append(str(tag))
                if matched_list == []:
                    return
                for mid in matched_list:
                    bot.cancelGroupInvitation(op.param1,[mid])
        if op.type == 17:
            if op.param2 in ban["blacklist"]:
                bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                bot.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if clMID in op.param3:
                cl.leaveRoom(op.param1)
            if k1MID in op.param3:
                k1.leaveRoom(op.param1)
            if k1MID in op.param3:
                k1.leaveRoom(op.param1)
            if k2MID in op.param3:
                k2.leaveRoom(op.param1)
            if k3MID in op.param3:
                k3.leaveRoom(op.param1)
            if k4MID in op.param3:
                k4.leaveRoom(op.param1)
            if k5MID in op.param3:
                k5.leaveRoom(op.param1)
            if k6MID in op.param3:
                k6.leaveRoom(op.param1)
            if k7MID in op.param3:
                k7.leaveRoom(op.param1)
            if k8MID in op.param3:
                k8.leaveRoom(op.param1)


        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in sender:
                if text.lower() == 'gc':
                    if sender in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][sender])))
                    else:
                        cl.sendMessage(to,"你沒有票，歡迎私聊作者購買票券")
                elif text.lower() =='test':
                    cl.sendMessage(to,"running...")
                    k1.sendMessage(to,"1")
                    k2.sendMessage(to,"2")
                    k3.sendMessage(to,"3")
                    k4.sendMessage(to,"4")
                    k5.sendMessage(to,"5")
                    k6.sendMessage(to,"6")
                    k7.sendMessage(to,"7")
                    k8.sendMessage(to,"8")
                    cl.sendMessage(to,"共9個")
                    cl.sendMessage(to,"完...")
                elif text.lower() == 'runtime':
                    cl.sendMessage(to, "系統已運作 {}".format(str(format_timespan(time.time() - botStart))))

                elif text.lower() == 'sp':
                    start = time.time()
                    k1.sendMessage(to, "計算中...")
                    elapsed_time = time.time() - start
                    k1.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'gm':
                    G = cl.getGroup(to)
                    if G.id not in gp["s"] or gp["s"][G.id]==[]:
                        cl.sendMessage(7,"無群管!")
                    else:
                        mc = "╔══[ Group Manager ]"
                        for mi_d in gp["s"][G.id]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'help':
                    if sender in ban["admin"]:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                    elif sender in ban["owners"]:
                        helpMessageTag = helpmessagetag()
                        cl.sendMessage(to, str(helpMessageTag))
                    else:
                        helpN = helpn()
                        cl.sendMessage(to, str(helpN))
            if sender in ban["admin"] or sender in ban["owners"]:
                if text.lower() =='@bye':
                    cl.leaveGroup(msg.to)
                    k1.leaveGroup(msg.to)
                    k2.leaveGroup(msg.to)
                    k3.leaveGroup(msg.to)
                    k4.leaveGroup(msg.to)
                    k5.leaveGroup(msg.to)
                    k6.leaveGroup(msg.to)
                    k7.leaveGroup(msg.to)
                    k8.leaveGroup(msg.to)


                elif text.lower() == 'join':
                    botJoin(msg.to)
                elif text.lower() == 'adminlist':
                    if ban["admin"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ Admin List ]"
                        for mi_d in ban["admin"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "[ Black List ]"
                        for mi_d in ban["blacklist"]:
                            if ban["blacklist"][mi_d] == True:
                                mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)
                            else:
                            	mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)+"[baned]"
                        cl.sendMessage(msg.to,mc + "\n[ Finish ]")
            if sender in ban["owners"]:
                if text.lower().startswith("gadd "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        gp["s"][G.id] =[]
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to,"OK")
                if text.lower().startswith("gdel "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        cl.sendMessage(to, "There is no group manager！")
                    else:
                        for x in key["MENTIONEES"]:
                            try:
                                gp["s"][G.id].remove(x["M"])
                            except:
                                cl.sendMessage(to,"Not in GM.")
                        cl.sendMessage(to,"OK")
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower().startswith("gc "):
                    x = text.split(" ")
                    if x[1] in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][x[1]])))
                    else:
                        cl.sendMessage(to,"你沒有票，歡迎私聊作者購買票券")
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中...")
                    cl.sendMessage(to, "重啟成功")
                    restartBot()
                elif text.lower() == 'clear ban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower().startswith("tk "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"]:
                            pass
                        else:
                            try:
                                kicker=random.choice([k1,k2,k3,k4,k5,k6,k7,k8])
                                kicker.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif text.lower() == 'kg':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        group=cl.getGroup(i)
                        gMembMids = [contact.mid for contact in group.members] 
                        ban_list = [] 
                        for tag in ban["blacklist"]: 
                            ban_list += filter(lambda str: str == tag, gMembMids) 
                        if ban_list == []: 
                            cl.sendMessage(i, "沒有黑名單") 
                        else: 
                            for jj in ban_list: 
                                bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8]) 
                                bot.kickoutFromGroup(i, [jj]) 
                            cl.sendMessage(i, "掃黑結束") 
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in ban["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            bot = random.choice([cl,k1,k2,k3,k4,k5,k6,k7,k8])
                            for jj in matched_list:
                                bot.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單以踢除")
                elif text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"]:
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        cl.sendMessage(to,"already")
                elif text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                elif text.lower() == 'add':
                    wait["add"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'del':
                    wait["del"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower().startswith("a "):
                    x = text.split(" ")
                    ban["admin"].append(x[1])
                    if len(x) ==2:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = 1
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=1
                            cl.sendMessage(to,"ok")
                    elif len(x) ==3:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = int(x[2])
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=int(x[2])
                            cl.sendMessage(to,"ok")
                    backupData()
                elif text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith("ban:"):
                    txt = text.replace("Ban:","")
                    try:
                        ban["blacklist"][txt] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !" +txt)
                elif text.lower().startswith("unban:"):
                    txt = text.replace("Unban:","")
                    try:
                        del ban["blacklist"][txt]
                        cl.sendMessage(msg.to,"已刪除黑單!")
                    except:
                        cl.sendMessage(msg.to,"刪除失敗 !" +txt)
                elif text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] =False
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'ban':
                    wait["ban"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"] = True
                    cl.sendMessage(to,"Please send a Contact")
        if op.type == 25 or op.type ==26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["ban"] = False
                        else:
                           ban["blacklist"][msg.contentMetadata["mid"]] = True
                           wait["ban"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["unban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["unban"] = False
                        else:
                           del ban["blacklist"][msg.contentMetadata["mid"]]
                           wait["unban"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
                elif wait["add"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["add"] = False
                        else:
                           ban["admin"].append(str(msg.contentMetadata["mid"]))
                           wait["add"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["del"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["del"] = False
                        else:
                           ban["admin"].remove(str(msg.contentMetadata["mid"]))
                           wait["del"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
#                else:
#                    cl.sendMessage(msg.to,str(msg.contentMetadata["mid"]))
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
