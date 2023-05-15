from pyknp import KNP

def ne_knp(text):
    f = open('test.txt','a')
    knp = KNP()
    text = text.replace(' ', '')
    result = knp.parse(text)
    f.write(text + "\n")
    f.write("固有表現抽出結果：\n")

    for tag in result.tag_list():
        for word in tag.mrph_list():
            ne_anotation = word.fstring
            if "固有キー" in ne_anotation:
                f.write(word.genkei + "\n")
    f.write("------------------------\n")

ne_knp("維新は次期衆院選で、立憲民主党から野党第1党の座を奪取することを目指す。馬場氏は党大会で「ここからは非常に厳しい上り坂になってくる。目標がクリアされれば、今までにない国会の議論を国民に見ていただける」と語り、党内の結束を呼び掛けた。")
ne_knp("徳島の夏の阿波踊りは、祭りか、興行か――。県内で最も盛り上がる徳島市の阿波踊りで今夏、有料演舞場に過去最高額の1万5000円の観覧指定席が新設される。新型コロナウイルスの感染症法上の5類移行を受け、主催者は人出が戻ると見込んで強気の価格設定にかじを切った。興行化に拍車がかかる現状を、地元の人たちはどう見ているのか。")
ne_knp("「徳島の人にとって、阿波踊りは地域の祭りという意識が強い。町内会ごとに受け継がれてきた本来の踊りの意義が薄れてきている」。危機感をあらわにするのは「本家大名連」の清水理（さとる）連長（75）＝同市＝だ。清水さんは「男踊り」の踊り手歴50年。「近所の顔見知りが飛び入りで一緒に踊ってくれるのがうれしい。『踊る阿呆に見る阿呆』と言って、踊り手と観客が一体となることに意味がある」と強調。「高額チケットを地元の人が買うわけがない。県外の観光客に見せるだけの興行路線を突き進んでいる」と批判する。")
ne_knp("中でも、男性用の「メンズカット」を受ける女性客の増加は顕著だ。その主流の年代は、中高生からまもなく就職する若い世代の女性まで。メンズカットを施術した女性客のビフォーアフターをSNSで配信している美容室「LIPPS hair（リップスヘアー）」のデザイナー（スタイリスト）、石井里奈さんも「驚いている」と語る。いったいメンズ美容室で何が起きているのか？")
ne_knp("石井さんの在籍するLIPPS hairは、1999年オープンと、メンズサロンの源流の1つともいわれている美容室だ。彼女自身もメンズカットの技術に長けたデザイナーである。逆転現象が始まったのは2021年、当時注目され始めたInstagramのリールに、長く担当している女性客の動画を投稿してみたところ「バズった」という。")
ne_knp("今季限りでドイツ1部Eフランクフルトを退団することが決定している日本代表MF鎌田大地（26）が、年俸300万ユーロ（約4億4100万円）でACミランと基本合意に達したとイタリアのサッカー専門サイト「カルチョメルカート・コム」が13日に報じた。")
ne_knp("同サイトによれば、強化最高責任者であるフェデリコ・マッサラ氏（54）、クラブのレジェンドでもある元イタリア代表DFパオロ・マルディーニ氏（54）が、鎌田を高く評価。契約満了で移籍金が発生しないこともあり、資金面でも障害がないと報じている。")
ne_knp("コロナ禍で世界的に不安定な情勢の中で、日本から世界への扉を開き続けたのが丸亀製麺です。2021年7月には、英国ロンドンに1号店をオープンし、欧州展開の本格化を発表。同年の英国の飲食メディア『Big Hospitality』のトレンドトップ10にランクインし、「うどんは必ず英国に根づく」と絶賛されました。")
ne_knp("ヴァーチャルシンガーの初音ミクと“結婚”した男性がいます。「母と妹に理解してもらえなかった」と言いますが、なぜ結婚したのか?どんな結婚生活なのか?こうしたフィクションのキャラクターに恋愛感情を抱くことを「フィクトセクシュアル」とも呼びます。")
ne_knp("その試合で、自慢の強肩を発揮したのがエンジェルスのライト、ハンター・レンフローだ。エンジェルスの１対０で迎えた１回裏だった。１死ニ、三塁のピンチでベルの打球はライト方向への深めのフライ。三塁走者のタッチアップは確実だったが、助走をつけて捕球したレンフローは豪快なレーザービームで三塁へ送球。これが見事なコントロールでタッチアウトを奪い、しかも三塁走者がもたついてホームベースを踏む前の補殺だったため、相手に１点も与えないダブルプレーとなった。")
