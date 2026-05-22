#!/usr/bin/python2

import sys
from copy import *
from sqlalchemy import inspect
# import pdb

from .dbsession import *


class mixin(object):
    def getdict(self):
        mydict={}
        for mykey in self.__dict__.keys():
            if mykey in self.__table__.columns:
                myvalue = self.__dict__[mykey]
                if sys.version_info < (3,0):
                    if type(mykey) is unicode:
                        mykey = mykey.encode()

                    if type(myvalue) is unicode:
                        myvalue = myvalue.encode()
                mydict["%s.%s" % (self.__tablename__, mykey)]= myvalue
        try:
            self.__class__.outprocess(mydict)
        except:
            pass 
        return mydict

    #return a tuple of table primary keys
    @classmethod
    def primkeys(cls):
        ins = inspect(cls)
        prikeys=[ item.key for item in ins.primary_key ]
        prikeys.sort(reverse=False)
        return tuple(prikeys)

    #return the key of object in table row
    @classmethod
    def getobjkey(cls):
        return cls.primkeys()

    @classmethod
    def isValid(cls, netname, tabdict):
        return True

    @classmethod
    def dict2tabentry(self,objdict):
        pass      
    
    @classmethod
    def getcolumns(self):
        return self.__table__.columns.keys()

    @classmethod
    def getTabtype(self):
        return 'matrix'

    @classmethod
    def getReservedKeys(self):
        return []
########################################################################
class passwd(Base,mixin):
    """"""
    __tablename__ = 'passwd'
    __table_args__ = autoload_kwargs(DBsession.getEngine('passwd'))

    @classmethod
    def primkeys(cls):
        return ('key','username')

    @classmethod
    def getobjkey(cls):
        return tuple(['key'])
    
########################################################################
class networks(Base,mixin):
    """"""
    __tablename__ = 'networks'
    __table_args__ = autoload_kwargs(DBsession.getEngine('networks'))

    @classmethod
    def primkeys(cls):
        return tuple(['netname'])
    @classmethod
    def getobjkey(cls):
        return tuple(['netname'])

    @classmethod    
    def isValid(cls, netname, tabdict):
        eptkey=0
        if 'net' not in tabdict.keys() or not tabdict['net']:
            print("Error: net value should not be empty for xCAT network object "+netname)
            eptkey=1
        if 'mask' not in tabdict.keys() or not tabdict['mask']:
            print ("Error: mask value should not be empty for xCAT network object "+netname)
            eptkey=1
        if eptkey:
            return False
        else:
            return True

########################################################################
class routes(Base,mixin):
    """"""
    __tablename__ = 'routes'
    __table_args__ = autoload_kwargs(DBsession.getEngine('routes'))


########################################################################
class nodetype(Base,mixin):
    """"""
    __tablename__ = 'nodetype'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nodetype'))

########################################################################
'''
class hosts(Base,mixin):
    """"""
    __tablename__ = 'hosts'
    __table_args__ = autoload_kwargs(DBsession.getEngine('hosts'))
'''
########################################################################
class noderes(Base,mixin):
    """"""
    __tablename__ = 'noderes'
    __table_args__ = autoload_kwargs(DBsession.getEngine('noderes'))

########################################################################
class switch(Base,mixin):
    """"""
    __tablename__ = 'switch'
    __table_args__ = autoload_kwargs(DBsession.getEngine('switch'))

    @classmethod
    def getobjkey(cls):
        return tuple(['node'])
########################################################################
class switches(Base,mixin):
    """"""
    __tablename__ = 'switches'
    __table_args__ = autoload_kwargs(DBsession.getEngine('switches'))


########################################################################
class mac(Base,mixin):
    """"""
    __tablename__ = 'mac'
    __table_args__ = autoload_kwargs(DBsession.getEngine('mac'))
########################################################################
class hwinv(Base,mixin):
    """"""
    __tablename__ = 'hwinv'
    __table_args__ = autoload_kwargs(DBsession.getEngine('hwinv'))
########################################################################
class postscripts(Base,mixin):
    """"""
    __tablename__ = 'postscripts'
    __table_args__ = autoload_kwargs(DBsession.getEngine('postscripts'))

    @classmethod
    def getReservedKeys(self):
        return ('xcatdefaults','service')
    
########################################################################
class bootparams(Base,mixin):
    """"""
    __tablename__ = 'bootparams'
    __table_args__ = autoload_kwargs(DBsession.getEngine('bootparams'))

########################################################################
class nodelist(Base,mixin):
    """"""
    __tablename__ = 'nodelist'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nodelist'))

########################################################################
class vm(Base,mixin):
    """"""
    __tablename__ = 'vm'
    __table_args__ = autoload_kwargs(DBsession.getEngine('vm'))
########################################################################
class policy(Base,mixin):
    """"""
    __tablename__ = 'policy'
    __table_args__ = autoload_kwargs(DBsession.getEngine('policy'))

########################################################################
class nodehm(Base,mixin):
    """"""
    __tablename__ = 'nodehm'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nodehm'))
########################################################################
class nodegroup(Base,mixin):
    """"""
    __tablename__ = 'nodegroup'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nodegroup'))
########################################################################
class vpd(Base,mixin):
    """"""
    __tablename__ = 'vpd'
    __table_args__ = autoload_kwargs(DBsession.getEngine('vpd'))
########################################################################
class servicenode(Base,mixin):
    """"""
    __tablename__ = 'servicenode'
    __table_args__ = autoload_kwargs(DBsession.getEngine('servicenode'))
########################################################################
class hosts(Base,mixin):
    """"""
    __tablename__ = 'hosts'
    __table_args__ = autoload_kwargs(DBsession.getEngine('hosts'))
########################################################################
class nics(Base,mixin):
    """"""
    __tablename__ = 'nics'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nics'))
########################################################################
class openbmc(Base,mixin):
    """"""
    __tablename__ = 'openbmc'
    __table_args__ = autoload_kwargs(DBsession.getEngine('openbmc'))
########################################################################
class prodkey(Base,mixin):
    """"""
    __tablename__ = 'prodkey'
    __table_args__ = autoload_kwargs(DBsession.getEngine('prodkey'))

    @classmethod
    def getobjkey(cls):
        return tuple(['node'])
########################################################################
class domain(Base,mixin):
    """"""
    __tablename__ = 'domain'
    __table_args__ = autoload_kwargs(DBsession.getEngine('domain'))
########################################################################
class chain(Base,mixin):
    """"""
    __tablename__ = 'chain'
    __table_args__ = autoload_kwargs(DBsession.getEngine('chain'))
########################################################################
class rack(Base,mixin):
    """"""
    __tablename__ = 'rack'
    __table_args__ = autoload_kwargs(DBsession.getEngine('rack'))
########################################################################
class nodepos(Base,mixin):
    """"""
    __tablename__ = 'nodepos'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nodepos'))
########################################################################
class ppc(Base,mixin):
    """"""
    __tablename__ = 'ppc'
    __table_args__ = autoload_kwargs(DBsession.getEngine('ppc'))
########################################################################
class ppchcp(Base,mixin):
    """"""
    __tablename__ = 'ppchcp'
    __table_args__ = autoload_kwargs(DBsession.getEngine('ppchcp'))
########################################################################
class mp(Base,mixin):
    """"""
    __tablename__ = 'mp'
    __table_args__ = autoload_kwargs(DBsession.getEngine('mp'))
########################################################################
class zvm(Base,mixin):
    """"""
    __tablename__ = 'zvm'
    __table_args__ = autoload_kwargs(DBsession.getEngine('zvm'))
########################################################################
class mpa(Base,mixin):
    """"""
    __tablename__ = 'mpa'
    __table_args__ = autoload_kwargs(DBsession.getEngine('mpa'))
########################################################################
class pdu(Base,mixin):
    """"""
    __tablename__ = 'pdu'
    __table_args__ = autoload_kwargs(DBsession.getEngine('pdu'))
########################################################################
class pduoutlet(Base,mixin):
    """"""
    __tablename__ = 'pduoutlet'
    __table_args__ = autoload_kwargs(DBsession.getEngine('pduoutlet'))
########################################################################
class cfgmgt(Base,mixin):
    """"""
    __tablename__ = 'cfgmgt'
    __table_args__ = autoload_kwargs(DBsession.getEngine('cfgmgt'))
########################################################################
class hypervisor(Base,mixin):
    """"""
    __tablename__ = 'hypervisor'
    __table_args__ = autoload_kwargs(DBsession.getEngine('hypervisor'))
########################################################################
class iscsi(Base,mixin):
    """"""
    __tablename__ = 'iscsi'
    __table_args__ = autoload_kwargs(DBsession.getEngine('iscsi'))
########################################################################
class mic(Base,mixin):
    """"""
    __tablename__ = 'mic'
    __table_args__ = autoload_kwargs(DBsession.getEngine('mic'))
########################################################################
class ppcdirect(Base,mixin):
    """"""
    __tablename__ = 'ppcdirect'
    __table_args__ = autoload_kwargs(DBsession.getEngine('ppcdirect'))

    @classmethod
    def primkeys(cls):
        return tuple(['hcp'])
########################################################################
class storage(Base,mixin):
    """"""
    __tablename__ = 'storage'
    __table_args__ = autoload_kwargs(DBsession.getEngine('storage'))
########################################################################
class websrv(Base,mixin):
    """"""
    __tablename__ = 'websrv'
    __table_args__ = autoload_kwargs(DBsession.getEngine('websrv'))
########################################################################
class prescripts(Base,mixin):
    """"""
    __tablename__ = 'prescripts'
    __table_args__ = autoload_kwargs(DBsession.getEngine('prescripts'))
########################################################################
class ipmi(Base,mixin):
    """"""
    __tablename__ = 'ipmi'
    __table_args__ = autoload_kwargs(DBsession.getEngine('ipmi'))
########################################################################
class osimage(Base,mixin):
    """"""
    __tablename__ = 'osimage'
    __table_args__ = autoload_kwargs(DBsession.getEngine('osimage'))
########################################################################
class linuximage(Base,mixin):
    """"""
    __tablename__ = 'linuximage'
    __table_args__ = autoload_kwargs(DBsession.getEngine('linuximage'))
########################################################################
class winimage(Base,mixin):
    """"""
    __tablename__ = 'winimage'
    __table_args__ = autoload_kwargs(DBsession.getEngine('winimage'))
########################################################################
class nimimage(Base,mixin):
    """"""
    __tablename__ = 'nimimage'
    __table_args__ = autoload_kwargs(DBsession.getEngine('nimimage'))
########################################################################
class zone(Base,mixin):
    """"""
    __tablename__ = 'zone'
    __table_args__ = autoload_kwargs(DBsession.getEngine('zone'))
########################################################################
class osdistro(Base,mixin):
    """"""
    __tablename__ = 'osdistro'
    __table_args__ = autoload_kwargs(DBsession.getEngine('osdistro'))
########################################################################
class site(Base,mixin):
    """"""
    __tablename__ = 'site'
    __table_args__ = autoload_kwargs(DBsession.getEngine('site'))
########################################################################
    def getdict(self):
        mydict={}
        mykey=self.__dict__['key']
        mydict[self.__tablename__+'.'+mykey]=mykey=self.__dict__['value']
        return mydict

    @classmethod
    def dict2tabentry(self,objdict):
        mydict={}
        ret=[]
        for key in objdict.keys():
            mydict['key']=key
            mydict['value']=objdict[key]
            mydict['disable']=None
            ret.append(deepcopy(mydict))
        return ret
       
    @classmethod
    def getTabtype(self):
        return 'flat'
#----------------------------------------------------------------------

def query_table_by_node(session, tclass, tkey):
    """"""
    result=session.query(tclass).filter(tclass.node == tkey).all()
    if not result:
       return None 
    return result[0].getdict()


def query_nodelist_by_key(session, nodelist):
    """"""
    nodelist_value = {}
    for node in nodelist:
        nodelist_value[node]={}
        classlist = [Bootparams,Nodetype,Hosts,Switch,Mac,Noderes]
        for eachclass in classlist:
            clsdict = query_table_by_node(session,eachclass,node)
            nodelist_value[node].update(clsdict)
    return nodelist_value

if __name__ == "__main__":
     pass
  
