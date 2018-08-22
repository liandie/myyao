#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6.5
@author: myyao
@license: python
@contact: longzinziyan@gmail.com
@software: PyCharm
@file: views.py
@time: 2018/4/13 20:37
"""
from django.conf.urls import url
from .import views 

handler403 = views.page_error
handler404 = views.page_error
handler500 = views.page_error


urlpatterns = [
    url(r'^girl$|^girl/$^',views.girl,name='girl'),
    
    url(r'^boy$|^boy/$',views.boy,name='boy'),

    url(r'^blog2$|^blog2/$',views.blog2,name='blog2'),

    url(r'^blog1$|^blog1/$',views.blog1,name='blog1'),
    url(r'^blog1_share$|^blog1_share/$',views.blog1_share,name='blog1_share'),
    url(r'^blog1_list$|^blog1_list/$',views.blog1_list,name='blog1_list'),
    url(r'^blog1_about$|^blog1_about/$',views.blog1_about,name='blog1_about'),
    url(r'^blog1_gbook$|^blog1_gbook/$',views.blog1_gbook,name='blog1_gbook'),
    url(r'^blog1_info$|^blog1_info/$',views.blog1_info,name='blog1_info'),
    url(r'^blog1_infopic$|^blog1_infopic/$',views.blog1_infopic,name='blog1_infopic'),

    url(r'^blog3$|^blog3/$',views.blog3,name='blog3'),
    url(r'^blog3_typography$|^blog3_typography/$',views.blog3_typography,name='blog3_typography'),
    url(r'^blog3_blog$|^blog3_blog/$',views.blog3_blog,name='blog3_blog'),
    url(r'^blog3_gallery$|^blog3_gallery/$',views.blog3_gallery,name='blog3_gallery'),
    url(r'^blog3_contact$|^blog3_contact/$',views.blog3_contact,name='blog3_contact'),
    url(r'^blog3_single$|^blog3_single/$',views.blog3_single,name='blog3_single'),

    url(r'^photo1$|^photo1/$',views.photo1,name='photo1'),
    url(r'^photo1_about$|^photo1_about/$',views.photo1_about,name='photo1_about'),
    url(r'^photo1_faq$|^photo1_faq/$',views.photo1_faq,name='photo1_faq'),
    url(r'^photo1_price$|^photo1_price/$',views.photo1_price,name='photo1_price'),
    url(r'^photo1_register$|^photo1_register/$',views.photo1_register,name='photo1_register'),
    url(r'^photo1_single$|^photo1_single/$',views.photo1_single,name='photo1_single'),
    url(r'^photo1_stock$|^photo1_stock/$',views.photo1_stock,name='photo1_stock'),
    url(r'^photo1_support$|^photo1_support/$',views.photo1_support,name='photo1_support'),

    url(r'^photo2$|^photo2/$',views.photo2,name='photo2'),
    url(r'^photo2_about$|^photo2_about/$',views.photo2_about,name='photo2_about'),
    url(r'^photo2_account$|^photo2_account/$',views.photo2_account,name='photo2_account'),
    url(r'^photo2_codes$|^photo2_codes/$',views.photo2_codes,name='photo2_codes'),
    url(r'^photo2_contact$|^photo2_contact/$',views.photo2_contact,name='photo2_contact'),
    url(r'^photo2_gallery$|^photo2_gallery/$',views.photo2_gallery,name='photo2_gallery'),
    url(r'^photo2_news$|^photo2_news/$',views.photo2_news,name='photo2_news'),

    url(r'^photo3$|^photo3/$',views.photo3,name='photo3'),
    url(r'^photo3_index_1$|^photo3_index_1/$',views.photo3_index_1,name='photo3_index_1'),
    url(r'^photo3_index_2$|^photo3_index_2/$',views.photo3_index_2,name='photo3_index_2'),
    url(r'^photo3_index_3$|^photo3_index_3/$',views.photo3_index_3,name='photo3_index_3'),
    url(r'^photo3_index_4|^photo3_index_4/$',views.photo3_index_4,name='photo3_index_4'),

    url(r'^photo4$|^photo4/$',views.photo4,name='photo4'),
    url(r'^photo4_0_base_file$|^photo4_0_base_file/$',views.photo4_0_base_file,name='photo4_0_base_file'),
    url(r'^photo4_404$|^photo4_404/$',views.photo4_404,name='photo4_404'),
    url(r'^photo4_aboutus$|^photo4_aboutus/$',views.photo4_aboutus,name='photo4_aboutus'),
    url(r'^photo4_backup$|^photo4_backup/$',views.photo4_backup,name='photo4_backup'),
    url(r'^photo4_blog_single$|^photo4_blog_single/$',views.photo4_blog_single,name='photo4_blog_single'),
    url(r'^photo4_blog1$|^photo4_blog1/$',views.photo4_blog1,name='photo4_blog1'),
    url(r'^photo4_blog2$|^photo4_blog2/$',views.photo4_blog2,name='photo4_blog2'),
    url(r'^photo4_contactus$|^photo4_contactus/$',views.photo4_contactus,name='photo4_contactus'),
    url(r'^photo4_faq$|^photo4_faq/$',views.photo4_faq,name='photo4_faq'),
    url(r'^photo4_gallery$|^photo4_gallery/$',views.photo4_gallery,name='photo4_gallery'),
    url(r'^photo4_grid$|^photo4_grid/$',views.photo4_grid,name='photo4_grid'),
    url(r'^photo4_login$|^photo4_login/$',views.photo4_login,name='photo4_login'),
    url(r'^photo4_portfolio_single$|^photo4_portfolio_single/$',views.photo4_portfolio_single,name='photo4_portfolio_single'),
    url(r'^photo4_pricing$|^photo4_pricing/$',views.photo4_pricing,name='photo4_pricing'),
    url(r'^photo4_register$|^photo4_register/$',views.photo4_register,name='photo4_register'),
    url(r'^photo4_service$|^photo4_service/$',views.photo4_service,name='photo4_service'),
    url(r'^photo4_sitemap$|^photo4_sitemap/$',views.photo4_sitemap,name='photo4_sitemap'),

    url(r'^photo5$|^photo5/$',views.photo5,name='photo5'),

]
