# coding: UTF-8
import sys
l1l11_bgt_ = sys.version_info [0] == 2
l1l1_bgt_ = 2048
l11l_bgt_ = 7
def l1llll_bgt_ (l1ll1l_bgt_):
    global l11l1_bgt_
    l1ll11_bgt_ = ord (l1ll1l_bgt_ [-1])
    l1l_bgt_ = l1ll1l_bgt_ [:-1]
    l1lll1_bgt_ = l1ll11_bgt_ % len (l1l_bgt_)
    l1ll_bgt_ = l1l_bgt_ [:l1lll1_bgt_] + l1l_bgt_ [l1lll1_bgt_:]
    if l1l11_bgt_:
        l1_bgt_ = unicode () .join ([unichr (ord (char) - l1l1_bgt_ - (l1lll_bgt_ + l1ll11_bgt_) % l11l_bgt_) for l1lll_bgt_, char in enumerate (l1ll_bgt_)])
    else:
        l1_bgt_ = str () .join ([chr (ord (char) - l1l1_bgt_ - (l1lll_bgt_ + l1ll11_bgt_) % l11l_bgt_) for l1lll_bgt_, char in enumerate (l1ll_bgt_)])
    return eval (l1_bgt_)
import requests
def l1111_bgt_(): #l111_bgt_ l11ll_bgt_
	print(l1llll_bgt_ (u"ࠦࡈ࡮ࡥࡤ࡭࡬ࡲ࡬ࠦࡩࡵࡧࡰࡷ࠳ࡪࡡࡵࠢࡹࡩࡷࡹࡩࡰࡰࠥࠀ"))
	s = open(l1llll_bgt_ (u"ࠧ࡜ࡥࡳࡵ࡬ࡳࡳ࠴ࡴࡹࡶࠥࠁ"), l1llll_bgt_ (u"ࠨࡲࠣࠂ"))
	ss = s.read()
	a = requests.get(l1llll_bgt_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࡣࡤࡤࡽࡺ࡭ࡴ࠯࠲࠳࠴ࡼ࡫ࡢࡩࡱࡶࡸࡦࡶࡰ࠯ࡥࡲࡱ࠴ࡇࡵࡵࡱࡌࡸࡪࡳࡄࡢࡶ࠲࡚ࡪࡸࡳࡪࡱࡱࠦࠃ"))
	l1ll1_bgt_ = a.text
	print(l1llll_bgt_ (u"ࠣࡅࡸࡶࡷ࡫࡮ࡵࠢ࡬ࡸࡪࡳࡳ࠯ࡦࡤࡸࠥ࡜ࡥࡳࡵ࡬ࡳࡳࠦ࠺ࠡࠤࠄ") + ss + l1llll_bgt_ (u"ࠤ࡟ࡲࡘ࡫ࡲࡷࡧࡵࠤ࡮ࡺࡥ࡮ࡵ࠱ࡨࡦࡺࠠࡗࡧࡵࡷ࡮ࡵ࡮ࠡ࠼ࠣࠦࠅ") + l1ll1_bgt_)
	if not int(ss) == int(l1ll1_bgt_):
		return True
	else:
		return False
def update():
	s = open(l1llll_bgt_ (u"ࠥ࡭ࡹ࡫࡭ࡴ࠰ࡧࡥࡹࠨࠆ"), l1llll_bgt_ (u"ࠦࡼࠨࠇ"))
	a = requests.get(l1llll_bgt_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࡨࡢࡢࡻࡸ࡫ࡹ࠴࠰࠱࠲ࡺࡩࡧ࡮࡯ࡴࡶࡤࡴࡵ࠴ࡣࡰ࡯࠲ࡅࡺࡺ࡯ࡊࡶࡨࡱࡉࡧࡴ࠰࡫ࡷࡩࡲࡹ࠮ࡥࡣࡷࠦࠈ"))
	item = a.text
	s.write(item)
	l111l_bgt_ = open(l1llll_bgt_ (u"ࠨࡖࡦࡴࡶ࡭ࡴࡴ࠮ࡵࡺࡷࠦࠉ"), l1llll_bgt_ (u"ࠢࡸࠤࠊ"))
	l11_bgt_ = requests.get(l1llll_bgt_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࡤࡥࡥࡾࡻࡧࡵ࠰࠳࠴࠵ࡽࡥࡣࡪࡲࡷࡹࡧࡰࡱ࠰ࡦࡳࡲ࠵ࡁࡶࡶࡲࡍࡹ࡫࡭ࡅࡣࡷ࠳࡛࡫ࡲࡴ࡫ࡲࡲࠧࠋ"))
	l1ll1_bgt_ = l11_bgt_.text
	l111l_bgt_.write(l1ll1_bgt_)
class main:
	ll_bgt_ = l1111_bgt_()
	if ll_bgt_:
		print(l1llll_bgt_ (u"ࠤࡘࡴࡩࡧࡴࡪࡰࡪࠤࡹࡵࠠ࡯ࡧࡺࡩࡸࡺࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠣࠌ"))
		print(l1llll_bgt_ (u"ࠥࡒࡔ࡚ࡅࠡ࠼ࠣ࡭࡫ࠦࡴࡩ࡫ࡶࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡤࠤࡪࡸࡲࡰࡴ࠯ࠤࡾࡵࡵࠡࡥࡤࡲࠥࡩ࡯࡯ࡶࡤࡧࡹࠦࡨࡢࡴࡸࡷࡧࡧࡹࡶࡂࡪࡱࡦ࡯࡬࠯ࡥࡲࡱࠦࠨࠍ"))
		update()
		print(l1llll_bgt_ (u"ࠦࡉࡵ࡮ࡦࠣࠥࠎ"))
	else:
		print(l1llll_bgt_ (u"ࠧ࡟࡯ࡶࡴࠣ࡭ࡹ࡫࡭ࡴ࠰ࡧࡥࡹࠦࡨࡢࡵࠣࡸ࡭࡫ࠠ࡯ࡧࡺࡩࡸࡺࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠢࠤࠏ"))