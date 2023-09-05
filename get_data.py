import json
import requests

cookies = {
    'cookieId': '2BE9D395_FDF2_62A4_6914_BD30AF85B973',
    'RESOURCE_ADAPT_DEVICE': 'width%3D1920%26height%3D1080%26dpr%3D1%26mobile%3D0%26ios%3D0',
    'RESOURCE_ADAPT_WEBP': '1',
    '_csrf': '-YVeJpzJEI50M1LZmbkYaEl1',
    '_ym_uid': '1688924928910613710',
    '_ym_d': '1688924928',
    '_gcl_au': '1.1.1779055252.1688924928',
    'REVIEW_LIKE_TIPS': '1',
    'c': 't5usTb01-1688927230187-6d3722d08b812-1236862677',
    '_fmdata': 'dCTPe9%2FMjE0y1dN3h8hr%2FP6arnrb2D86eHYF24KG9HeItHR8yj%2Bc1VQU1uweZDmO2PZwxr7sLbG1Z72dPbnXlA%3D%3D',
    '_xid': '2VDBZsMZGC6omNBFqZ6qDtuF9KjIZ9fRxkHvS6HinoM%3D',
    'forterToken': 'd81121ee8e7249e5bf4736a3df077a88_1689509572121_111_UDFT15_17ck',
    'language': 'ru',
    'ssrAbt': 'hidequicktype%3DAtype%3Dsellingpointtype%3DBclose_prime_pricerule%3D1727_1766_767%3ABDetailNoShowQuickis_pde%3D3%26rule_id_120%3Drec_ver%3AS120V3.0%26rule_id_121%3Drec_ver%3AS121V2.1ZfreestylestripitemfreeshippingnonerangedetailtypelBLogisticsTimeASizeTipsBUnderPriceFeedsoffUnderPriceShowASameLabelbannerConnetlabelAGroupsameA3PsellerdeliveryshowdetailshowsellerinfonoshowCccDetailVideosheinxreinforcenew1goodsPicAbBdiscountLabelDetailFamilyOutfitscallnolimitstoreyesReportshowhidebigpicturenobigE_Price_CalNoneE_Price_AutoClaimNoneE_PriceCouponE_Price_AddOnItemNoneE_Time_LimitNotShowrec_ver_s152rec_verS152V1.0AdultProductAgeAspuPicshowMall_1',
    'country': 'RU',
    'countryId': '178',
    'sessionID_shein': 's%3AlPWgVI77R0vDX9luISYFWstW-Z0EMn2j.mo%2BmsHJxHqOWAiIwe3SisriVljnF7%2FcHV26MnJ%2BvRVs',
    '_abck': '05A0D2986D239DC40FA435FA23766E7A~0~YAAQs2pkXwv6g+WJAQAACKEpEgr8uKrYJJdB95RYtr+uxzoHX2gH6iuJslkP8Dxp1YHl+t4TS2ShBD1eUd3WqH83PazAaONpOZv4BPUtHZi//6visJ91iC4+h2vZYwrBjCjwUnFd4xmGajsnUTql4152zcZT9GVvdVC9TNOMIgQP+aquX8lpO/YhRVgXKwY02MaCcOSBAZrYfQhyAmQ6Qxy3gUWuqPFy+bMHCT4nArtA67vSxc+6oUKLPAzLNvZDX1P6yuvfuuhP+DJ6ihk593gGoulezYaqJdXqFPSpijnhQWEtoLDxywH6jsYew1sVJDl86kp04n7ZuQncv/mDQKm1AWb3RYDSOJeMMNbejq/JvmZ2znn2qc4jhvpMC7N+tlY/xSA1Gj/zZVX53DL+DQxDoOI=~-1~-1~-1',
    'bm_sz': '1B7EB950FB17C657EFCA55E01E0FB296~YAAQs2pkXw76g+WJAQAACKEpEhQpt6W2+PIhqbUyH5HTLzGvQrNOmOOYWlRKhLgJO8Z23IJS1xHyebcFJH10RNqgkMJvyBIRCdJaDh0C6jRlrBAwdaauSmP/fwOxWfZbR3JBHoOQSiH+6Xmr14Dy22RGwLNtWoxJc1TZxjbWQinqCKL67rvnhuSOP+R1VPnAP2DSAn9NUPNklU2AtUojXYRx1HeJK682RmBJy5lic0mtOKorhpZtUjsQMoioibNZ+cjJmuAhCVUZu0HGYADCvQHH3pxfegqNSkdYFM6g2mkYNQ==~3420728~4539446',
    'bm_mi': '02AD889B4033CDE693E815DD9B395399~YAAQs2pkX4r+g+WJAQAAxeUpEhTX2Uto/ZIlqBaX/rAYGVl+20MstQVjehe1jLmvkO7btnuBTN+unngqQ5EFnNHBzKAce8wL6xPjvXxmOijaRBj1dsyp1z1Ce45BB2qRmpsrgqcgqVYo/XBsCyaUFd0gfBSLlSp55bBl6GM6ejs6Z4RF2IlwfDx9sHAL1WlWFvut0gMNbviCuEKAWN1pGu/Kl5IbQXoSbi9dH/iYd5k4V35XuUihYW/eQ3wONxrYl8nZotx/99uddqItCI8yU5wOh4CGNoCrhZNUkqBKlUCo0MS8iXH7Bm9OaF8dpIwk0wqzwNjseFWufBey/Pm3MSKjd649St/7PeSbvaz7inlbI6KThvwNuHCEESlZF2qcokBoivjpv82fxrdyg1j3gBjYOauIpQ==~1',
    '_gid': 'GA1.2.374176831.1692521855',
    'WEB_UGID_INIT': '1',
    'ak_bmsc': 'D1355F4F82AC01F085FB1E8B9400DD62~000000000000000000000000000000~YAAQs2pkXz0AhOWJAQAASfkpEhQUHKjpUeze7ukU1T7A9oySyLMWWxdAQLyNb42BusauvFQ0nDC3eV8g8WRFKNFl7PDfI1sS7jczCJjBex4yXL9n2T3LnItlK97i1zl/4Sbp4k/vyrL5L9SYGzt6DZ9vkNJ+StnQoLhscRPT+x7KTxJ2pNmy5Go2TMc6Tw5m7YlfTqJcUg/4WKRiVI0ZBpxHrOxACMSv4G5CWtoGiXKKiEv+o/JT+E1Y2fLGMM1x9onu7RCEObhm9Q9+o2hDAl2kEy410doojl+6cBRAR9uZRgoasSDjrVByO5xmAhIx2JHX0DZhQo97OySi+6ZWmfi3K4Woao9QcuxTst5j4Qr48qFKIW2WC7hgDtM9QFxIo7NHlfYgJdT9iM+Dn0mMM4vAsvZ+gFx+TY6/XCZmgNMw//hoB4ixIyChdi4wuy2fxQmej3CGfSsORDSG8Op+cqajgzRhaN5K07HjJqUjo1qO3JL9MtE+rjCd+4fpmObEPUAKyXzWNE1iJEn8W3j5k/uQNNQfLzBleoH+Y7XnIFUVYrY56RzyhnwxX10QN1fGtLV93LcxQ2gWQJNCcE4Sro2Vot0Fk5DUWXOPWmmMwmrMjI6oe4g=',
    'app_country': 'RU',
    '_ym_isad': '2',
    'g_state': '{"i_p":1692529059594,"i_l":1}',
    'have_show': '1',
    '_cfuvid': '8EtmRvq2SO7WCapM88D4Omkj2YjNSu8ZCvKr9g0Yb78-1692521920559-0-604800000',
    'cf_clearance': 'exNuVatnDdRBcg705RqWgsz7maGcPcMue9.ODhVTbFA-1692521921-0-1-fc47acb6.2a811456.ab46f356-0.2.1692521921',
    'jump_to_ru': '1',
    'no_pop_up_ru': '1',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Sun+Aug+20+2023+12%3A17%3A48+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.13.0&hosts=&consentId=73bee6ff-a344-4492-9664-1f0112a38ea1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=RU%3BCU',
    'OptanonAlertBoxClosed': '2023-08-20T09:17:48.344Z',
    'bi_session_id': 'bi_1692523744259_31273',
    'default_currency_expire': '1',
    'ftr_blst_1h': '1692526375642',
    'cate_channel_type': '2',
    'addressCookie': '%7B%22countryId%22%3A%22178%22%2C%22createdTime%22%3A1692527297308%2C%22isUserHandle%22%3A%221%22%2C%22siteUid%22%3A%22ru%22%7D',
    'forterToken': 'd81121ee8e7249e5bf4736a3df077a88_1692527299109_991_dUAL43-m9-a9-d4_17ck',
    '_ga': 'GA1.1.1156353816.1688924925',
    '_ga_SC3MXK8VH1': 'GS1.1.1692521857.14.1.1692527536.60.0.0',
    'bm_sv': '58EEF3DD4672817D8DC0A99DEC9812A1~YAAQ5g8fuIcIjgKKAQAAXg2QEhT+LR4UTPAx1Ww2LXkg7viWRbgNeiuNizRRNH6KTf7g+OZUaL8Q657C2VPYPsreZFIwGL2BGZZ7cf8qvmLKKHh4FtmrlzwNjREbNgOkjPZ9p7peIzzHryOZ8AVFTowPar+mIKjYv0QcE4u14Y0TDqBNiC7UZiVy6f31/P3XjAyB1GI0kWR7snyxdAeU+RWrS/Cr4xi0Z8oRRuYzHBpu+DgQMZY8O7va/myfQRTkeA==~1',
    '_gat_shein': '1',
}

headers = {
    'authority': 'ru.shein.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'cookieId=2BE9D395_FDF2_62A4_6914_BD30AF85B973; RESOURCE_ADAPT_DEVICE=width%3D1920%26height%3D1080%26dpr%3D1%26mobile%3D0%26ios%3D0; RESOURCE_ADAPT_WEBP=1; _csrf=-YVeJpzJEI50M1LZmbkYaEl1; _ym_uid=1688924928910613710; _ym_d=1688924928; _gcl_au=1.1.1779055252.1688924928; REVIEW_LIKE_TIPS=1; c=t5usTb01-1688927230187-6d3722d08b812-1236862677; _fmdata=dCTPe9%2FMjE0y1dN3h8hr%2FP6arnrb2D86eHYF24KG9HeItHR8yj%2Bc1VQU1uweZDmO2PZwxr7sLbG1Z72dPbnXlA%3D%3D; _xid=2VDBZsMZGC6omNBFqZ6qDtuF9KjIZ9fRxkHvS6HinoM%3D; forterToken=d81121ee8e7249e5bf4736a3df077a88_1689509572121_111_UDFT15_17ck; language=ru; ssrAbt=hidequicktype%3DAtype%3Dsellingpointtype%3DBclose_prime_pricerule%3D1727_1766_767%3ABDetailNoShowQuickis_pde%3D3%26rule_id_120%3Drec_ver%3AS120V3.0%26rule_id_121%3Drec_ver%3AS121V2.1ZfreestylestripitemfreeshippingnonerangedetailtypelBLogisticsTimeASizeTipsBUnderPriceFeedsoffUnderPriceShowASameLabelbannerConnetlabelAGroupsameA3PsellerdeliveryshowdetailshowsellerinfonoshowCccDetailVideosheinxreinforcenew1goodsPicAbBdiscountLabelDetailFamilyOutfitscallnolimitstoreyesReportshowhidebigpicturenobigE_Price_CalNoneE_Price_AutoClaimNoneE_PriceCouponE_Price_AddOnItemNoneE_Time_LimitNotShowrec_ver_s152rec_verS152V1.0AdultProductAgeAspuPicshowMall_1; country=RU; countryId=178; sessionID_shein=s%3AlPWgVI77R0vDX9luISYFWstW-Z0EMn2j.mo%2BmsHJxHqOWAiIwe3SisriVljnF7%2FcHV26MnJ%2BvRVs; _abck=05A0D2986D239DC40FA435FA23766E7A~0~YAAQs2pkXwv6g+WJAQAACKEpEgr8uKrYJJdB95RYtr+uxzoHX2gH6iuJslkP8Dxp1YHl+t4TS2ShBD1eUd3WqH83PazAaONpOZv4BPUtHZi//6visJ91iC4+h2vZYwrBjCjwUnFd4xmGajsnUTql4152zcZT9GVvdVC9TNOMIgQP+aquX8lpO/YhRVgXKwY02MaCcOSBAZrYfQhyAmQ6Qxy3gUWuqPFy+bMHCT4nArtA67vSxc+6oUKLPAzLNvZDX1P6yuvfuuhP+DJ6ihk593gGoulezYaqJdXqFPSpijnhQWEtoLDxywH6jsYew1sVJDl86kp04n7ZuQncv/mDQKm1AWb3RYDSOJeMMNbejq/JvmZ2znn2qc4jhvpMC7N+tlY/xSA1Gj/zZVX53DL+DQxDoOI=~-1~-1~-1; bm_sz=1B7EB950FB17C657EFCA55E01E0FB296~YAAQs2pkXw76g+WJAQAACKEpEhQpt6W2+PIhqbUyH5HTLzGvQrNOmOOYWlRKhLgJO8Z23IJS1xHyebcFJH10RNqgkMJvyBIRCdJaDh0C6jRlrBAwdaauSmP/fwOxWfZbR3JBHoOQSiH+6Xmr14Dy22RGwLNtWoxJc1TZxjbWQinqCKL67rvnhuSOP+R1VPnAP2DSAn9NUPNklU2AtUojXYRx1HeJK682RmBJy5lic0mtOKorhpZtUjsQMoioibNZ+cjJmuAhCVUZu0HGYADCvQHH3pxfegqNSkdYFM6g2mkYNQ==~3420728~4539446; bm_mi=02AD889B4033CDE693E815DD9B395399~YAAQs2pkX4r+g+WJAQAAxeUpEhTX2Uto/ZIlqBaX/rAYGVl+20MstQVjehe1jLmvkO7btnuBTN+unngqQ5EFnNHBzKAce8wL6xPjvXxmOijaRBj1dsyp1z1Ce45BB2qRmpsrgqcgqVYo/XBsCyaUFd0gfBSLlSp55bBl6GM6ejs6Z4RF2IlwfDx9sHAL1WlWFvut0gMNbviCuEKAWN1pGu/Kl5IbQXoSbi9dH/iYd5k4V35XuUihYW/eQ3wONxrYl8nZotx/99uddqItCI8yU5wOh4CGNoCrhZNUkqBKlUCo0MS8iXH7Bm9OaF8dpIwk0wqzwNjseFWufBey/Pm3MSKjd649St/7PeSbvaz7inlbI6KThvwNuHCEESlZF2qcokBoivjpv82fxrdyg1j3gBjYOauIpQ==~1; _gid=GA1.2.374176831.1692521855; WEB_UGID_INIT=1; ak_bmsc=D1355F4F82AC01F085FB1E8B9400DD62~000000000000000000000000000000~YAAQs2pkXz0AhOWJAQAASfkpEhQUHKjpUeze7ukU1T7A9oySyLMWWxdAQLyNb42BusauvFQ0nDC3eV8g8WRFKNFl7PDfI1sS7jczCJjBex4yXL9n2T3LnItlK97i1zl/4Sbp4k/vyrL5L9SYGzt6DZ9vkNJ+StnQoLhscRPT+x7KTxJ2pNmy5Go2TMc6Tw5m7YlfTqJcUg/4WKRiVI0ZBpxHrOxACMSv4G5CWtoGiXKKiEv+o/JT+E1Y2fLGMM1x9onu7RCEObhm9Q9+o2hDAl2kEy410doojl+6cBRAR9uZRgoasSDjrVByO5xmAhIx2JHX0DZhQo97OySi+6ZWmfi3K4Woao9QcuxTst5j4Qr48qFKIW2WC7hgDtM9QFxIo7NHlfYgJdT9iM+Dn0mMM4vAsvZ+gFx+TY6/XCZmgNMw//hoB4ixIyChdi4wuy2fxQmej3CGfSsORDSG8Op+cqajgzRhaN5K07HjJqUjo1qO3JL9MtE+rjCd+4fpmObEPUAKyXzWNE1iJEn8W3j5k/uQNNQfLzBleoH+Y7XnIFUVYrY56RzyhnwxX10QN1fGtLV93LcxQ2gWQJNCcE4Sro2Vot0Fk5DUWXOPWmmMwmrMjI6oe4g=; app_country=RU; _ym_isad=2; g_state={"i_p":1692529059594,"i_l":1}; have_show=1; _cfuvid=8EtmRvq2SO7WCapM88D4Omkj2YjNSu8ZCvKr9g0Yb78-1692521920559-0-604800000; cf_clearance=exNuVatnDdRBcg705RqWgsz7maGcPcMue9.ODhVTbFA-1692521921-0-1-fc47acb6.2a811456.ab46f356-0.2.1692521921; jump_to_ru=1; no_pop_up_ru=1; OptanonConsent=isIABGlobal=false&datestamp=Sun+Aug+20+2023+12%3A17%3A48+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.13.0&hosts=&consentId=73bee6ff-a344-4492-9664-1f0112a38ea1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=RU%3BCU; OptanonAlertBoxClosed=2023-08-20T09:17:48.344Z; bi_session_id=bi_1692523744259_31273; default_currency_expire=1; ftr_blst_1h=1692526375642; cate_channel_type=2; addressCookie=%7B%22countryId%22%3A%22178%22%2C%22createdTime%22%3A1692527297308%2C%22isUserHandle%22%3A%221%22%2C%22siteUid%22%3A%22ru%22%7D; forterToken=d81121ee8e7249e5bf4736a3df077a88_1692527299109_991_dUAL43-m9-a9-d4_17ck; _ga=GA1.1.1156353816.1688924925; _ga_SC3MXK8VH1=GS1.1.1692521857.14.1.1692527536.60.0.0; bm_sv=58EEF3DD4672817D8DC0A99DEC9812A1~YAAQ5g8fuIcIjgKKAQAAXg2QEhT+LR4UTPAx1Ww2LXkg7viWRbgNeiuNizRRNH6KTf7g+OZUaL8Q657C2VPYPsreZFIwGL2BGZZ7cf8qvmLKKHh4FtmrlzwNjREbNgOkjPZ9p7peIzzHryOZ8AVFTowPar+mIKjYv0QcE4u14Y0TDqBNiC7UZiVy6f31/P3XjAyB1GI0kWR7snyxdAeU+RWrS/Cr4xi0Z8oRRuYzHBpu+DgQMZY8O7va/myfQRTkeA==~1; _gat_shein=1',
    'pragma': 'no-cache',
    'referer': 'https://ru.shein.com/men?ici=ru_tab04',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
}

params = {
    'ici': 'ru_tab04navbar02',
    'src_module': 'topcat',
    'src_tab_page_id': 'page_home1692525337608',
    'src_identifier': 'fc=Men`sc=РАСПРОДАЖА`tc=0`oc=0`ps=tab04navbar02`jc=itemPicking_00511758',
    'srctype': 'category',
    'userpath': 'category-РАСПРОДАЖА',
}


def get_data1(show_only, use_sorting, gender, max_price, page_count):
    pages = page_count
    men = 'https://ru.shein.com/sale/Men-On-Sale-sc-00511758.html'
    women = 'https://ru.shein.com/promotion/Total-sc-02560281.html'
    if gender == 'мужчины':
        url = men
    elif gender == 'женщины':
        url = women
    for page in range(0, pages):
        response = requests.get(
            f'{url}?child_cat_id={show_only}&max_price={max_price}&page={page + 1}&sort={use_sorting}', params=params,
            cookies=cookies, headers=headers).text
        text = response[response.index('"goods":', 2) + 8: response.index("selectedCate") - 2]
        text = text[text.index('"goods":', 2) + 8:]
        goods_data = json.loads(text)
        goods_id_list = [item['goods_id'] for item in goods_data]
        goods_cat_list = [item['cat_id'] for item in goods_data]
        goods_images = [item['goods_img'][2:] for item in goods_data]
        goods_urlname_list = [item['goods_url_name'] for item in goods_data]
        # detail_urls = [item['detail_url'] for item in goods_data]
        detail_urls = []
        goods_sns = [item['goods_sn'] for item in goods_data]

        for i in range(len(goods_id_list)):
            # print(f'https://ru.shein.com/{detail_urls[i]}.html\n',
            detail_urls.append(
                f'https://ru.shein.com/{goods_urlname_list[i].replace(" ", "-")}-p-{goods_id_list[i]}-cat-{goods_cat_list[i]}.html\n')
        # f'https://{goods_images[i]}')
        return detail_urls, goods_id_list, goods_sns, goods_cat_list, goods_images


def get_data2(i, discont, detail_urls, goods_id_list, goods_sns, goods_cat_list, goods_images):
    discont = int(discont)
    json_data = {
        'atomicParams': [
            {
                'mall_code': '1',
                'goods_id': goods_id_list[i],
                'goods_sn': goods_sns[i],
                'cat_id': goods_cat_list[i],
            },
        ],
        'fields': {
            'prices': True,
            'promotion': True,
            'topPick': False,
            'seriesAndBrand': True,
            'sellingPoints': True,
            'videoIcon': False,
            'cccTspBadges': True,
            'enableDecisionAttr': False,
            'locateLabels': 'default',
            'wish': True,
            'stock': True,
            'sheinClubPromotionInfo': False,
            'newFlashPromotion': True,
            'promoLabel': False,
            'realTimeTspLabels': {
                'machine_label': [
                    '3598',
                ],
            },
            'userBehaviorLabel': True,
            'userCommentKeywordsLabel': True,
            'beltLabel': True,
            'rankingList': True,
            'vipDiscountPrices': True,
            'estimatedPrice': False,
            'tspLabels': '',
        },
        'isPaid': 0,
        'scene': {
            'sceneKey': 'TWO_IN_A_ROW',
            'pageKey': 'page_select_class',
            'subPageKey': '',
        },
        'cccParams': {
            'cateId': '00511758',
        },
    }
    response = requests.post(
        'https://ru.shein.com/api/productAtom/atomicInfo/get',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).text
    response = '[' + response + ']'
    goods_data = json.loads(response)
    goods_retale_price = [item['data'][f'{goods_id_list[i]}']['retailPrice']['amountWithSymbol'] for item in
                          goods_data]
    goods_sale_price = [item['data'][f'{goods_id_list[i]}']["salePrice"]['amountWithSymbol'] for item in
                        goods_data]
    goods_discount = [item['data'][f'{goods_id_list[i]}']['unit_discount'] for item in
                      goods_data]
    if goods_discount[0] >= discont:
        return f'https://ru.shein.com/{detail_urls[i]}', f'{goods_images[i]}\n', goods_retale_price[0], \
            goods_sale_price[0], goods_discount[0]
    else:
        return '', '', '', '', ''
