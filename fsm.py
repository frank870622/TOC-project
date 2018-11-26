from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_simon(self, event):
        if event.get("message"):
            text = event['message']['text']
            return 'simon' in text.lower()
        return False

    def is_going_to_food(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '食用系少女' in text.lower()
        return False

    def is_going_to_bubble(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '小圓' in text.lower()
        return False

    def is_going_to_chicken(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '小光' in text.lower()
        return False

    def is_going_to_loser(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '小滷' in text.lower()
        return False

    def is_going_to_dragon(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '龍兒' in text.lower()
        return False

    def is_going_to_ice(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '果果' in text.lower()
        return False

    def is_going_to_ipass(self, event):
        if event.get("message"):
            text = event['message']['text']
            return 'ipass' in text.lower()
        return False

    def is_going_to_smallpa(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '小帕' in text.lower()
        return False

    def is_going_to_P(self, event):
        if event.get("message"):
            text = event['message']['text']
            return 'p' in text.lower()
        return False

    def is_going_to_elfair(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '艾兒' in text.lower()
        return False

    def is_going_to_3boss(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '屏東三巨頭' in text.lower()
        return False

    def is_going_to_air(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '艾兒' in text.lower() or '空氣少女' in text.lower()
        return False

    def is_going_to_magi(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '小瑪' in text.lower() or '迷路小瑪在萬金' in text.lower()
        return False

    def is_going_to_sakura(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '絢櫻' in text.lower() or '初夏的東港之櫻' in text.lower()
        return False

    def is_going_to_rice(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '東津萌米' in text.lower() or '穗姬' in text.lower()
        return False

    def is_going_to_child(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '秧苗' in text.lower()
        return False

    def is_going_to_sister(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '結穗' in text.lower()
        return False

    def is_going_to_whiterice(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '白米' in text.lower() or '穗姬' in text.lower()
        return False

    def is_going_to_mrt(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '高捷' in text.lower()
        return False

    def is_going_to_sora(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '小穹' in text.lower()
        return False

    def is_going_to_emilia(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '艾米' in text.lower() or '莉亞' in text.lower()
        return False

    def is_going_to_jay(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '婕兒' in text.lower()
        return False

    def is_going_to_nana(self, event):
        if event.get("message"):
            text = event['message']['text']
            return 'nana' in text.lower() or '耐耐' in text.lower()
        return False

    def on_enter_simon(self, event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"希萌創意\nhttp://simon.moe/")
        responese = send_text_message(sender_id, "Simon，希萌創意\r\n關於希萌的一些作品們\r輸入 食用系少女 魔法少女ipass 屏東三巨頭 前進吧！！高捷少女\n輸入 simon 來回到這個頁面")

    def on_enter_food(self, event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"食用系少女\nhttp://simon.moe/youcaneatthegirl/")
        send_text_message(sender_id, "若是沒有在一百天通過評鑑\n小吃街就要遭到收購？！\n\n東漢《論衡》：「物之老者，其精為人。」， \n日本亦有工具經百年成為「付喪神」的傳說。 \n然而歷史悠久的小吃名店則是…… \n玩家做為行銷公司的顧問，接手了地方小吃街的推廣案。 \n發現曾經風光的小吃街門可羅雀，更面臨收購的危機！ \n必須設法和小吃街的少女們一起努力，在三個月內通過評鑑， \n避免倒閉的危機！ \n然而少女們卻有著不為人知的祕密……\n\n拯救小吃街的經營故事即展開！\n\n角色介紹輸入: 小圓 小光 小滷 龍兒 果果")
    
    def on_enter_bubble(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/qy8ZrEo.jpg")

    def on_enter_chichen(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/KQ5LuZi.jpg")

    def on_enter_loser(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/qLnnVCj.jpg")

    def on_enter_dragon(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/8MiiVd5.jpg")

    def on_enter_ice(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/cXyCwJV.jpg")

    def on_enter_ipass(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"魔法少女ipass\nhttps://www.i-pass.com.tw/IPS/Event/Mgi/index.html")
        send_text_message(sender_id, "台灣路上隨處可見的女子高中生卻因為小P的出現\n\n捲入了魔法少女與油電雙漲、物價通膨的戰爭(?)。\n\n角色介紹輸入: 小帕 小P 艾兒")
    
    def on_enter_smallpa(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://simon.moe/project/images/ipass/01.jpg")

    def on_enter_P(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://simon.moe/project/images/ipass/02.jpg")

    def on_enter_elfair(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://simon.moe/project/images/ipass/03.jpg")

    def on_enter_3boss(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/nNSTF8L.jpg")
        send_text_message(sender_id, "這裡有「空氣少女注意報」、「迷路小瑪在萬金」以及「初夏的東港之櫻」、「東津萌米」\n你問好像有四個?\n三巨頭有四個人是很正常的啦～\n輸入各個名字看詳細窩～")
    
    def on_enter_air(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"空氣少女注意報\nhttps://www.facebook.com/273597940165501/photos/a.273602300165065/273600903498538/?type=3")
        send_image_message(sender_id, "http://simon.moe/project/images/air/01.jpg")
        send_text_message(sender_id,"Rinascimento，意思是義大利文的文藝復興 \n 在這裡，艾兒將重新出發，與眾人一同譜出空氣少女的全新故事。")

    def on_enter_magi(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"迷路小瑪在萬金\nhttps://zh-tw.facebook.com/MAGI.in.Wanchin.Basilica/")
        send_image_message(sender_id, "http://simon.moe/project/images/magi/01.jpg")
        send_text_message(sender_id,"喜愛著美麗的萬金聖母聖殿與在地獨特的人文氣息\n 希望能和大家在玫瑰小鎮-萬金度過一個不一樣的聖誕節。")

    def on_enter_sakura(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"初夏的東港之櫻\nhttps://zh-tw.facebook.com/sergestid.shrimp/")
        send_image_message(sender_id, "http://simon.moe/project/images/shrimp/01.jpg")
        send_text_message(sender_id,"於蔚藍海水中舞躍的櫻花蝦\n在初夏的東港靜靜地等待您的到來。")

    def on_enter_rice(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"東津萌米\nhttp://simon.moe/rice/")
        send_image_message(sender_id, "http://simon.moe/project/images/rice/banner.jpg")
        send_text_message(sender_id,"「穗姬」意指此品種稻米猶如白米中的公主般，品種優良、米粒晶亮且口感絕佳。\n詳細搜尋: 秧苗 結穗 白米")

    def on_enter_child(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://simon.moe/project/images/rice/01.jpg")

    def on_enter_sister(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://simon.moe/project/images/rice/02.jpg")

    def on_enter_whiterice(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://simon.moe/project/images/rice/03.jpg")

    def on_enter_mrt(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"前進吧！高捷少女《進め！高捷（たかめ）少女！》\nhttps://www.facebook.com/K.R.T.GIRLS/")
        send_text_message(sender_id, "K.R.T.GIRLS\n這是一個關於在高捷服務的少女們\n與來往的旅客所共譜出的日常物語\n角色詳細輸入: 小穹 艾米莉亞 婕兒 耐耐")

    def on_enter_sora(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://simon.moe/project/images/krt/01.jpg")

    def on_enter_emilia(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://simon.moe/project/images/krt/02.jpg")

    def on_enter_jay(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://simon.moe/project/images/krt/03.jpg")

    def on_enter_nana(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://simon.moe/project/images/krt/04.jpg")

