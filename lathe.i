%module lathe
%{
#include "../LatheX/include/lathe.h"
#include "Lathe/stdafx.h"
#define EXT
#define int32_t int
#define uint16_t unsigned short int
#define int16_t short int
#include "../LatheX/include/remvardef.h"
%}

#define EXT
#define INCLUDE 1
%include "../LatheX/src/lathe.c"
#if 1
#define int32_t int
#define uint16_t unsigned short int
#define int16_t short int
%include "../LatheX/include/remvardef.h"
#endif
