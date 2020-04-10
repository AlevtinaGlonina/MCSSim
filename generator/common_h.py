#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.compat import unicode

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.1.0'
__CHEETAH_versionTuple__ = (3, 1, 0, 'final', 1)
__CHEETAH_genTime__ = 1586513964.996211
__CHEETAH_genTimestamp__ = 'Fri Apr 10 13:19:24 2020'
__CHEETAH_src__ = 'common_h.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Apr 10 11:57:32 2020'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class common_h(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(common_h, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''#ifndef __COMMON__H_
#define __COMMON__H_

#include <vector>
#include <string>
#include "network.h"
#include "channel.h"
#include "timer.h"
#include "var.h"

#define DUMMY_NUM 100000000

''')
        for n in VFFSL(SL,"declarations",True): # generated from line 13, col 1
            _v = VFFSL(SL,"n",True) # u'$n' on line 14, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$n')) # from line 14, col 1.
            write(u'''
''')
        write(u'''
''')
        for i in VFN(VFFSL(SL,"base",True),"keys",False)(): # generated from line 17, col 1
            write(u'''void create''')
            _v = VFFSL(SL,"i",True) # u'$i' on line 18, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 18, col 12.
            write(u''' (std::string type, std::string _name, Network *n, int p, bool t''')
            automaton = VFFSL(SL,"base",True)[i][0]
            for p in VFFSL(SL,"automaton.typedParams",True): # generated from line 20, col 1
                write(u''', ''')
                _v = VFFSL(SL,"p",True)[1] # u'${p[1]}' on line 21, col 3
                if _v is not None: write(_filter(_v, rawExpr=u'${p[1]}')) # from line 21, col 3.
                write(u'''* _''')
                _v = VFFSL(SL,"p",True)[0] # u'${p[0]}' on line 21, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'${p[0]}')) # from line 21, col 13.
            for p in VFFSL(SL,"automaton.arrayTypedParams",True): # generated from line 23, col 1
                write(u''', std::vector <''')
                _v = VFFSL(SL,"p",True)[1] # u'${p[1]}' on line 24, col 16
                if _v is not None: write(_filter(_v, rawExpr=u'${p[1]}')) # from line 24, col 16.
                write(u'''*> & _''')
                _v = VFFSL(SL,"p",True)[0] # u'${p[0]}' on line 24, col 29
                if _v is not None: write(_filter(_v, rawExpr=u'${p[0]}')) # from line 24, col 29.
            for p in VFFSL(SL,"automaton.vars",True): # generated from line 26, col 1
                write(u''', Var* _''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 27, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 27, col 9.
            for p in VFFSL(SL,"automaton.arrayVars",True): # generated from line 29, col 1
                write(u''', std::vector <Var*> &_''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 30, col 24
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 30, col 24.
            for p in VFFSL(SL,"automaton.arrayArrayVars",True): # generated from line 32, col 1
                write(u''', std::vector < std::vector <Var*> > &_''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 33, col 40
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 33, col 40.
            for p in VFFSL(SL,"automaton.chans",True): # generated from line 35, col 1
                write(u''', Channel* _''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 36, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 36, col 13.
            for p in VFFSL(SL,"automaton.arrayChans",True): # generated from line 38, col 1
                write(u''', std::vector <Channel*> &_''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 39, col 28
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 39, col 28.
            for p in VFFSL(SL,"automaton.timers",True): # generated from line 41, col 1
                write(u''', Timer* _''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 42, col 11
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 42, col 11.
            for p in VFFSL(SL,"automaton.arrayTimers",True): # generated from line 44, col 1
                write(u''', std::vector <Timer*> &_''')
                _v = VFFSL(SL,"p",True) # u'$p' on line 45, col 26
                if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 45, col 26.
            write(u''');
''')
        write(u'''
#endif
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_common_h = 'respond'

## END CLASS DEFINITION

if not hasattr(common_h, '_initCheetahAttributes'):
    templateAPIClass = getattr(common_h,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(common_h)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=common_h()).run()

