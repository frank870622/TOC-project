# TOC-project
<p> 此 bot 為程式學習用
<p> BOT步驟
<p> 首先隨便打個東西，BOT就會進到simon state 會印出提示你輸入的東西 然後就照著提示輸入 就醬
<p> 不管在任何state 都可以輸入 "simon" 來回到主state（simon）
<p> 傳送圖片會比較慢一點
<p> feature: heroku deploy & send image & a lot of state
<img src=https://github.com/frank870622/TOC-project/blob/master/fsm.png>
<p> 初始state(user) with (任何input)-> 主state(simon)
<p> 主state(simon) with　(食用系少女 || 魔法少女ipass ||　屏東三巨頭 || 前進吧！！高捷少女) -> 食用系少女 || 魔法少女ipass ||　屏東三巨頭 || 前進吧！！高捷少女
<p> 食用系少女 with (小圓 || 小光 || 小滷 || 龍兒 || 果果) -> state of (小圓 || 小光 || 小滷 || 龍兒 || 果果) with image
<p> 魔法少女ipass with (小帕 ||小P || 艾兒(elf))　-> state of (小帕 ||小P || 艾兒(elf)) with image
<p> 屏東三巨頭 with (空氣少女注意報 || 迷路小瑪在萬金 || 初夏的東港之櫻 || 東津萌米) -> (空氣少女注意報 || 迷路小瑪在萬金 || 初夏的東港之櫻 || 東津萌米)
<p> 東津萌米 with (秧苗 || 結穗 || 白米) ->　(秧苗 || 結穗 || 白米)　with image
<p> 高捷少女 with (小穹 || 艾米莉亞 || 婕兒 || 耐耐) ->　(小穹 || 艾米莉亞 || 婕兒 || 耐耐)　with image 
<p> any state with simon -> 主state(simon)
  
  
  
