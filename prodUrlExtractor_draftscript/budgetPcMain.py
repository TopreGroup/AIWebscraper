from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv 
import re
import os
from lxml import html
from budgetPcCat import budgetCat as bc
from budgetProdDescrip import budgetProd as bd 
import time


# r = requests.get("https://www.budgetpc.com.au/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# c = r.content

# soup = BeautifulSoup(c,"html.parser")


# dropDownCat = soup.find( "div", {"class":"span12"}).findChildren()
# # print(type(dropDownCat))
# # print(len(dropDownCat))
# temp =[]
# href =[]
# for i in range(len(dropDownCat)):
#     holder = dropDownCat[i].get("href")
#     if holder is not None and "html" in holder:
#         href.append(holder)
      
# print(len(href))

# for i in range(len(href)):
#     row = href[i]
#     file1 = open("href.txt","a")    
#     file1.write( row+"\n") 
#     file1.close() 
# # File_object = open(r"hrefs","Access_Mode")       

# Refurbished urls
# a = "https://www.budgetpc.com.au/refurbished-products-77.html"
# b = "https://www.budgetpc.com.au/refurbished-products-77/refurbished-computers.html"
# c ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-all-in-one-computers.html"
# d ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-notebooks.html"
# e ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-monitors.html"
# f ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-tablets.html"
# g ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-workstations.html"
# h ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-servers.html"
# i ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-server-parts.html"
# j = "https://www.budgetpc.com.au/refurbished-products-77/refurbished-networking-products.html"
# k ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-thin-clients.html"
# l ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-accessories.html"
# m ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-storage-products.html"
# n ="https://www.budgetpc.com.au/refurbished-products-77/refurbished-photo-copiers.html"
# href = [b,c,d,e,f,g,h,i,j,k,l,m,n]
# Computer & servers


# # a= "https://www.budgetpc.com.au/computers-servers.html"
# b= "https://www.budgetpc.com.au/computers-servers/branded-computers.html"
# c ="https://www.budgetpc.com.au/computers-servers/branded-computers/desktop-computers.html"
# d="https://www.budgetpc.com.au/computers-servers/branded-computers/workstations.html"
# e="https://www.budgetpc.com.au/computers-servers/branded-computers/all-in-one-pcs.html"
# f="https://www.budgetpc.com.au/computers-servers/branded-computers/pos-sytem.html"
# g="https://www.budgetpc.com.au/computers-servers/branded-computers/thin-client-terminal.html"
# h ="https://www.budgetpc.com.au/computers-servers/branded-computers/barebones.html"
# # i="https://www.budgetpc.com.au/computers-servers/budget-pc-custom-computers.html"
# j="https://www.budgetpc.com.au/computers-servers/budget-pc-custom-computers/mini-ultra-portable-range.html"
# k="https://www.budgetpc.com.au/computers-servers/budget-pc-custom-computers/business-range.html"
# l="https://www.budgetpc.com.au/computers-servers/budget-pc-custom-computers/workstation-range.html"
# # m="https://www.budgetpc.com.au/computers-servers/branded-servers.html"
# n="https://www.budgetpc.com.au/computers-servers/branded-servers/rack-servers.html"
# o="https://www.budgetpc.com.au/computers-servers/branded-servers/tower-servers.html"
# p="https://www.budgetpc.com.au/computers-servers/branded-servers/intel-server-cpu.html"
# q="https://www.budgetpc.com.au/computers-servers/branded-servers/hp-server-cpu.html"
# r="https://www.budgetpc.com.au/computers-servers/branded-servers/lenovo-server-cpu.html"
# s="https://www.budgetpc.com.au/computers-servers/branded-servers/server-storage-devices.html"
# t="https://www.budgetpc.com.au/computers-servers/budget-pc-custom-servers.html"
# # u="https://www.budgetpc.com.au/computers-servers/apple.html"
# v="https://www.budgetpc.com.au/computers-servers/apple/mac.html"
# w="https://www.budgetpc.com.au/computers-servers/apple/mac/mac-mini.html"
# x="https://www.budgetpc.com.au/computers-servers/apple/mac/mac-pro.html"
# z="https://www.budgetpc.com.au/computers-servers/apple/mac/macbook.html"
# A="https://www.budgetpc.com.au/computers-servers/apple/mac/macbook-air.html"
# B="https://www.budgetpc.com.au/computers-servers/apple/mac/macbook-pro.html"
# C="https://www.budgetpc.com.au/computers-servers/apple/mac/imac.html"
# D="https://www.budgetpc.com.au/computers-servers/apple/mac/imac-pro.html"
# E="https://www.budgetpc.com.au/computers-servers/apple/ipad.html"
# J="https://www.budgetpc.com.au/computers-servers/apple/ipad/ipad.html"
# K="https://www.budgetpc.com.au/computers-servers/apple/ipad/ipad-pro.html"
# L="https://www.budgetpc.com.au/computers-servers/apple/ipad/ipad-air.html"
# M="https://www.budgetpc.com.au/computers-servers/apple/ipad/ipad-mini.html"
# N="Ohttps://www.budgetpc.com.au/computers-servers/apple/music.html"
# W="https://www.budgetpc.com.au/computers-servers/apple/music/ipod-touch.html"
# X="https://www.budgetpc.com.au/computers-servers/apple/music/airpods.html"
# Y="https://www.budgetpc.com.au/computers-servers/apple/apple-tv.html"
# Z="https://www.budgetpc.com.au/computers-servers/apple/apple-tv/apple-tv.html"
# aa="https://www.budgetpc.com.au/computers-servers/apple/accessories.html"
# bb="https://www.budgetpc.com.au/computers-servers/apple/accessories/apple-tv-accessories.html"
# cc="https://www.budgetpc.com.au/computers-servers/apple/accessories/cables-docks.html"
# dd="https://www.budgetpc.com.au/computers-servers/apple/accessories/ipad-accessories.html"
# ee="https://www.budgetpc.com.au/computers-servers/apple/accessories/ipad-cover-case.html"
# ff="https://www.budgetpc.com.au/computers-servers/apple/accessories/iphone-accessories.html"
# gg="https://www.budgetpc.com.au/computers-servers/apple/accessories/ipod-accessories.html"
# hh="https://www.budgetpc.com.au/computers-servers/apple/accessories/mac-accessories.html"
# ii="https://www.budgetpc.com.au/computers-servers/apple/accessories/mac-accessories/mac-cover-case.html"
# jj="https://www.budgetpc.com.au/computers-servers/apple/apple-care.html"
# # kk="https://www.budgetpc.com.au/computers-servers/ms-surface.html"
# ll="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-pro-6.html"
# mm="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-laptop-2.html"
# nn="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-studio-2.html"
# oo="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-go-lte.html"
# pp="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-go-commercial.html"
# qq="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-go-education.html"
# rr="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-book-2.html"
# ss="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-pro-lte.html"
# tt="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-pro.html"
# uu="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories.html"
# vv="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-cables-adapters.html"
# ww="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-cover-case.html"
# xx="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-dock.html"
# yy="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-keyboard.html"
# zz="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-mouse.html"
# ab="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-pen.html"
# ac="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-power-supply.html"
# ad="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-type-cover.html"
# ae="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-accessories/surface-other.html"
# af="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty.html"
# ag="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-go-extended-warranty.html"
# ah="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-go-complete-for-business-plus.html"
# ai="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-studio-extended-warranty.html"
# aj="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-laptop-extended-warranty.html"
# ak="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-laptop-complete-for-business-plus.html"
# al="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-book-extended-warranty.html"
# am="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-book-complete-for-business-plus.html"
# an="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-pro-extended-warranty.html"
# ao="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-pro-complete-for-business-plus.html"
# ap="https://www.budgetpc.com.au/computers-servers/ms-surface/surface-extended-warranty/surface-student-extended-warranty.html"

# href = [b,c,d,e,f,g,h,j,k,l,n,o,p,q,r,s,t,v,w,x,z,A,B,C,D,E,K,L,M,N,W,X,Y,Z,aa,bb,cc,dd,ee,ff,gg,hh,ii,
# jj,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap]
# prodUrl = []
# prodList = []



# a = """https://www.budgetpc.com.au/computer-hardware/computer-components.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/cpus-processors/intel-1151-8th-gen-cpu.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/cpus-processors/intel-1151-9th-gen-cpu.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/cpus-processors/intel-socket-2066-cpu.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/cpus-processors/amd-desktop-processors.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/intel-socket-1151-7th-gen.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/intel-socket-1151-8th-gen.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/intel-socket-1151-9th-gen.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/intel-socket-2066.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/amd-socket-am4-2rd-gen.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/amd-socket-am4-3rd-gen.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/amd-socket-tr4.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/motherboards/intel-server-motherboard.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/memory/desktop-ddr4-memory.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/memory/desktop-ddr3-memory-77.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/memory/sodimm-memory.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/memory/server-workstation-memory.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gt-710.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-1030.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-1050-1050-ti.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-1660.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-1060.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-1650.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-1660-ti.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-gtx-2060.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-rtx-2060-super.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-rtx-2070.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-rtx-2070-super.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-rtx-2080.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-rtx-2080ti.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/geforce-rtx-2080-super.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-550.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-560.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-570.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-580.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-590.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-5700.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-rx-5700-xt.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/radeon-vii.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/graphics-cards-workstation.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/video-cards/graphics-cards-accessories.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/aerocool-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/msi-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/bitfenix-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/cooler-master-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/corsair-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/cougar-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/deepcool-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/evga-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/fractal-design-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/gamemax-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/in-win-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/nzxt-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/tgc-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/computer-cases/thermaltake-cases.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/case-mod-led-lights.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/case-accessories.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/aerocool.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/cooler-master.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/corsair.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/evga.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/gamemax.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/sfp.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/silverstone.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/thermaltake.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/power-supplies/fractal-design-power-supplies.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/fans-pc-cooling/cpu-cooling.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/fans-pc-cooling/memory-cooling.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/fans-pc-cooling/vga-cooling.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/fans-pc-cooling/liquid-cooling.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/fans-pc-cooling/cooling-fans.html
# https://www.budgetpc.com.au/computer-hardware/computer-components/fans-pc-cooling/cooling-accessories.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/internal-hard-drives.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/internal-hard-drives/2-5-hard-drive.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/internal-hard-drives/3-5-hard-drive.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/internal-hard-drives/nas-hard-drive.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/internal-hard-drives/hp-server-hard-drive.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/internal-hard-drives/hard-drive-accessories.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/external-hard-drives.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/adata-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/crucial-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/hp-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/intel-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/kingston-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/samsung-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/sandisk-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/seagate-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/gigabyte-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/team-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/ssd-accessories.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/toshiba-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/ssds/west-digital-ssd.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/flash-memory.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/usb-flash-drives.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/optical-drives/internal-optical-drives.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/optical-drives/external-optical-drives.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/optical-drives/media.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/network-attached-storage-nas/desktop-tower-nas.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/network-attached-storage-nas/rackmount-nas.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/network-attached-storage-nas/nas-accessories.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/network-attached-storage-nas/nas-waranties.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/hard-drive-enclosures.html
# https://www.budgetpc.com.au/computer-hardware/storage-devices/hard-drive-docks.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/monitors/below-19-inch-monitors.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/monitors/19-24-inch-monitors.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/monitors/25-27-inch-monitors.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/monitors/28-32-inch-monitors.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/monitors/33-inch-and-above-monitors.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/commercial-display.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/projector-accessories.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mobile-projectors.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/display-accessories.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/digital-performance-eyewear.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/cooler-master-k-m-combo.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/corsair-k-m-combo-77.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/gigabyte-k-m-combo.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/cougar.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/logitech-k-m-combo.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/microsoft-k-m-combo.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/rapoo-k-m-combo.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboard-mouse-combo/tt-esports-k-m-combo.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/asus-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/azio-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/cooler-master-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/corsair-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/cougar-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/gigabyte-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/hp-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/hyperx-keyboard.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/logitech-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/mirrosoft-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/msi-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/rapoo-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/razor-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/roccat-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/steel-series-keyboards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/keyboards/thermaltake-keyboard.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/asus-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/cooler-master-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/corsair-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/cougar-mices.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/gigabyte-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/hp-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/logitech-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/mirrosoft-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/rapoo-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/razor-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/roccat-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/shintaro-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/steel-series-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/thermaltake-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mice/hyperx-mice.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/asus-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/cooler-master-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/corsair-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/gigabyte-mousepad.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/hyperx-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/logitech-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/razor-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/roccat-mousepad.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/steel-series-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/mousepads/thermaltake-mousepads.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/game-devices.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/gaming-chairs.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/speakers/altec-lansing-speaker.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/speakers/creative-speaker.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/speakers/jabra-speaker.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/speakers/logitech-speaker.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/speakers/razer-speaker.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/speakers/edifier-speaker.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/asus-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/cooler-master-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/corsair-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/cougar-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/creative-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/jabra-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/kingston-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/logitech-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/microsoft-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/msi-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/plantronics-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/razer-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/roccat-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/shintaro-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/steel-series-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/thermaltake-headset.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headsets/creative-headset-77.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/headset-holders.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/web-cams.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/tv-tuner-capture.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/kvms.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/kvm-accessories.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/ups/desktop-ups.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/ups/tower-ups.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/ups/rackmount-ups.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/ups/ups-batteries.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/ups/ups-accessories.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/surge-protector-power-boards.html
# https://www.budgetpc.com.au/computer-hardware/peripherals/pdu.html
# https://www.budgetpc.com.au/computer-hardware/printing/3d-printing.html
# https://www.budgetpc.com.au/computer-hardware/printing/3d-printing/3d-printer.html
# https://www.budgetpc.com.au/computer-hardware/printing/3d-printing/3d-consumable-parts.html
# https://www.budgetpc.com.au/computer-hardware/printing/inkjet-printing/inkjet-a3-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/inkjet-printing/inkjet-a4-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/inkjet-printing/inkjet-multifunction-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/laser-printing.html
# https://www.budgetpc.com.au/computer-hardware/printing/laser-printing/mono-laser-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/laser-printing/mono-laser-multi-function-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/laser-printing/color-laser-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/laser-printing/colour-laser-multi-function-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/large-format-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/portable-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/fax-machines.html
# https://www.budgetpc.com.au/computer-hardware/printing/scanners/a3-scanners.html
# https://www.budgetpc.com.au/computer-hardware/printing/scanners/a4-scanners.html
# https://www.budgetpc.com.au/computer-hardware/printing/scanners/portable-scanners.html
# https://www.budgetpc.com.au/computer-hardware/printing/scanners/scanner-accessories.html
# https://www.budgetpc.com.au/computer-hardware/printing/scanners/scanner-warranties.html
# https://www.budgetpc.com.au/computer-hardware/printing/toners-genuine.html
# https://www.budgetpc.com.au/computer-hardware/printing/ink-cartridges.html
# https://www.budgetpc.com.au/computer-hardware/printing/dot-matrix-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/label-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/papers-cards-labels.html
# https://www.budgetpc.com.au/computer-hardware/printing/point-of-sale/barcode-scanners.html
# https://www.budgetpc.com.au/computer-hardware/printing/point-of-sale/thermal-printers.html
# https://www.budgetpc.com.au/computer-hardware/printing/point-of-sale/thermal-printers-consumables.html
# https://www.budgetpc.com.au/computer-hardware/printing/point-of-sale/pos-accessories.html
# https://www.budgetpc.com.au/computer-hardware/printing/printer-warranties.html
# https://www.budgetpc.com.au/computer-hardware/accessories/add-on-cards.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/apple-adapters.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/vga.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/video-splitters.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/video-extenders.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/dvi.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/hdmi.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/display-port.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/usb.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/power.html
# https://www.budgetpc.com.au/computer-hardware/accessories/adapters-converters/serial-parallel.html
# https://www.budgetpc.com.au/computer-hardware/accessories/batteries.html
# https://www.budgetpc.com.au/computer-hardware/accessories/card-readers.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/audio.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/dvi.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/vga.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/hdmi.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/display-port.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/parallel.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/serial.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/power.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/sata-esata.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/ide.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/firewire.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/network.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/kvm.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/usb.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/rca.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable/lc-lc-om1-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable/lc-sc-om1-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable/lc-st-om1-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable/sc-sc-om1-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable/sc-st-om1-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om1-multi-mode-duplex-fibre-cable/st-st-om1-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om3-multi-mode-duplex-fibre-cable.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om3-multi-mode-duplex-fibre-cable/lc-lc-om3-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om3-multi-mode-duplex-fibre-cable/lc-sc-om3-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om3-multi-mode-duplex-fibre-cable/lc-st-om3-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om3-multi-mode-duplex-fibre-cable/sc-sc-om3-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om3-multi-mode-duplex-fibre-cable/st-st-om3-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om4-multi-mode-duplex-fibre-cable.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om4-multi-mode-duplex-fibre-cable/lc-lc-om4-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om4-multi-mode-duplex-fibre-cable/lc-sc-om4-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om4-multi-mode-duplex-fibre-cable/lc-st-om4-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om4-multi-mode-duplex-fibre-cable/sc-sc-om4-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/om4-multi-mode-duplex-fibre-cable/st-st-om4-multimode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable/lc-lc-os1-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable/lc-sc-os1-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable/lc-st-os1-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable/sc-sc-os1-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable/sc-st-os1-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os1-single-mode-duplex-fibre-cable/st-st-os1-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable/lc-lc-os2-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable/lc-sc-os2-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable/lc-st-os2-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable/sc-sc-os2-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable/sc-st-os2-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fiber-optic/os2-single-mode-duplex-fibre-cable/st-st-os2-singlemode-duplex.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fibre-pigtails/multimode-om1.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fibre-pigtails/multimode-om3.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fibre-pigtails/multimode-om4.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fibre-pigtails/singlemode-os1.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/fibre-pigtails/singlemode-os1-77.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/scsi-sas.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/sfp-sfp-qsfp-qsfp-cables.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cables/thunderbolt-cables.html
# https://www.budgetpc.com.au/computer-hardware/accessories/cable-management.html
# https://www.budgetpc.com.au/computer-hardware/accessories/hubs.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-torch.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-lights/accessories.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-lights/commercial-lighting.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-lights/downlight-kits.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-lights/globes.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-lights/lamps.html
# https://www.budgetpc.com.au/computer-hardware/accessories/led-lights/spotlights.html
# https://www.budgetpc.com.au/computer-hardware/accessories/video-capture-hardware.html
# https://www.budgetpc.com.au/computer-hardware/accessories/test-measure.html
# https://www.budgetpc.com.au/computer-hardware/accessories/phone-accessories.html
# https://www.budgetpc.com.au/computer-hardware/accessories/server-racks.html
# https://www.budgetpc.com.au/computer-hardware/accessories/server-racks/cabinets-accessories.html """ 


a = """https://www.budgetpc.com.au/networking/network-hardware.html
https://www.budgetpc.com.au/networking/network-hardware/modems.html
https://www.budgetpc.com.au/networking/network-hardware/routers.html
https://www.budgetpc.com.au/networking/network-hardware/switches.html
https://www.budgetpc.com.au/networking/network-hardware/switches/poe-switches.html
https://www.budgetpc.com.au/networking/network-hardware/switches/non-poe-switches.html
https://www.budgetpc.com.au/networking/network-hardware/firewalls.html
https://www.budgetpc.com.au/networking/network-hardware/antennas.html
https://www.budgetpc.com.au/networking/wireless.html
https://www.budgetpc.com.au/networking/wireless/bluetooth.html
https://www.budgetpc.com.au/networking/wireless/wireless-adapters.html
https://www.budgetpc.com.au/networking/wireless/range-extenders.html
https://www.budgetpc.com.au/networking/wireless/access-points.html
https://www.budgetpc.com.au/networking/network-brands.html
https://www.budgetpc.com.au/networking/network-brands/tycon-power.html
https://www.budgetpc.com.au/networking/network-brands/rf-armor.html
https://www.budgetpc.com.au/networking/network-brands/openmesh.html
https://www.budgetpc.com.au/networking/network-brands/mikrotik-router-ap-sfp.html
https://www.budgetpc.com.au/networking/network-adapters-converters.html
https://www.budgetpc.com.au/networking/network-adapters-converters/powerline-adapters-kits.html
https://www.budgetpc.com.au/networking/network-adapters-converters/ethernet-adapters.html
https://www.budgetpc.com.au/networking/network-adapters-converters/fibre-media-converters.html
https://www.budgetpc.com.au/networking/network-adapters-converters/poe-injectors-splitters-extenders.html
https://www.budgetpc.com.au/networking/ip-camera-surveillance.html
https://www.budgetpc.com.au/networking/ip-camera-surveillance/surveillance-ip-recorders.html
https://www.budgetpc.com.au/networking/ip-camera-surveillance/ip-network-cameras.html
https://www.budgetpc.com.au/networking/ip-camera-surveillance/ip-camera-accessories.html
https://www.budgetpc.com.au/networking/voip-and-phone.html
https://www.budgetpc.com.au/networking/server-accessories.html
https://www.budgetpc.com.au/networking/server-accessories/server-cabinets.html
https://www.budgetpc.com.au/networking/server-accessories/server-blanking-panels.html
https://www.budgetpc.com.au/networking/server-accessories/vertical-cable-pdu-trays.html
https://www.budgetpc.com.au/networking/server-accessories/server-lacing-bars.html
https://www.budgetpc.com.au/networking/server-accessories/server-cabinet-shelves.html
https://www.budgetpc.com.au/networking/server-accessories/server-cable-management-rails.html
https://www.budgetpc.com.au/networking/server-accessories/patch-panels.html
https://www.budgetpc.com.au/networking/server-accessories/printer-servers.html
https://www.budgetpc.com.au/networking/huawei.html
https://www.budgetpc.com.au/networking/huawei/huawei-firewall.html
https://www.budgetpc.com.au/networking/huawei/huawei-mobile-phone-accessory.html
https://www.budgetpc.com.au/networking/huawei/huawei-nas.html
https://www.budgetpc.com.au/networking/huawei/huawei-modem.html
https://www.budgetpc.com.au/networking/huawei/huawei-router.html
https://www.budgetpc.com.au/networking/huawei/huawei-switch.html
https://www.budgetpc.com.au/networking/huawei/huawei-notebook.html
https://www.budgetpc.com.au/networking/huawei/huawei-notebook-accessory.html
https://www.budgetpc.com.au/networking/huawei/huawei-servers.html
https://www.budgetpc.com.au/networking/huawei/huawei-wearable-electonics.html
https://www.budgetpc.com.au/networking/ubiquiti.html
https://www.budgetpc.com.au/networking/ubiquiti/airfiber.html
https://www.budgetpc.com.au/networking/ubiquiti/airmax.html
https://www.budgetpc.com.au/networking/ubiquiti/airmax/airgateway.html
https://www.budgetpc.com.au/networking/ubiquiti/airmax/airmax-ac.html
https://www.budgetpc.com.au/networking/ubiquiti/airmax/airmax-aetennas.html
https://www.budgetpc.com.au/networking/ubiquiti/airmax/airrouter.html
https://www.budgetpc.com.au/networking/ubiquiti/edgemax.html
https://www.budgetpc.com.au/networking/ubiquiti/edgemax/edgerouter.html
https://www.budgetpc.com.au/networking/ubiquiti/edgemax/edgeswitch.html
https://www.budgetpc.com.au/networking/ubiquiti/edgemax/edgepoint.html
https://www.budgetpc.com.au/networking/ubiquiti/mfi.html
https://www.budgetpc.com.au/networking/ubiquiti/unifi.html
https://www.budgetpc.com.au/networking/ubiquiti/unifi-switch.html
https://www.budgetpc.com.au/networking/ubiquiti/unifi-voip.html
https://www.budgetpc.com.au/networking/ubiquiti/unifi-video.html
https://www.budgetpc.com.au/networking/ubiquiti/accessories.html
https://www.budgetpc.com.au/networking/ubiquiti/accessories/toughcable.html
https://www.budgetpc.com.au/networking/ubiquiti/accessories/toughswitch.html
https://www.budgetpc.com.au/networking/ubiquiti/amplifi.html
https://www.budgetpc.com.au/networking/cisco.html
https://www.budgetpc.com.au/networking/cisco/wireless.html
https://www.budgetpc.com.au/networking/cisco/wireless/ap-ac-wap.html
https://www.budgetpc.com.au/networking/cisco/wireless/wireless-router.html
https://www.budgetpc.com.au/networking/cisco/wireless/wireless-controller.html
https://www.budgetpc.com.au/networking/cisco/switches-77.html
https://www.budgetpc.com.au/networking/cisco/switches-77/poe-switch.html
https://www.budgetpc.com.au/networking/cisco/switches-77/smart-switch.html
https://www.budgetpc.com.au/networking/cisco/switches-77/unmanaged-switch.html
https://www.budgetpc.com.au/networking/cisco/routers-77.html
https://www.budgetpc.com.au/networking/cisco/routers-77/morden-router.html
https://www.budgetpc.com.au/networking/cisco/routers-77/wan-router.html
https://www.budgetpc.com.au/networking/cisco/routers-77/security-enabled-router.html
https://www.budgetpc.com.au/networking/cisco/security.html
https://www.budgetpc.com.au/networking/cisco/security/firewall.html
https://www.budgetpc.com.au/networking/cisco/security/ip-cameras.html
https://www.budgetpc.com.au/networking/cisco/voice.html
https://www.budgetpc.com.au/networking/cisco/voice/ip-phone.html
https://www.budgetpc.com.au/networking/cisco/voice/video-enabled.html
https://www.budgetpc.com.au/networking/grandstream.html
https://www.budgetpc.com.au/networking/grandstream/ata.html
https://www.budgetpc.com.au/networking/grandstream/gateways.html
https://www.budgetpc.com.au/networking/grandstream/grandstream-ip-pbx.html
https://www.budgetpc.com.au/networking/grandstream/grandstream-dect-ip-phones.html
https://www.budgetpc.com.au/networking/grandstream/grandstream-hd-ip-phones.html
https://www.budgetpc.com.au/networking/grandstream/grandstream-ip-video-multimedia-phones.html
https://www.budgetpc.com.au/networking/grandstream/ipsurveillance.html
https://www.budgetpc.com.au/networking/grandstream/ipvideoconferencing.html
https://www.budgetpc.com.au/networking/grandstream/ipphoneaccessories.html
https://www.budgetpc.com.au/networking/cambium.html
https://www.budgetpc.com.au/networking/cambium/cambium-cnpilot.html
https://www.budgetpc.com.au/networking/cambium/cambium-epmp.html
https://www.budgetpc.com.au/networking/cambium/cambium-waranties.html
https://www.budgetpc.com.au/networking/cambium/cambium-accessories.html """

a = a.replace("\n",",")
href =[]
for i in range((a.count(","))+1):
    holder = a.split(",")[i]
    href.append(holder)




count = 0
for i in range(len(href)):
    holder = href[i]
    # txtTitle =holder.rsplit("/",1)[1]
    # txtTitle = txtTitle.replace(".html","")
    
    holdertwo = bc(holder).main()
    if holdertwo is not None:
        print("in not none")
        count = count+len(holdertwo)
        print(count)
        # prodUrl.extend(holdertwo)
        for i in range(len(holdertwo)):
            row = holdertwo[i]
            file1 = open("BudgetPc_networking.txt","a")    
            file1.write( row+",\n") 
            file1.close() 
            # 
            # time.sleep(1)


            # holderThree = bd(levelOne,levelTwo,holdertwo[i]).main()
            # if os.path.exists('budgetPc.csv') is False:
            #     row = ['Category', 'Sub Category', 'Product','Description','Price','Product Image','Product Url','Configuration']
    
            #     with open('budgetPc.csv', 'a') as csvFile:
            #         writer = csv.writer(csvFile)
            #         writer.writerow(row)
            #     csvFile.close()

            
            # row = holderThree
        
            # with open('budgetPc.csv', 'a') as csvFile:
            #     writer = csv.writer(csvFile)
            #     writer.writerow(row)
            # csvFile.close()

            # # prodList.append(holderThree)
            # print(row)
            # # time.sleep(0.2)

print("Final Product list count:", count)
# refubrished 805
# computer & service 1425
# netbooks-tablet 971

# print(href[0])