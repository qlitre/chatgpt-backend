from typing import Tuple


def get_mock_response() -> str:
    """
    トークンを消費せずに、仮のベタ打ちのメッセージを返す。
    """
    return """
            カネコアヤノ（Kaneko Ayano）は、日本のシンガーソングライターです。彼女は以下のような特徴や経歴を持っています：
            デビュー: カネコアヤノは、2010年代初頭に音楽活動を開始し、その独自の歌詞やメロディーで注目を集めました。
            音楽スタイル: 彼女の楽曲は、日常の風景や感情を繊細に描写した歌詞と、シンプルながらも印象的なメロディーで知られています。アコースティックギターを中心としたアレンジが多いです。
            作品: カネコアヤノは、数多くのアルバムやシングルをリリースしています。その中でも、彼女の作品は多くのリスナーから愛されており、その音楽性や歌詞の世界観が高く評価されています。
            ライブ活動: 彼女は、日本国内を中心にライブ活動を展開しており、その熱量あるライブパフォーマンスも魅力の一つです。
            カネコアヤノは、その独特の声や歌詞の世界観、感受性豊かなメロディーで多くのファンに支持されています。彼女の楽曲は、多くの人々の心に寄り添い、共感を呼び起こすものとなっています。
            """


def get_mock_topic_and_response() -> Tuple[str, str]:
    """
    トークンを消費せずに、仮のベタ打ちのメッセージとトピックを返す。
    """
    ai_res = """
            柴田聡子は、1986年12月11日に北海道札幌市で生まれた日本のミュージシャン、詩人です。
            彼女は武蔵野美術大学と東京藝術大学で学び、2010年から音楽活動を本格化させました。
            2012年にデビューアルバム『しばたさとこ島』をリリースし、2014年にはレコード会社P-VINEに移籍し、2ndアルバム『いじわる全集』をリリースしました。
            詩の才能も持ち合わせており、2016年に詩集『さばーく』を発表し、エルスール財団新人賞・現代詩部門を受賞しました。
            2017年には4thアルバム『愛の休日 DO YOU NEED A REST FROM LOVE?』をリリースし、オリコンアルバムチャートで71位にランクインしました。
            このアルバムには山本精一、岸田繁など多くの著名なアーティストが参加しています。
            """
    # topicもGPTにやらせる
    # この文章のトピックを20文字以内で書いて。他に余計な情報は載せずトピックだけ書いて返して。
    topic = "柴田聡子の音楽と詩の経歴"
    return ai_res, topic
