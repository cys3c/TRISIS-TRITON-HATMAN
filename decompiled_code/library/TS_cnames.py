# uncompyle6 version 2.14.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
# [GCC 5.4.0 20160609]
# Embedded file name: TS_cnames.pyc
# Compiled at: 2017-08-03 12:26:36
TS_cst = {1: 'CONNECT REQUEST',
   2: 'CONNECT REPLY',
   3: 'DISCONN REPLY',
   4: 'DISCONN REQUEST',
   5: 'COMMAND REPLY',
   6: 'PING',
   7: 'CONN LIMIT REACHED',
   8: 'NOT CONNECTED',
   9: 'MPS ARE DEAD',
   10: 'ACCESS DENIED',
   11: 'CONNECTION FAILED'
   }
TS_keystate = {0: 'STOP',
   1: 'PROG',
   2: 'RUN',
   3: 'REMOTE',
   4: 'INVALID'
   }
TS_progstate = {0: 'RUNNING',
   1: 'HALTED',
   2: 'PAUSED',
   3: 'EXCEPTION'
   }
TS_names = {-1: 'Not set',
   0: 'Start download all',
   1: 'Start download change',
   2: 'Update configuration',
   3: 'Upload configuration',
   4: 'Set I/O addresses',
   5: 'Allocate network',
   6: 'Load vector table',
   7: 'Set calendar',
   8: 'Get calendar',
   9: 'Set scan time',
   10: 'End download all',
   11: 'End download change',
   12: 'Cancel download change',
   13: 'Attach TRICON',
   14: 'Set I/O address limits',
   15: 'Configure module',
   16: 'Set multiple point values',
   17: 'Enable all points',
   18: 'Upload vector table',
   19: 'Get CP status ',
   20: 'Run program',
   21: 'Halt program',
   22: 'Pause program',
   23: 'Do single scan',
   24: 'Get chassis status',
   25: 'Get minimum scan time',
   26: 'Set node number',
   27: 'Set I/O point values',
   28: 'Get I/O point values',
   29: 'Get MP status',
   30: 'Set retentive values',
   31: 'Adjust clock calendar',
   32: 'Clear module alarms',
   33: 'Get event log',
   34: 'Set SOE block',
   35: 'Record event log',
   36: 'Get SOE data',
   37: 'Enable OVD',
   38: 'Disable OVD',
   39: 'Enable all OVDs',
   40: 'Disable all OVDs',
   41: 'Process MODBUS',
   42: 'Upload network',
   43: 'Set lable',
   44: 'Configure system variables',
   45: 'Deconfigure module',
   46: 'Get system variables',
   47: 'Get module types',
   48: 'Begin conversion table download',
   49: 'Continue conversion table download',
   50: 'End conversion table download',
   51: 'Get conversion table',
   52: 'Set ICM status',
   53: 'Broadcast SOE data available',
   54: 'Get module versions',
   55: 'Allocate program',
   56: 'Allocate function',
   57: 'Clear retentives',
   58: 'Set initial values',
   59: 'Start TS2 program download',
   60: 'Set TS2 data area',
   61: 'Get TS2 data',
   62: 'Set TS2 data',
   63: 'Set program information',
   64: 'Get program information',
   65: 'Upload program',
   66: 'Upload function',
   67: 'Get point groups',
   68: 'Allocate symbol table',
   69: 'Get I/O address',
   70: 'Resend I/O address',
   71: 'Get program timing',
   72: 'Allocate multiple functions',
   73: 'Get node number',
   74: 'Get symbol table',
   75: 'Unk75',
   76: 'Unk76',
   77: 'Unk77',
   78: 'Unk78',
   79: 'Unk79',
   80: 'Go to DOWNLOAD mode',
   81: 'Unk81',
   83: 'Unk83',
   100: 'Command rejected',
   101: 'Download all permitted',
   102: 'Download change permitted',
   103: 'Modification accepted',
   104: 'Download cancelled',
   105: 'Program accepted',
   106: 'TRICON attached',
   107: 'I/O addresses set',
   108: 'Get CP status response',
   109: 'Program is running',
   110: 'Program is halted',
   111: 'Program is paused',
   112: 'End of single scan',
   113: 'Get chassis configuration response',
   114: 'Scan period modified',
   115: '<115>',
   116: '<116>',
   117: 'Module configured',
   118: '<118>',
   119: 'Get chassis status response',
   120: 'Vectors response',
   121: 'Get I/O point values response',
   122: 'Calendar changed',
   123: 'Configuration updated',
   124: 'Get minimum scan time response',
   125: '<125>',
   126: 'Node number set',
   127: 'Get MP status response',
   128: 'Retentive values set',
   129: 'SOE block set',
   130: 'Module alarms cleared',
   131: 'Get event log response',
   132: 'Symbol table ccepted',
   133: 'OVD enable accepted',
   134: 'OVD disable accepted',
   135: 'Record event log response',
   136: 'Upload network response',
   137: 'Get SOE data response',
   138: 'Alocate network accepted',
   139: 'Load vector table accepted',
   140: 'Get calendar response',
   141: 'Label set',
   142: 'Get module types response',
   143: 'System variables configured',
   144: 'Module deconfigured',
   145: '<145>',
   146: '<146>',
   147: 'Get conversion table response',
   148: 'ICM print data sent',
   149: 'Set ICM status response',
   150: 'Get system variables response',
   151: 'Get module versions response',
   152: 'Process MODBUS response',
   153: 'Allocate program response',
   154: 'Allocate function response',
   155: 'Clear retentives response',
   156: 'Set initial values response',
   157: 'Set TS2 data area response',
   158: 'Get TS2 data response',
   159: 'Set TS2 data response',
   160: 'Set program information reponse',
   161: 'Get program information response',
   162: 'Upload program response',
   163: 'Upload function response',
   164: 'Get point groups response',
   165: 'Allocate symbol table response',
   166: 'Program timing response',
   167: 'Disable points full',
   168: 'Allocate multiple functions response',
   169: 'Get node number response',
   170: 'Symbol table response',
   200: 'Wrong command',
   201: 'Load is in progress',
   202: 'Bad clock calendar data',
   203: 'Control program not halted',
   204: 'Control program checksum error',
   205: 'No memory available',
   206: 'Control program not valid',
   207: 'Not loading a control program',
   208: 'Network is out of range',
   209: 'Not enough arguments',
   210: 'A Network is missing',
   211: 'The download time mismatches',
   212: 'Key setting prohibits this operation',
   213: 'Bad control program version',
   214: 'Command not in correct sequence',
   215: '<215>',
   216: 'Bad Index for a module',
   217: 'Module address is invalid',
   218: '<218>',
   219: '<219>',
   220: 'Bad offset for an I/O point',
   221: 'Invalid point type',
   222: 'Invalid Point Location',
   223: 'Program name is invalid',
   224: '<224>',
   225: '<225>',
   226: '<226>',
   227: 'Invalid module type',
   228: '<228>',
   229: 'Invalid table type',
   230: '<230>',
   231: 'Invalid network continuation',
   232: 'Invalid scan time',
   233: 'Load is busy',
   234: 'An MP has re-educated',
   235: 'Invalid chassis or slot',
   236: 'Invalid SOE number',
   237: 'Invalid SOE type',
   238: 'Invalid SOE state',
   239: 'The variable is write protected',
   240: 'Node number mismatch',
   241: 'Command not allowed',
   242: 'Invalid sequence number',
   243: 'Time change on non-master TRICON',
   244: 'No free Tristation ports',
   245: 'Invalid Tristation I command',
   246: 'Invalid TriStation 1131 command',
   247: 'Only one chassis allowed',
   248: 'Bad variable address',
   249: 'Response overflow',
   250: 'Invalid bus',
   251: 'Disable is not allowed',
   252: 'Invalid length',
   253: 'Point cannot be disabled',
   254: 'Too many retentive variables',
   255: 'LOADER_CONNECT',
   256: 'Unknown reject code'
   }