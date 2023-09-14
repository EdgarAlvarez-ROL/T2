
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD CADENA CAT CONT COPY DELETE DESTINO DIR EDIT EXECUTE FDISK FILE1 FILE2 FIT FS FS_VAL GRP GUION ID IGUAL LETRAS_FIT LETRA_FDISK LETRA_MKDISK LOGIN LOGOUT MKDIR MKDISK MKFILE MKFS MKGRP MKUSR MOUNT NAME NUM PASS PATH R REMOVE RENAME REP RMDISK RMGRP RMUSR SIZE STRING TYPE UNIT UNMOUNT USERcomando : MKDISK atributosmatributosm : atributosm atributom\n                 | atributomatributom : GUION PATH DIR\n                 | GUION FIT STRING\n                 | GUION UNIT STRING\n                 | GUION SIZE STRINGcomando : FDISK atributosatributos : atributos atributo\n                 | atributoatributo : GUION PATH DIR\n                | GUION TYPE STRING\n                | GUION UNIT STRING\n                | GUION NAME STRING\n                | GUION SIZE STRING\n                | GUION FIT STRING\n                | GUION ADD STRING\n                | GUION DELETEcomando : REP GUION PATH DIRcomando : RMDISK GUION PATH DIRcomando : MOUNT atributos_mountatributos_mount : atributos_mount atributo_mm\n                 | atributo_mmatributo_mm : GUION PATH DIR\n                   | GUION NAME STRINGcomando : UNMOUNT GUION ID STRINGcomando : MKFS atributos_mkfsatributos_mkfs : atributos_mkfs atributosSolo_mkfs\n                        | atributosSolo_mkfsatributosSolo_mkfs : GUION ID STRING\n                            | GUION TYPE STRING\n                            | GUION FS STRINGcomando : LOGIN atributos_loginatributos_login : atributos_login atributosSolo_login\n                        | atributosSolo_loginatributosSolo_login :  GUION USER STRING\n                            | GUION PASS STRING\n                            | GUION ID STRINGcomando : LOGOUTcomando : MKGRP GUION NAME STRINGcomando : RMGRP GUION NAME STRINGcomando : MKUSR atributos_mkusratributos_mkusr : atributos_mkusr atributosSolo_mkusr\n                        | atributosSolo_mkusratributosSolo_mkusr :  GUION USER STRING\n                            | GUION PASS STRING\n                            | GUION GRP STRINGcomando : RMUSR GUION NAME STRINGcomando : MKFILE atributos_mkfileatributos_mkfile : atributos_mkfile atributosSolo_mkfile\n                        | atributosSolo_mkfileatributosSolo_mkfile : GUION PATH DIR\n                            | GUION SIZE STRING\n                            | GUION CONT STRING\n                            | GUION Rcomando : CAT listaFilesCATlistaFilesCAT : listaFilesCAT atributosSolo_CAT\n                        | atributosSolo_CATatributosSolo_CAT : GUION FILE2 STRING\n                         | GUION FILE1 STRINGcomando : REMOVE GUION PATH IGUAL DIRcomando : EDIT listas_editlistas_edit : listas_edit atributosSolo_EDIT\n                        | atributosSolo_EDITatributosSolo_EDIT : GUION PATH IGUAL DIR\n                         |  GUION CONT IGUAL DIRcomando : RENAME lista_renamelista_rename : lista_rename atributosSolo_RENAME\n                        | atributosSolo_RENAMEatributosSolo_RENAME : GUION PATH IGUAL DIR\n                            | GUION NAME IGUAL CADENAcomando : MKDIR lista_mkdirlista_mkdir : lista_mkdir atributosSolo_MKDIR\n                        | atributosSolo_MKDIRatributosSolo_MKDIR : GUION PATH IGUAL DIR\n                           | GUION Rcomando : COPY lista_copylista_copy : lista_copy atributosSolo_COPY\n                        | atributosSolo_COPYatributosSolo_COPY : GUION PATH IGUAL DIR\n                          | GUION DESTINO IGUAL DIRcomando : EXECUTE GUION PATH DIR'
    
_lr_action_items = {'MKDISK':([0,],[2,]),'FDISK':([0,],[3,]),'REP':([0,],[4,]),'RMDISK':([0,],[5,]),'MOUNT':([0,],[6,]),'UNMOUNT':([0,],[7,]),'MKFS':([0,],[8,]),'LOGIN':([0,],[9,]),'LOGOUT':([0,],[10,]),'MKGRP':([0,],[11,]),'RMGRP':([0,],[12,]),'MKUSR':([0,],[13,]),'RMUSR':([0,],[14,]),'MKFILE':([0,],[15,]),'CAT':([0,],[16,]),'REMOVE':([0,],[17,]),'EDIT':([0,],[18,]),'RENAME':([0,],[19,]),'MKDIR':([0,],[20,]),'COPY':([0,],[21,]),'EXECUTE':([0,],[22,]),'$end':([1,10,23,24,26,27,31,32,35,36,38,39,43,44,47,48,50,51,54,55,57,58,60,61,63,64,67,72,80,83,87,91,97,102,106,107,111,114,117,119,120,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,165,166,167,168,169,170,171,172,173,],[0,-39,-1,-3,-8,-10,-21,-23,-27,-29,-33,-35,-42,-44,-49,-51,-56,-58,-62,-64,-67,-69,-72,-74,-77,-79,-2,-9,-18,-22,-28,-34,-43,-50,-55,-57,-63,-68,-73,-76,-78,-4,-5,-6,-7,-11,-12,-13,-14,-15,-16,-17,-19,-20,-24,-25,-26,-30,-31,-32,-36,-37,-38,-40,-41,-45,-46,-47,-48,-52,-53,-54,-59,-60,-82,-61,-65,-66,-70,-71,-75,-80,-81,]),'GUION':([2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,31,32,35,36,38,39,43,44,47,48,50,51,54,55,57,58,60,61,63,64,67,72,80,83,87,91,97,102,106,107,111,114,117,119,120,124,125,126,127,128,129,130,131,132,133,134,137,138,140,141,142,143,144,145,148,149,150,152,153,154,155,156,167,168,169,170,171,172,173,],[25,28,29,30,33,34,37,40,41,42,45,46,49,52,53,56,59,62,65,66,25,-3,28,-10,33,-23,37,-29,40,-35,45,-44,49,-51,52,-58,56,-64,59,-69,62,-74,65,-79,-2,-9,-18,-22,-28,-34,-43,-50,-55,-57,-63,-68,-73,-76,-78,-4,-5,-6,-7,-11,-12,-13,-14,-15,-16,-17,-24,-25,-30,-31,-32,-36,-37,-38,-45,-46,-47,-52,-53,-54,-59,-60,-65,-66,-70,-71,-75,-80,-81,]),'PATH':([25,28,29,30,33,49,53,56,59,62,65,66,],[68,73,81,82,84,103,110,112,115,118,121,123,]),'FIT':([25,28,],[69,78,]),'UNIT':([25,28,],[70,75,]),'SIZE':([25,28,49,],[71,77,104,]),'TYPE':([28,37,],[74,89,]),'NAME':([28,33,41,42,46,59,],[76,85,95,96,101,116,]),'ADD':([28,],[79,]),'DELETE':([28,],[80,]),'ID':([34,37,40,],[86,88,94,]),'FS':([37,],[90,]),'USER':([40,45,],[92,98,]),'PASS':([40,45,],[93,99,]),'GRP':([45,],[100,]),'CONT':([49,56,],[105,113,]),'R':([49,62,],[106,119,]),'FILE2':([52,],[108,]),'FILE1':([52,],[109,]),'DESTINO':([65,],[122,]),'DIR':([68,73,81,82,84,103,123,157,158,159,160,162,163,164,],[124,128,135,136,137,152,165,166,167,168,169,171,172,173,]),'STRING':([69,70,71,74,75,76,77,78,79,85,86,88,89,90,92,93,94,95,96,98,99,100,101,104,105,108,109,],[125,126,127,129,130,131,132,133,134,138,139,140,141,142,143,144,145,146,147,148,149,150,151,153,154,155,156,]),'IGUAL':([110,112,113,115,116,118,121,122,],[157,158,159,160,161,162,163,164,]),'CADENA':([161,],[170,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comando':([0,],[1,]),'atributosm':([2,],[23,]),'atributom':([2,23,],[24,67,]),'atributos':([3,],[26,]),'atributo':([3,26,],[27,72,]),'atributos_mount':([6,],[31,]),'atributo_mm':([6,31,],[32,83,]),'atributos_mkfs':([8,],[35,]),'atributosSolo_mkfs':([8,35,],[36,87,]),'atributos_login':([9,],[38,]),'atributosSolo_login':([9,38,],[39,91,]),'atributos_mkusr':([13,],[43,]),'atributosSolo_mkusr':([13,43,],[44,97,]),'atributos_mkfile':([15,],[47,]),'atributosSolo_mkfile':([15,47,],[48,102,]),'listaFilesCAT':([16,],[50,]),'atributosSolo_CAT':([16,50,],[51,107,]),'listas_edit':([18,],[54,]),'atributosSolo_EDIT':([18,54,],[55,111,]),'lista_rename':([19,],[57,]),'atributosSolo_RENAME':([19,57,],[58,114,]),'lista_mkdir':([20,],[60,]),'atributosSolo_MKDIR':([20,60,],[61,117,]),'lista_copy':([21,],[63,]),'atributosSolo_COPY':([21,63,],[64,120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> comando","S'",1,None,None,None),
  ('comando -> MKDISK atributosm','comando',2,'p_comando_mkdisk','DOSgramatica.py',263),
  ('atributosm -> atributosm atributom','atributosm',2,'p_atributosM','DOSgramatica.py',312),
  ('atributosm -> atributom','atributosm',1,'p_atributosM','DOSgramatica.py',313),
  ('atributom -> GUION PATH DIR','atributom',3,'p_atributoM','DOSgramatica.py',321),
  ('atributom -> GUION FIT STRING','atributom',3,'p_atributoM','DOSgramatica.py',322),
  ('atributom -> GUION UNIT STRING','atributom',3,'p_atributoM','DOSgramatica.py',323),
  ('atributom -> GUION SIZE STRING','atributom',3,'p_atributoM','DOSgramatica.py',324),
  ('comando -> FDISK atributos','comando',2,'p_comando_fdisk','DOSgramatica.py',331),
  ('atributos -> atributos atributo','atributos',2,'p_atributos','DOSgramatica.py',400),
  ('atributos -> atributo','atributos',1,'p_atributos','DOSgramatica.py',401),
  ('atributo -> GUION PATH DIR','atributo',3,'p_atributo','DOSgramatica.py',409),
  ('atributo -> GUION TYPE STRING','atributo',3,'p_atributo','DOSgramatica.py',410),
  ('atributo -> GUION UNIT STRING','atributo',3,'p_atributo','DOSgramatica.py',411),
  ('atributo -> GUION NAME STRING','atributo',3,'p_atributo','DOSgramatica.py',412),
  ('atributo -> GUION SIZE STRING','atributo',3,'p_atributo','DOSgramatica.py',413),
  ('atributo -> GUION FIT STRING','atributo',3,'p_atributo','DOSgramatica.py',414),
  ('atributo -> GUION ADD STRING','atributo',3,'p_atributo','DOSgramatica.py',415),
  ('atributo -> GUION DELETE','atributo',2,'p_atributo','DOSgramatica.py',416),
  ('comando -> REP GUION PATH DIR','comando',4,'p_comando_rep','DOSgramatica.py',426),
  ('comando -> RMDISK GUION PATH DIR','comando',4,'p_comando_rmdisk','DOSgramatica.py',440),
  ('comando -> MOUNT atributos_mount','comando',2,'p_comando_mount','DOSgramatica.py',455),
  ('atributos_mount -> atributos_mount atributo_mm','atributos_mount',2,'p_atributos_mount','DOSgramatica.py',479),
  ('atributos_mount -> atributo_mm','atributos_mount',1,'p_atributos_mount','DOSgramatica.py',480),
  ('atributo_mm -> GUION PATH DIR','atributo_mm',3,'p_atributo_mount','DOSgramatica.py',488),
  ('atributo_mm -> GUION NAME STRING','atributo_mm',3,'p_atributo_mount','DOSgramatica.py',489),
  ('comando -> UNMOUNT GUION ID STRING','comando',4,'p_comando_unmount','DOSgramatica.py',495),
  ('comando -> MKFS atributos_mkfs','comando',2,'p_comando_mkfs','DOSgramatica.py',507),
  ('atributos_mkfs -> atributos_mkfs atributosSolo_mkfs','atributos_mkfs',2,'p_atributos_mkfs','DOSgramatica.py',535),
  ('atributos_mkfs -> atributosSolo_mkfs','atributos_mkfs',1,'p_atributos_mkfs','DOSgramatica.py',536),
  ('atributosSolo_mkfs -> GUION ID STRING','atributosSolo_mkfs',3,'p_atributoSolo_mkfs','DOSgramatica.py',544),
  ('atributosSolo_mkfs -> GUION TYPE STRING','atributosSolo_mkfs',3,'p_atributoSolo_mkfs','DOSgramatica.py',545),
  ('atributosSolo_mkfs -> GUION FS STRING','atributosSolo_mkfs',3,'p_atributoSolo_mkfs','DOSgramatica.py',546),
  ('comando -> LOGIN atributos_login','comando',2,'p_comando_login','DOSgramatica.py',552),
  ('atributos_login -> atributos_login atributosSolo_login','atributos_login',2,'p_atributos_login','DOSgramatica.py',589),
  ('atributos_login -> atributosSolo_login','atributos_login',1,'p_atributos_login','DOSgramatica.py',590),
  ('atributosSolo_login -> GUION USER STRING','atributosSolo_login',3,'p_atributoSolo_login','DOSgramatica.py',598),
  ('atributosSolo_login -> GUION PASS STRING','atributosSolo_login',3,'p_atributoSolo_login','DOSgramatica.py',599),
  ('atributosSolo_login -> GUION ID STRING','atributosSolo_login',3,'p_atributoSolo_login','DOSgramatica.py',600),
  ('comando -> LOGOUT','comando',1,'p_comando_logout','DOSgramatica.py',606),
  ('comando -> MKGRP GUION NAME STRING','comando',4,'p_comando_mkgrp','DOSgramatica.py',619),
  ('comando -> RMGRP GUION NAME STRING','comando',4,'p_comando_rmgrp','DOSgramatica.py',635),
  ('comando -> MKUSR atributos_mkusr','comando',2,'p_comando_mkusr','DOSgramatica.py',651),
  ('atributos_mkusr -> atributos_mkusr atributosSolo_mkusr','atributos_mkusr',2,'p_atributos_mkusr','DOSgramatica.py',680),
  ('atributos_mkusr -> atributosSolo_mkusr','atributos_mkusr',1,'p_atributos_mkusr','DOSgramatica.py',681),
  ('atributosSolo_mkusr -> GUION USER STRING','atributosSolo_mkusr',3,'p_atributoSolo_mkusr','DOSgramatica.py',689),
  ('atributosSolo_mkusr -> GUION PASS STRING','atributosSolo_mkusr',3,'p_atributoSolo_mkusr','DOSgramatica.py',690),
  ('atributosSolo_mkusr -> GUION GRP STRING','atributosSolo_mkusr',3,'p_atributoSolo_mkusr','DOSgramatica.py',691),
  ('comando -> RMUSR GUION NAME STRING','comando',4,'p_comando_rmusr','DOSgramatica.py',698),
  ('comando -> MKFILE atributos_mkfile','comando',2,'p_comando_mkfile','DOSgramatica.py',721),
  ('atributos_mkfile -> atributos_mkfile atributosSolo_mkfile','atributos_mkfile',2,'p_atributos_mkfile','DOSgramatica.py',785),
  ('atributos_mkfile -> atributosSolo_mkfile','atributos_mkfile',1,'p_atributos_mkfile','DOSgramatica.py',786),
  ('atributosSolo_mkfile -> GUION PATH DIR','atributosSolo_mkfile',3,'p_atributoSolo_mkfile','DOSgramatica.py',794),
  ('atributosSolo_mkfile -> GUION SIZE STRING','atributosSolo_mkfile',3,'p_atributoSolo_mkfile','DOSgramatica.py',795),
  ('atributosSolo_mkfile -> GUION CONT STRING','atributosSolo_mkfile',3,'p_atributoSolo_mkfile','DOSgramatica.py',796),
  ('atributosSolo_mkfile -> GUION R','atributosSolo_mkfile',2,'p_atributoSolo_mkfile','DOSgramatica.py',797),
  ('comando -> CAT listaFilesCAT','comando',2,'p_comando_cat','DOSgramatica.py',814),
  ('listaFilesCAT -> listaFilesCAT atributosSolo_CAT','listaFilesCAT',2,'p_listaFilesCAT','DOSgramatica.py',888),
  ('listaFilesCAT -> atributosSolo_CAT','listaFilesCAT',1,'p_listaFilesCAT','DOSgramatica.py',889),
  ('atributosSolo_CAT -> GUION FILE2 STRING','atributosSolo_CAT',3,'p_atributoSolo_CAT','DOSgramatica.py',898),
  ('atributosSolo_CAT -> GUION FILE1 STRING','atributosSolo_CAT',3,'p_atributoSolo_CAT','DOSgramatica.py',899),
  ('comando -> REMOVE GUION PATH IGUAL DIR','comando',5,'p_comando_remove','DOSgramatica.py',908),
  ('comando -> EDIT listas_edit','comando',2,'p_comando_edit','DOSgramatica.py',920),
  ('listas_edit -> listas_edit atributosSolo_EDIT','listas_edit',2,'p_listaFilesEDIT','DOSgramatica.py',946),
  ('listas_edit -> atributosSolo_EDIT','listas_edit',1,'p_listaFilesEDIT','DOSgramatica.py',947),
  ('atributosSolo_EDIT -> GUION PATH IGUAL DIR','atributosSolo_EDIT',4,'p_atributoSolo_EDIT','DOSgramatica.py',955),
  ('atributosSolo_EDIT -> GUION CONT IGUAL DIR','atributosSolo_EDIT',4,'p_atributoSolo_EDIT','DOSgramatica.py',956),
  ('comando -> RENAME lista_rename','comando',2,'p_comando_rename','DOSgramatica.py',963),
  ('lista_rename -> lista_rename atributosSolo_RENAME','lista_rename',2,'p_listaFilesRENAME','DOSgramatica.py',990),
  ('lista_rename -> atributosSolo_RENAME','lista_rename',1,'p_listaFilesRENAME','DOSgramatica.py',991),
  ('atributosSolo_RENAME -> GUION PATH IGUAL DIR','atributosSolo_RENAME',4,'p_atributoSolo_RENAME','DOSgramatica.py',999),
  ('atributosSolo_RENAME -> GUION NAME IGUAL CADENA','atributosSolo_RENAME',4,'p_atributoSolo_RENAME','DOSgramatica.py',1000),
  ('comando -> MKDIR lista_mkdir','comando',2,'p_comando_mkdir','DOSgramatica.py',1007),
  ('lista_mkdir -> lista_mkdir atributosSolo_MKDIR','lista_mkdir',2,'p_listaFilesMKDIR','DOSgramatica.py',1035),
  ('lista_mkdir -> atributosSolo_MKDIR','lista_mkdir',1,'p_listaFilesMKDIR','DOSgramatica.py',1036),
  ('atributosSolo_MKDIR -> GUION PATH IGUAL DIR','atributosSolo_MKDIR',4,'p_atributoSolo_MKDIR','DOSgramatica.py',1044),
  ('atributosSolo_MKDIR -> GUION R','atributosSolo_MKDIR',2,'p_atributoSolo_MKDIR','DOSgramatica.py',1045),
  ('comando -> COPY lista_copy','comando',2,'p_comando_copy','DOSgramatica.py',1055),
  ('lista_copy -> lista_copy atributosSolo_COPY','lista_copy',2,'p_listaFilesCOPY','DOSgramatica.py',1083),
  ('lista_copy -> atributosSolo_COPY','lista_copy',1,'p_listaFilesCOPY','DOSgramatica.py',1084),
  ('atributosSolo_COPY -> GUION PATH IGUAL DIR','atributosSolo_COPY',4,'p_atributoSolo_COPY','DOSgramatica.py',1092),
  ('atributosSolo_COPY -> GUION DESTINO IGUAL DIR','atributosSolo_COPY',4,'p_atributoSolo_COPY','DOSgramatica.py',1093),
  ('comando -> EXECUTE GUION PATH DIR','comando',4,'p_comando_execute','DOSgramatica.py',1100),
]
