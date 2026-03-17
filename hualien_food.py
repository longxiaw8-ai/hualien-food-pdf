#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
花蓮美食 PDF 生成器
Usage: python3 hualien_food.py
"""

from fpdf import FPDF
import os

# 花蓮美食資料
hualien_foods = [
    {
        "name": "液香扁食",
        "type": "小吃",
        "address": "花蓮市中山路 136 號",
        "description": "花蓮知名扁食店，皮薄餡多，湯頭清淡鲜美",
        "must_try": "⭐ 扁食湯"
    },
    {
        "name": "炸彈蔥油餅",
        "type": "小吃",
        "address": "花蓮市重庆路 & 中山路交叉口",
        "description": "外酥内軟的蔥油餅，内含半熟蛋，香氣四溢",
        "must_try": "⭐ 炸彈蔥油餅"
    },
    {
        "name": "公正街包子店",
        "type": "小吃",
        "address": "花蓮市公正街 14-1 號",
        "description": "24小時營業的排隊名店，肉包汁多味美",
        "must_try": "⭐ 肉包、菜包"
    },
    {
        "name": "海埔蚵仔煎",
        "type": "小吃",
        "address": "花蓮市自由街 86 號",
        "description": "花蓮最老的蚵仔煎老店，粉漿Q彈，蚵仔新鮮",
        "must_try": "⭐ 蚵仔煎"
    },
    {
        "name": "一心泡泡冰",
        "type": "甜品",
        "address": "花蓮市節約街 27 號",
        "description": "古早味剉冰，水果口味多样",
        "must_try": "⭐ 芒果冰、草莓冰"
    },
    {
        "name": "廟口咖喱飯",
        "type": "餐廳",
        "address": "花蓮市福全镇 36-6 號",
        "description": "日式咖喱飯，香氣濃郁，配料豐富",
        "must_try": "⭐ 咖喱飯、炸豬排"
    },
    {
        "name": "米噹泰式料理",
        "type": "餐廳",
        "address": "花蓮市中美路 78-1 號",
        "description": "正宗泰式料理，平價美味",
        "must_try": "⭐ 泰式酸辣湯、涼拌青木瓜"
    },
    {
        "name": "闔家歡南北什",
        "type": "餐廳",
        "address": "花蓮市和平路 581 號",
        "description": "中式合菜，適合家庭聚餐",
        "must_try": "⭐ 炒時蔬、白切雞"
    },
    {
        "name": "欣欣麵館",
        "type": "小吃",
        "address": "花蓮市中山路 169 巷 6 號",
        "description": "古早味麵店，滷味是一絕",
        "must_try": "⭐ 乾麵、滷味拼盤"
    },
    {
        "name": "陳記狀元粥",
        "type": "小吃",
        "address": "花蓮市節約街 28 號",
        "description": "料多味美的粥品，早餐宵夜都適合",
        "must_try": "⭐ 海鮮粥、皮蛋瘦肉粥"
    }
]

class FoodPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(200, 80, 80)  # 紅色
        self.cell(0, 15, '花蓮美食推薦', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_food_pdf():
    pdf = FoodPDF()
    pdf.add_page()
    
    # 標題資訊
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, '整理日期：2026年3月17日', 0, 1, 'C')
    pdf.ln(5)
    
    # 美食列表
    for i, food in enumerate(hualien_foods, 1):
        # 餐廳名稱
        pdf.set_font('Arial', 'B', 14)
        pdf.set_text_color(0, 100, 200)
        pdf.cell(0, 10, f'{i}. {food["name"]}', 0, 1, 'L')
        
        # 類型
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(0, 6, f'類型：{food["type"]}', 0, 1, 'L')
        
        # 地址
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(0, 6, f'地址：{food["address"]}', 0, 1, 'L')
        
        # 描述
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 6, f'簡介：{food["description"]}')
        
        # 必點
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(255, 140, 0)
        pdf.cell(0, 6, food['must_try'], 0, 1, 'L')
        
        pdf.ln(8)
        
        # 分隔線
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
    
    # 輸出 PDF
    output_path = '花蓮美食推薦.pdf'
    pdf.output(output_path)
    print(f'✅ PDF 已生成：{output_path}')
    return output_path

if __name__ == '__main__':
    create_food_pdf()
