# coding=utf-8

'''
   Java set-get 代码生成
'''
import re

ORG_STR = '''
	private Long id;
	private String title;
	private String tag;
	private String preview1Url;
	private Double size;
	private String status;
	private String zipPath;
	private BigDecimal cost;
	private String channel;
	private String type;
	private String usableType;
	private String business;
	private String description;
	private String shareDescription;
	private Date createTime;
	private Date lastModifyTime;
		'''

SET_STR = "appThemeDto.set"
GET_STR = "this."

COMPILE = re.compile('[\s][\w]*;')

RS = COMPILE.finditer(ORG_STR)

for r in RS:
	# print(r.group(0))
	field = str(r.group(0)).strip()[0:-1]
	field_upper = field[0].upper()+field[1:]
	print(SET_STR+field_upper+'('+GET_STR+field+');')
