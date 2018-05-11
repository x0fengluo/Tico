#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 18/4/26 上午9:56
@license: Apache Licence 2.0
usege:
    ......

"""

import os


PATH = os.path.dirname(os.path.abspath(__file__))




# 选择主题，换皮肤时注意此处
THEMES='white'

# 站点副标题
SITE_TITLE ="黑白格博客"
# 站点页脚版权
SITE_FOOTER = '&copy 2018 个人github pages构建工具'


#个人md位置
PERSON_POST_PATH = PATH+'/source/_posts/'
PERSON_PAGE_PATH = PATH+'/source/_pages/'


#模板位置换皮肤时注意此处
SRC_TEMPLATE_PATH  = PATH+'/themes/'+THEMES+'/templates'
SRC_STATIC_PATH    = PATH+'/themes/'+THEMES+'/static'

#生成静态文件位置
DST_STATIC_PATH    =  PATH+'/html/static'
DST_TEMPLATE_PATH  =  PATH+'/html/templates'
DST_POSTS_PATH  =  PATH+'/html/templates/posts'
DST_CATEGORYS_PATH  =  PATH+'/html/templates/categorys'
DST_ARCHIVES_PATH  =  PATH+'/html/templates/archives'