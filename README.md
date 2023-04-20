# IoT-Home-assistant-Line-chat-bot-Via-speech-recognition

  【IoT-Home-assistant-Line-chat-bot-Via-speech-recognition(物聯網語音辨識居家Line Chat Bot)】，是一個由Line Chat Bot結合物聯網想要做到可以用語音控制的智慧居家系統。是因為有一些情況之下可能不方便用手去操控或開關東西，所以想藉由語音就可以達到一些簡單的智慧居家控制，在本專題中也成功的實驗藉由Line輸入語音訊息就可以控制電燈、冷氣、電子鎖…等物件的控制。

  簡單的說明是，先把Line上的語音訊息轉成字串，再就由NLP把字串的語意進行拆解，找到關鍵字的字詞，再去雲端資料庫中將關鍵字的字詞依照需求去做改變，本地的智慧居家依據資料庫的改變即可完成相關命令的改變。例如: 語音輸入Turn on the light，NLP將其拆開為Turn on 、 light，雲端資料庫中的light項目就會改成true，而電燈在抓取資料庫的時候就會將其改成亮燈的狀態。


Demo Video:
[![IMAGE ALT TEXT](http://img.youtube.com/vi/oalzh-NQI7Q/0.jpg)](https://www.youtube.com/watch?v=oalzh-NQI7Q "IoT-Home-assistant-Line-chat-bot-Via-speech-recognition Demo Video")
