# coding=utf-8

'''
   Java set-get 代码生成
'''
import re

ORG_STR = '''
	private long id;
    private long feideeUser;
    private long ssjUser;
    private int type;
    private int isDefault;
    private Date createTime;
    private Date lastModifyTime;
		'''

SET_STR = "bookAndRelationMap.put(\""
GET_STR = "bookRelationDto.get"

COMPILE = re.compile('[\s][\w]*;')

RS = COMPILE.finditer(ORG_STR)

for r in RS:
	# print(r.group(0))
	field = str(r.group(0)).strip()[0:-1]
	field_upper = field[0].upper()+field[1:]
	print(SET_STR+field+'", '+GET_STR+field_upper+'());')
