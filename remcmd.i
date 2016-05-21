%module remcmd
%{
#define EXT
#define int32_t int
#define uint16_t unsigned short int
#define int16_t short int
#include "../LatheX/include/remvardef.h"
#undef EXT
#include "../LatheX/include/remcmd.h"
%}

%include "../LatheX/include/cmdList.h"
%include "../LatheX/include/parmList.h"
%include "../LatheX/src/remcmd.c"
