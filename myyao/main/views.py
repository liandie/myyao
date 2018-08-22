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

from django.shortcuts import render

def page_error(request):
    return render(request, '404.html')


def girl(request):
    return render(request, 'girl/girl.html')

def boy(request):
    return render(request, 'boy/boy.html')

def blog1(request):
    return render(request, 'blog1/index.html')

def blog1_share(request):
    return render(request, 'blog1/share.html')

def blog1_list(request):
    return render(request, 'blog1/list.html')

def blog1_about(request):
    return render(request, 'blog1/about.html')

def blog1_gbook(request):
    return render(request, 'blog1/gbook.html')

def blog1_info(request):
    return render(request, 'blog1/info.html')

def blog1_infopic(request):
    return render(request, 'blog1/infopic.html')

def blog2(request):
    return render(request, 'blog2/index.html')

def blog3(request):
    return render(request, 'blog3/index.html')

def blog3_typography(request):
    return render(request, 'blog3/typography.html')

def blog3_blog(request):
    return render(request, 'blog3/blog.html')

def blog3_gallery(request):
    return render(request, 'blog3/gallery.html')

def blog3_contact(request):
    return render(request, 'blog3/contact.html')

def blog3_single(request):
    return render(request, 'blog3/single.html')

def photo1(request):
    return render(request, 'photo1/index.html')

def photo1_about(request):
    return render(request, 'photo1/about.html')

def photo1_faq(request):
    return render(request, 'photo1/faq.html')

def photo1_price(request):
    return render(request, 'photo1/price.html')

def photo1_register(request):
    return render(request, 'photo1/register.html')

def photo1_single(request):
    return render(request, 'photo1/single.html')

def photo1_stock(request):
    return render(request, 'photo1/stock.html')

def photo1_support(request):
    return render(request, 'photo1/support.html')

def photo2(request):
    return render(request, 'photo2/index.html')

def photo2_about(request):
    return render(request, 'photo2/about.html')

def photo2_account(request):
    return render(request, 'photo2/account.html')

def photo2_codes(request):
    return render(request, 'photo2/codes.html')

def photo2_contact(request):
    return render(request, 'photo2/contact.html')

def photo2_gallery(request):
    return render(request, 'photo2/gallery.html')

def photo2_news(request):
    return render(request, 'photo2/news.html')

def photo3(request):
    return render(request, 'photo3/index.html')

def photo3_index_1(request):
    return render(request, 'photo3/index-1.html')

def photo3_index_2(request):
    return render(request, 'photo3/index-2.html')

def photo3_index_3(request):
    return render(request, 'photo3/index-3.html')

def photo3_index_4(request):
    return render(request, 'photo3/index-4.html')

def photo4(request):
    return render(request, 'photo4/index.html')

def photo4_0_base_file(request):
    return render(request, 'photo4/0-base-file.html')

def photo4_404(request):
    return render(request, 'photo4/404.html')

def photo4_aboutus(request):
    return render(request, 'photo4/aboutus.html')

def photo4_backup(request):
    return render(request, 'photo4/backup.html')

def photo4_blog_single(request):
    return render(request, 'photo4/blog-single.html')

def photo4_blog1(request):
    return render(request, 'photo4/blog1.html')

def photo4_blog2(request):
    return render(request, 'photo4/blog2.html')

def photo4_contactus(request):
    return render(request, 'photo4/contactus.html')

def photo4_faq(request):
    return render(request, 'photo4/faq.html')

def photo4_gallery(request):
    return render(request, 'photo4/gallery.html')

def photo4_grid(request):
    return render(request, 'photo4/grid.html')

def photo4_login(request):
    return render(request, 'photo4/login.html')

def photo4_portfolio_single(request):
    return render(request, 'photo4/portfolio-single.html')

def photo4_pricing(request):
    return render(request, 'photo4/pricing.html')

def photo4_register(request):
    return render(request, 'photo4/register.html')

def photo4_service(request):
    return render(request, 'photo4/service.html')

def photo4_sitemap(request):
    return render(request, 'photo4/sitemap.html')

def photo5(request):
    return render(request, 'photo5/index.html')