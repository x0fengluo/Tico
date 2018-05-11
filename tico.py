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
import shutil
import codecs
from markdown import Markdown
from jinja2 import Environment, FileSystemLoader
from conf import  *


POSTS_DATA = []
CATEGORY_DATA = []
ARCHIVE_DATA = []

CATEGORY_DATA_DICT = {}

TEMPLATE_ENVIRONMENT = Environment(autoescape=False,loader=FileSystemLoader(SRC_TEMPLATE_PATH),trim_blocks=False)



def create_templates_post():
    """
    渲染单页面
    :return:
    """

    # 为post文件夹中每个文件成生页面
    for root, dirs, files in os.walk(PERSON_POST_PATH):
        for name in files:

            #打开需要的文件
            with codecs.open(PERSON_POST_PATH+name, mode="r", encoding="utf-8", errors='ignore') as f:
                body = f.read()
                md = Markdown(extensions=['fenced_code', 'codehilite(css_class=highlight,linenums=None)',
                                          'meta', 'admonition', 'tables'])

                #下面内容
                content = md.convert(body)

                #头内容
                meta = md.Meta if hasattr(md, 'Meta') else {}
                meta['url'] = DST_POSTS_PATH.split('/')[-1]+"/"+name.lower()+'.html'



                POSTS_DATA.append(meta)
                ARCHIVE_DATA.append(meta.get('datetime')[0])
                CATEGORY_DATA.append(meta.get('category')[0])


                if CATEGORY_DATA_DICT.get(meta.get('category')[0],False) ==False:
                    CATEGORY_DATA_DICT[meta.get('category')[0]] = []

                CATEGORY_DATA_DICT[meta.get('category')[0]].append({'url':name.lower()+'.html','title':meta.get('title')[0]})


                #渲染模板
                html = TEMPLATE_ENVIRONMENT.get_template('detail.html').render(
                    site_title = SITE_TITLE,
                    site_footer= SITE_FOOTER,
                    article_data=content,
                    article_head=dict(meta),
                    article_title=meta.get('title'))

                #生成posts所有页面
                if not os.path.exists(DST_POSTS_PATH):
                    os.makedirs(DST_POSTS_PATH)

                filename = name.lower() + ".html"
                with codecs.open(DST_POSTS_PATH + '/' + filename, 'w', 'utf-8') as f:
                    f.write(html)





def create_templates_index():
    """
    渲染首页
    :return:
    """

    #404 500页面
    shutil.copy(SRC_TEMPLATE_PATH+"/404.html", DST_TEMPLATE_PATH)
    shutil.copy(SRC_TEMPLATE_PATH+"/500.html", DST_TEMPLATE_PATH)
    shutil.copy(SRC_TEMPLATE_PATH+"/about.html", DST_TEMPLATE_PATH)
    shutil.copy(SRC_TEMPLATE_PATH+"/contact.html", DST_TEMPLATE_PATH)

    #生成INDEX下面的所有页面
    context = {
        'title' : SITE_TITLE,
        'footer':SITE_FOOTER,
        'posts' : POSTS_DATA,
        'categories' : list(set(CATEGORY_DATA)),
        'archives' : list(set(ARCHIVE_DATA)),

    }

    html = TEMPLATE_ENVIRONMENT.get_template("index.html").render(context)

    if not os.path.exists(DST_TEMPLATE_PATH):
        os.makedirs(DST_TEMPLATE_PATH)

    with codecs.open(DST_TEMPLATE_PATH + '/' + "index.html", 'w', 'utf-8') as f:
        f.write(html)


    #生成CATEGORY下面的所有页面
    for k,v in CATEGORY_DATA_DICT.items():

        cate = {
            'title': SITE_TITLE,
            'footer': SITE_FOOTER,
            "category":k,
            "posts":v,
            'categories' : list(set(CATEGORY_DATA)),
            'archives' : list(set(ARCHIVE_DATA)),

        }

        html = TEMPLATE_ENVIRONMENT.get_template("categorys.html").render(cate)

        # 生成分类下的所有页面
        if not os.path.exists(DST_CATEGORYS_PATH + "/" + k):
            os.makedirs(DST_CATEGORYS_PATH + "/" + k)

        with codecs.open(DST_CATEGORYS_PATH + "/" + k + '/' + "categorys.html", 'w', 'utf-8') as f:
            f.write(html)



def create_static():
    """
    创建所有css js image的文件夹static
    :return:
    """


    shutil.rmtree(DST_STATIC_PATH,ignore_errors=True)
    shutil.copytree(SRC_STATIC_PATH, DST_STATIC_PATH)



def main():
    create_static()

    create_templates_post()

    create_templates_index()



########################################
if __name__ == "__main__":
    main()
